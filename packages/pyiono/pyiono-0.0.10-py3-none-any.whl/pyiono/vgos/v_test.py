#!/usr/bin/env python
# coding: utf-8

# In[281]:


import os
import re
import subprocess
from scipy.io import loadmat
import netCDF4 as nc
import shelve
import csv
import shutil

import numpy as np
import statistics
import math
import pyproj
import random

from scipy.optimize import least_squares
import matplotlib.pylab as plt
import matplotlib.cm
import matplotlib.colors
import matplotlib
matplotlib.use('Agg')

import datetime
import time

import collections
from scipy import signal
import scipy

import aacgmv2
from magnetic_field_calculator import MagneticFieldCalculator

import multiprocessing


# In[ ]:





# In[2]:


def get_geomagnetic_lats(lats, lons):
    
    # geographic lat and lon of geomagnetic north pole
    # 1st column -> year
    # 2nd and 3rd columns -> lat and lon
    Geom_P = np.array([[2005, 79.82, -71.81], 
                       [2010, 80.09, -72.21],
                       [2015, 80.37, -72.61], 
                       [2020, 80.65, -72.68],
                       [2025, 80.90, -72.64]])
                
    # interplote the lat and lon for the session year
    lat0 = np.deg2rad(np.interp(2000+int(session[:2]), Geom_P[:,0], Geom_P[:,1]))
    lon0 = np.deg2rad(np.interp(2000+int(session[:2]), Geom_P[:,0], Geom_P[:,2]))
        
    # get the geomagnetic lat for all the stations
    geom_lat = np.arcsin(np.sin(lats)*np.sin(lat0) + 
                         np.cos(lats)*np.cos(lat0)*
                         np.cos(lons - lon0))
    
    return geom_lat            


# In[ ]:





# In[3]:


def get_dip_grid(session):
    
    # parameters: h, grid resolution, year, station lat and lon
#     # create a dictionry for months
#     m2n = {m:i+1 for i, m in enumerate(['JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN', 'JUL', 'AUG', 'SEP', 'OCT', 'NOV','DEC'])}
    
#     # get the session date 
#     date = str(2000+int(session[:2])) + '-' + str(m2n[session[2:5]])+'-'+session[5:7]
    
    # create an object for calculating the magnetic dip 
    calculator = MagneticFieldCalculator(model='IGRF', revision='13', custom_url='https://example.com')
    
    # create a multiprocessing pool
    p = multiprocessing.Pool()
    
    # generate a grid of 2.5x5 in latxlon
    results = p.starmap(calculator.calculate,
                    [(lat, lon, None, None, None, str(2000+int(session[:2])), None) 
                     for lat in np.arange(90,-92.5,-2.5) 
                     for lon in np.arange(-180, 185, 5)])
    
    
    # extract the dips and reshape the grid
    m_dips = np.deg2rad(np.array([result['field-value']['inclination']['value'] for result in results]).reshape((73, 73)))
    
    return m_dips        


# In[4]:


def interpolate_dips(grid, lat, lon):
    
    # bivariately interpolate for the magnetic dip from a grid of 2.5 x 5 degrees in lat x lon
    
    # convert the latitude and longitude from radian to degrees    
    lat, lon = np.rad2deg(lat), np.rad2deg(lon)
    
    # get the indice of the latitude and longitude of the 4 grid points surrounding the site of VGOS/VLBI station or IPP
    latu = math.ceil((90 - lat)*(grid.shape[0]-1)/(180)) # upper latitude
    latl = math.floor((90 - lat)*(grid.shape[0]-1)/(180)) # lower latitude
    lonr = math.ceil((180 + lon)*(grid.shape[1]-1)/360) # right longitude
    lonl = math.floor((180 + lon)*(grid.shape[1]-1)/360) # left longitude
    
    # get the TEC values at the surrounding points
    Eul = grid[latu,lonl]
    Eur = grid[latu,lonr]
    Ell = grid[latl,lonl]
    Elr = grid[latl,lonr]
    
    # get the difference in lat and lon between the VGOS/VLBI station and the lower, left corner
    dlatl = 2.5 - (90 - lat)%2.5
    dlonl = (180 + lon)%5
    
    # get the weights of the surrounding points
    p = dlonl/10
    q = dlatl/5
    Wul = (1 - p)*q # upper, left point
    Wur = p*q # upper, right point
    Wll = (1 - q)*(1 - p) # lower, left point
    Wlr = (1 - q)*p # lower, right point
    
    # get the magnetic dip
    m_dip = sum([Wul*Eul, Wur*Eur, Wll*Ell, Wlr*Elr])
    
    # get the modified dip latitude
    modip = np.arctan(m_dip/np.sqrt(np.cos(np.deg2rad(lat))))
    
    return modip


# In[ ]:





# In[5]:


def get_modips(session, lats, lons):
    #
    
    # convert from radian to degrees
    lats, lons = np.rad2deg(lats), np.rad2deg(lons)
    
    # create a dictionry for months
    m2n = {m:i+1 for i, m in enumerate(['JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN', 'JUL', 'AUG', 'SEP', 'OCT', 'NOV','DEC'])}
    
    # 
    date = str(2000+int(session[:2])) + '-' + str(m2n[session[2:5]])+'-'+session[5:7]
    
    # create an object for calculating the magnetic dip 
    calculator = MagneticFieldCalculator(model='IGRF', revision='13', custom_url='https://example.com')
    
    # create a multiprocessing pool
    p = multiprocessing.Pool()
    
    # generate a grid of 2.5x5 in latxlon
    results = p.starmap(calculator.calculate,
                    [(lat, lons[i], None, None, None, None,date) for i, lat in enumerate(lats)])
        
    # reshape the grid
    m_dips = np.deg2rad(np.array([result['field-value']['inclination']['value'] 
                                  for result in results]).reshape((lons.shape[0])))
    
    modips = np.arctan(m_dips/np.sqrt(np.cos(np.deg2rad(lats))))
    
    return modips        


# In[ ]:





# In[6]:


def IPP_LLA(session, stationLLA, meta_data, geomagnetic, modip, modip_grid):
    
    # calculate IPP Longitude and Latitude    
    for i in range(meta_data.shape[1]): # loop over the reference and remote stations
        for n, item in enumerate(meta_data[:,i,0:3]): # loop over the obervations / IPP
            
            # mean radius of earth and ionospheric layer height
            R, h = 6371.0, 450
            
            # Bull. Geod. Sci, Articles Section, Curitiba, v. 23, no4, p.669 - 683, Oct - Dec, 2017.
            # calculate the Earth-centred angle                      
            Elev = item[1]
            Psi = np.pi/2 - Elev - np.arcsin(R/(R+h)*np.cos(Elev))
            
            # compute the latitude of the IPP
            Az = item[2]
            lat = np.deg2rad(stationLLA[int(item[0])-1,0])         
            Phi = np.arcsin(np.sin(lat)*np.cos(Psi) + np.cos(lat)*np.sin(Psi)*np.cos(Az))
            
            # compute the longitude of the IPP
            lon = np.deg2rad(stationLLA[int(item[0])-1,1])
            Lambda = lon + np.arcsin(np.sin(Psi)*np.sin(Az)/np.cos(Phi))
            
            # save the latitude and the longitude of the ionospheric points
            meta_data[n,i,3] = Phi
            meta_data[n,i,4] = Lambda
            
            # save the latitude and the longitude of the stations
            meta_data[n,i,5] = lat
            meta_data[n,i,6] = lon
    
    
    # convert the lats to geomagnetic lats or modified dip lats
    if geomagnetic:                
        # get the geomagnetic latitude for IPPs
        meta_data[n,i,3] = get_geomagnetic_lats(meta_data[:,:,3], meta_data[:,:,4])
                    
        # get the geomagnetic latitude for all the stations
        meta_data[n,i,3] = get_geomagnetic_lats(meta_data[:,:,5], meta_data[:,:,6])
        
            
    elif modip:
        if modip_grid:            
            # use the grid for fast solution            
            if os.path.isfile('dips_' + str(2000+int(session[:2]))+'.txt'):
                # load the grid
                dips = np.array([line.split() for line in open('dips_' + str(2000+int(session[:2])) + 
                                                               '.txt', 'r').readlines()]).astype(float)
            else:
                # calcuate the dips from scratch
                dips = get_dip_grid(session)
                file = open('dips_' + str(2000+int(session[:2])) +'.txt', 'w') # change the date to year
                np.savetxt(file, dips, fmt='%s')
                file.close()
            
            # get the modifed dip latitude for IPPs
            meta_data[:,0,3] = np.array([interpolate_dips(dips, lat, meta_data[i,0,4]) 
                                         for i, lat in enumerate(meta_data[:,0,3])])
            meta_data[:,1,3] = np.array([interpolate_dips(dips, lat, meta_data[i,1,4]) 
                                         for i, lat in enumerate(meta_data[:,1,3])])
            
            # get the modifed dip latitude for all the stations
            smodips = [interpolate_dips(dips, item[0], item[1]) for item in np.deg2rad(stationLLA)]
            meta_data[:,0,5] = [smodips[int(item)-1] for item in meta_data[:,0,0]]
            meta_data[:,1,5] = [smodips[int(item)-1] for item in meta_data[:,1,0]]
                
        
        else:
            # calculate for all points for accurate solution
            # get the modifed latitude for IPPs
            meta_data[:,0,3] = get_modips(session, meta_data[:,0,3], meta_data[:,0,4])
            meta_data[:,1,3] = get_modips(session, meta_data[:,1,3], meta_data[:,1,4])
            
            # get the modifed latitude for all the stations
            smodips = [get_modips(session, np.array([item[0]]), np.array([item[1]])) 
                       for item in np.deg2rad(stationLLA[:,:2])]
            # map them to the observations
            meta_data[:,0,5] = [smodips[int(item)-1] for item in meta_data[:,0,0]]
            meta_data[:,1,5] = [smodips[int(item)-1] for item in meta_data[:,1,0]]
                            
    return meta_data


# In[ ]:





# In[227]:


def BsElAzIPPLLA(session, geomagnetic, modip, modip_grid, path):
    
    #######
    ########
    
    # read the station file
    try:
        Station = nc.Dataset(path + '/Apriori/Station.nc')
    except:
        print('error: the Station.nc file does not exist in the given path')
        
    # extract the station cartesian coordinates (XYZ)
    stationXYZ = Station['AprioriStationXYZ'][:]
    
    
    #######
    ########
    
    # convert the coordinates of the station from XYZ to longitudate, latitude, and altitude
    # create a tranformation object
    transformer = pyproj.Transformer.from_crs(
        {"proj":'geocent', "ellps":'WGS84', "datum":'WGS84'},
        {"proj":'latlong', "ellps":'WGS84', "datum":'WGS84'})
    
    # latitude, longitude, and altitude order
    stationLLA = np.zeros(shape = (len(stationXYZ[:]), len(stationXYZ[0,:])))
    
    # cartesian(XYZ) to georgraphic(LLA) coordinates
    for n, item in enumerate(stationXYZ[:]):
        # longitude, latitude, and altitude order
        stationLLA[n,1], stationLLA[n,0], stationLLA[n,2] = transformer.transform(item[0], item[1], item[2])
        
    
    #######
    ########
    
    # read the station cross reference file
    try:
        StaCrRef = nc.Dataset(path + '/CrossReference/StationCrossRef.nc')
    except:
        print('error: the StationCrossRef.nc file does not exist in the given path')
    
    # extract the station list
    StationList = StaCrRef['CrossRefStationList'][:]
    nStation = len(StationList)
    
    stations = []
    # decode the string back into ASCII
    for i in range(len(StationList[:])):
        x = []
        for j in range(len(StationList[i,:])):
            x.append(StationList[i,j].decode('UTF-8'))
        # concatenate the letters
        stations.append(''.join(x).replace(' ',''))
        
    # extract the elevation angle and azimuth for each scan and station    
    Scan2Station = StaCrRef['Scan2Station'][:].data
    AzEl2Station = np.zeros(shape=(len(Scan2Station[:,0]),len(stations),2))
    for i in range(len(stations)):
        try:
            AzEl = nc.Dataset(path + stations[i] + '/' + 'AzEl.nc')
        except:
            print('error: the AzEl.nc file does not exist in ' + stations[i] + ' folder' +' within the given path')
        El = AzEl['ElTheo'][:,0].data
        Az = AzEl['AzTheo'][:,0].data
        for n, item in enumerate(Scan2Station[:,i]):
            if item != 0:
                AzEl2Station[n,i,0] = El[item-1]
                AzEl2Station[n,i,1] = Az[item-1]
                
    
    #######
    ########
    
    # read the observation cross reference file
    try:
        ObsCrRef = nc.Dataset(path + '/CrossReference/ObsCrossRef.nc')
    except:
        print('error: the ObsCrossRef.nc file does not exist in the given path')
    
    # extract the elevation angle for each observation and station
    Obs2Scan = ObsCrRef['Obs2Scan'][:].data
    AzEl2Obs = AzEl2Station[Obs2Scan-1]
    
    # get the observations per baseline (station #)
    Obs2Baseline = ObsCrRef['Obs2Baseline'][:].data
            
    # get the elevation angle and the azimuth per station
    El2Station = np.zeros(shape=(len(Obs2Baseline[:,0]),len(Obs2Baseline[0,:])))
    Az2Station = np.zeros(shape=(len(Obs2Baseline[:,0]),len(Obs2Baseline[0,:])))
    for n, i in enumerate(Obs2Baseline[:,:]):
        El2Station[n,:] = AzEl2Obs[n,i[:]-1,0]
        Az2Station[n,:] = AzEl2Obs[n,i[:]-1,1]
            
    
    #######
    ########
       
    # read the source cross reference file
    try:
        SourceCrRef = nc.Dataset(path + '/CrossReference/SourceCrossRef.nc')
    except:
        print('error: the SourceCrossRef.nc file does not exist in the given path')
    
    # get the list of sources
    SourceList = SourceCrRef['CrossRefSourceList'][:].data
        
    Sources = []
    # decode the string back into ASCII
    for i in range(len(SourceList[:])):
        x = []
        for j in range(len(SourceList[i,:])):
            x.append(SourceList[i,j].decode('UTF-8'))
        # concatenate the letters
        Sources.append(''.join(x).replace(' ',''))
    
    # extract the number of the radio source for each observation and station
    Scan2Source = SourceCrRef['Scan2Source'][:].data      
    Obs2Source = Scan2Source[Obs2Scan-1]
    
    
    #######
    ########
    # organize the meta_data
    meta_data = np.zeros(shape=(Obs2Baseline.shape[0],Obs2Baseline.shape[1],8))
    meta_data[:,:,0] = Obs2Baseline
    meta_data[:,:,1] = El2Station
    meta_data[:,:,2] = Az2Station
    meta_data[:,0,7] = Obs2Source
    meta_data[:,1,7] = Obs2Scan    
        
    
    #######
    ########
    # 
    if geomagnetic and modip:
        raise Exception('You can choose either geomagnetic latitude or modip latitude; please, specify.')
    
    # get IPPs
    meta_data = IPP_LLA(session, stationLLA, meta_data, geomagnetic, modip, modip_grid)
                
                
    return nStation, meta_data, stations, stationLLA, stationXYZ.data, Sources


# In[ ]:





# In[ ]:





# In[ ]:




# In[9]:


def design(x, freq, nSta, nPara, s1n, s2n, Elev1, Elev2, 
           lonIPP1, lonIPP2, lonSta1, lonSta2, 
           latIPP1, latIPP2, latSta1, latSta2, 
           t, time_windows, optimize_mf, gradient):
    
    # get the mapping fuctions
    mf1, mf2 = mapping_function(Elev1, Elev2, optimize_mf)
    
    # get the starting and ending of the time window and their corresponding indices  
    if t  < time_windows[-1]:
        for i in range(time_windows.shape[0]):
            if time_windows[i] <= t < time_windows[i+1]:
                indx1 = i 
                indx2 = i+1 # index of 
                t1 = time_windows[i] # starting time of the window
                t2 = time_windows[i+1] # ending time of the window
                break
    else:
        indx1 = time_windows.shape[0]-2
        indx2 = time_windows.shape[0]-1
        t1 = time_windows[-2]
        t2 = time_windows[-1]
    
        
    # vtec
    vtec11 = x[(s1n-1)*nPara + indx1]
    vtec12 = x[(s1n-1)*nPara + indx2]
    vtec21 = x[(s2n-1)*nPara + indx1]
    vtec22 = x[(s2n-1)*nPara + indx2] 
    
    # create a design matrix corresponding to the observation in question
    Ai = np.zeros(shape = (nSta*nPara))
        
    if gradient:
        # two gradient: Gn and Gs
        # ionospheric latitudinal gradient
        Gn1 = x[s1n*nPara - 3]    
        Gs1 = x[s1n*nPara - 2]
        Gn2 = x[s2n*nPara - 3]    
        Gs2 = x[s2n*nPara - 2]    
        
    
        # 1st station in the baseline
        if (latIPP1-latSta1) >= 0:
            # derivative w.r.t vtec11
            Ai[(s1n-1)*nPara + indx1] = -(40.31/freq**2)*mf1*(1+(latIPP1-latSta1)*Gn1)*(1-(t + np.rad2deg(lonIPP1 - lonSta1)/15.0 - t1)/(t2-t1))
            # derivative w.r.t vtec12
            Ai[(s1n-1)*nPara + indx2] = -(40.31/freq**2)*mf1*(1+(latIPP1-latSta1)*Gn1)*(t + np.rad2deg(lonIPP1 - lonSta1)/15.0 - t1)/(t2-t1)
            # derivative w.r.t Gn1
            Ai[s1n*nPara - 3] = -(40.31/freq**2)*mf1*(latIPP1-latSta1)*(vtec11+((t + np.rad2deg(lonIPP1 - lonSta1)/15.0 - t1)/(t2-t1))*(vtec12-vtec11))
        else:
            # derivative w.r.t vtec11
            Ai[(s1n-1)*nPara + indx1] = -(40.31/freq**2)*mf1*(1+(latIPP1-latSta1)*Gs1)*(1-(t + np.rad2deg(lonIPP1 - lonSta1)/15.0 - t1)/(t2-t1))
            # derivative w.r.t vtec12
            Ai[(s1n-1)*nPara + indx2] = -(40.31/freq**2)*mf1*(1+(latIPP1-latSta1)*Gs1)*(t + np.rad2deg(lonIPP1 - lonSta1)/15.0 - t1)/(t2-t1)
            # derivative w.r.t Gs1
            Ai[s1n*nPara - 2] = -(40.31/freq**2)*mf1*(latIPP1-latSta1)*(vtec11+((t + np.rad2deg(lonIPP1 - lonSta1)/15.0 - t1)/(t2-t1))*(vtec12-vtec11))
        # derivative w.r.t instr1
        Ai[s1n*nPara - 1] = -1
                
        # 2nd station in the baseline
        if (latIPP2-latSta2) >= 0:
            # derivative w.r.t vtec21
            Ai[(s2n-1)*nPara + indx1] = (40.31/freq**2)*mf2*(1+(latIPP2-latSta2)*Gn2)*(1-(t + np.rad2deg(lonIPP2 - lonSta2)/15.0 - t1)/(t2-t1))
            # derivative w.r.t vtec22
            Ai[(s2n-1)*nPara + indx2] = (40.31/freq**2)*mf2*(1+(latIPP2-latSta2)*Gn2)*(t + np.rad2deg(lonIPP2 - lonSta2)/15.0 - t1)/(t2-t1)
            # derivative w.r.t Gn2
            Ai[s2n*nPara - 3] = (40.31/freq**2)*mf2*(latIPP2-latSta2)*(vtec21+((t + np.rad2deg(lonIPP2 - lonSta2)/15.0 - t1)/(t2-t1))*(vtec22-vtec21))
        else:
            # derivative w.r.t vtec21
            Ai[(s2n-1)*nPara + indx1] = (40.31/freq**2)*mf2*(1+(latIPP2-latSta2)*Gs2)*(1-(t + np.rad2deg(lonIPP2 - lonSta2)/15.0 - t1)/(t2-t1))
            # derivative w.r.t vtec22
            Ai[(s2n-1)*nPara + indx2] = (40.31/freq**2)*mf2*(1+(latIPP2-latSta2)*Gs2)*(t + np.rad2deg(lonIPP2 - lonSta2)/15.0 - t1)/(t2-t1)
            # derivative w.r.t Gs2
            Ai[s2n*nPara - 2] = (40.31/freq**2)*mf2*(latIPP2-latSta2)*(vtec21+((t + np.rad2deg(lonIPP2 - lonSta2)/15.0 - t1)/(t2-t1))*(vtec22-vtec21))
        # derivative w.r.t instr2
        Ai[s2n*nPara - 1] = 1
        
    else:        
        # one gradient: Gns
        # ionospheric latitudinal gradient
        Gns1 = x[s1n*nPara - 2] 
        Gns2 = x[s2n*nPara - 2]    
        
    
        # 1st station in the baseline        
        # derivative w.r.t vtec11
        Ai[(s1n-1)*nPara + indx1] = -(40.31/freq**2)*mf1*(1+(latIPP1-latSta1)*Gns1)*(1-(t + np.rad2deg(lonIPP1 - lonSta1)/15.0 - t1)/(t2-t1))
        # derivative w.r.t vtec12
        Ai[(s1n-1)*nPara + indx2] = -(40.31/freq**2)*mf1*(1+(latIPP1-latSta1)*Gns1)*(t + np.rad2deg(lonIPP1 - lonSta1)/15.0 - t1)/(t2-t1)
        # derivative w.r.t Gn1
        Ai[s1n*nPara - 2] = -(40.31/freq**2)*mf1*(latIPP1-latSta1)*(vtec11+((t + np.rad2deg(lonIPP1 - lonSta1)/15.0 - t1)/(t2-t1))*(vtec12-vtec11))
        # derivative w.r.t instr1
        Ai[s1n*nPara - 1] = -1
                
        # 2nd station in the baseline
        # derivative w.r.t vtec21
        Ai[(s2n-1)*nPara + indx1] = (40.31/freq**2)*mf2*(1+(latIPP2-latSta2)*Gns2)*(1-(t + np.rad2deg(lonIPP2 - lonSta2)/15.0 - t1)/(t2-t1))
        # derivative w.r.t vtec22
        Ai[(s2n-1)*nPara + indx2] = (40.31/freq**2)*mf2*(1+(latIPP2-latSta2)*Gns2)*(t + np.rad2deg(lonIPP2 - lonSta2)/15.0 - t1)/(t2-t1)
        # derivative w.r.t Gn2
        Ai[s2n*nPara - 2] = (40.31/freq**2)*mf2*(latIPP2-latSta2)*(vtec21+((t + np.rad2deg(lonIPP2 - lonSta2)/15.0 - t1)/(t2-t1))*(vtec22-vtec21))
        # derivative w.r.t instr2
        Ai[s2n*nPara - 1] = 1
            
    return Ai


# In[10]:


def observed_computed(x, freq, nSta, nPara, s1n, s2n, Elev1, Elev2, 
                      lonIPP1, lonIPP2, lonSta1, lonSta2, 
                      latIPP1, latIPP2, latSta1, latSta2, 
                      y, t, time_windows, optimize_mf, gradient):
    
    # get the mapping fuctions
    mf1, mf2 = mapping_function(Elev1, Elev2, optimize_mf)        
    
    # get the starting and ending of the time window and their corresponding indices
    if t  < time_windows[-1]:
        for i in range(time_windows.shape[0]):
            if time_windows[i] <= t < time_windows[i+1]:
                indx1 = i 
                indx2 = i+1 # index of 
                t1 = time_windows[i] # starting of the time window
                t2 = time_windows[i+1] # ending of the time window
                break
    else:
        indx1 = time_windows.shape[0]-2
        indx2 = time_windows.shape[0]-1
        t1 = time_windows[-2]
        t2 = time_windows[-1]
        
    # instrumental delay constant
    instr1 = x[s1n*nPara - 1]    
    instr2 = x[s2n*nPara - 1]
            
    # vtec
    vtec11 = x[(s1n-1)*nPara + indx1]
    vtec12 = x[(s1n-1)*nPara + indx2]
    vtec21 = x[(s2n-1)*nPara + indx1]
    vtec22 = x[(s2n-1)*nPara + indx2]
    
    if gradient:
        # two gradient: Gn and Gs
        # ionospheric latitudinal gradient
        Gn1 = x[s1n*nPara - 3]    
        Gs1 = x[s1n*nPara - 2]
        Gn2 = x[s2n*nPara - 3]  
        Gs2 = x[s2n*nPara - 2]
        
        # 1st station    
        if (latIPP1-latSta1) >= 0:
            fun1 = mf1*(1+(latIPP1-latSta1)*Gn1)*(vtec11+((t + np.rad2deg(lonIPP1 - lonSta1)/15.0 - t1)/(t2-t1))*(vtec12-vtec11))
        else:
            fun1 = mf1*(1+(latIPP1-latSta1)*Gs1)*(vtec11+((t + np.rad2deg(lonIPP1 - lonSta1)/15.0 - t1)/(t2-t1))*(vtec12-vtec11))
    
        # 2nd station
        if (latIPP2-latSta2) >= 0:
            fun2 = mf2*(1+(latIPP2-latSta2)*Gn2)*(vtec21+((t + np.rad2deg(lonIPP2 - lonSta2)/15.0 - t1)/(t2-t1))*(vtec22-vtec21)) 
        else:
            fun2 = mf2*(1+(latIPP2-latSta2)*Gs2)*(vtec21+((t + np.rad2deg(lonIPP2 - lonSta2)/15.0 - t1)/(t2-t1))*(vtec22-vtec21)) 
        
    else:
        # one gradient: Gns
        # ionospheric latitudinal gradient
        Gns1 = x[s1n*nPara - 2]
        Gns2 = x[s2n*nPara - 2]
        
        # 1st station 
        fun1 = mf1*(1+(latIPP1-latSta1)*Gns1)*(vtec11+((t + np.rad2deg(lonIPP1 - lonSta1)/15.0 - t1)/(t2-t1))*(vtec12-vtec11))
        
        # 2nd station
        fun2 = mf2*(1+(latIPP2-latSta2)*Gns2)*(vtec21+((t + np.rad2deg(lonIPP2 - lonSta2)/15.0 - t1)/(t2-t1))*(vtec22-vtec21)) 
    
 
    
    return y - ((40.31/freq**2)*(fun2 - fun1) + (instr2 - instr1))


# In[ ]:





# In[11]:


# parase the ionospheric map 
def parse_map(tecmap, exponent = -1):
    exponent = tecmap.find('Exponent')
    tecmap = re.split('.*END OF TEC MAP', tecmap)[0]
    return np.stack([np.fromstring(l, sep=' ') for l in re.split('.*LAT/LON1/LON2/DLON/H\\n',tecmap)[1:]])*10**exponent

# get the GIMs file
def get_tecmaps(filename):
    with open(filename) as file:
        ionex = file.read()
        return [parse_map(t) for t in ionex.split('START OF TEC MAP')[1:]]

# extract the VTEC at a specific location using Bivariate Interpolation
def get_tec(tecmap, lat, lon):
    # get the indices of the latitudes and longitudes of the 4 GIMs points surrounding the site of VGOS/VLBI station
    latu = math.ceil((87.5 - lat)*(tecmap.shape[0]-1)/(2*87.5)) # upper latitude
    latl = math.floor((87.5 - lat)*(tecmap.shape[0]-1)/(2*87.5)) # lower latitude
    lonr = math.ceil((180 + lon)*(tecmap.shape[1]-1)/360) # right longitude
    lonl = math.floor((180 + lon)*(tecmap.shape[1]-1)/360) # left longitude
    
    # get the TEC values at the surrounding points
    Eul = tecmap[latu,lonl]
    Eur = tecmap[latu,lonr]
    Ell = tecmap[latl,lonl]
    Elr = tecmap[latl,lonr]
    
    # get the difference in lat and lon between the VGOS/VLBI station and the lower, left corner
    dlatl = 2.5 - (87.5 - lat)%2.5
    dlonl = (180 + lon)%5
    
    # get the weights of the surrounding points
    p = dlonl/5
    q = dlatl/2.5
    Wul = (1 - p)*q # upper, left point
    Wur = p*q # upper, right point
    Wll = (1 - q)*(1 - p) # lower, left point
    Wlr = (1 - q)*p # lower, right point
    
    E = sum([Wul*Eul, Wur*Eur, Wll*Ell, Wlr*Elr])
    
    return E

def ionex_local_path(directory):
    file = os.listdir(directory)
    return directory + '/' + file[0]


# In[12]:


def doy(YMD):
    
    # get the year, month, and day
    year, month, day = 2000 + int(YMD[0]), int(YMD[1]), int(YMD[2])    
        
    # create a list for days
    days = []
    # find the day of year corresponding to this session
    startDate = datetime.date(year, 1, 1)
    endDate = datetime.date(year, month, day)
    delta = (endDate - startDate).days + 1
    thisD = delta
    # append it to the list of days
    days.append(str(thisD).rjust(3,'0'))   
    
    
    # get the last day of year
    endDate = datetime.date(year, 12, 31)
    lastD = (endDate - startDate).days + 1       
    
    # get the next day of year if the day isn't the last day in the year
    if thisD != lastD:        
        # get the next day of year
        nxtD = delta + 1
        # append it to the list of days
        days.append(str(nxtD).rjust(3,'0'))
    # else, save the 1st day in the next year
    else:
        days.append(str(1).rjust(3,'0'))
            
    return days   


# In[13]:


def initial_values(nSta, nPara, rcindx, gradient):  
    
    # create a variable for the estimates
    x0 = np.zeros(shape = (nSta * nPara))    
    
    # loop over the stations
    for j in range(nSta):        
        # set the initial values of the instrumental delay and ionospheric gradients
        x0[((j+1)*nPara-1)] = random.uniform(-5,5)
        
        if gradient:
            # two gradient: Gn and Gs
            x0[(j+1)*nPara-3:(j+1)*nPara-1] = [random.uniform(-1,1) for i in range((j+1)*nPara-3,(j+1)*nPara-1)]
        else:
            # one gradient: Gns
            x0[(j+1)*nPara-2] = random.uniform(-1,1)
        
        # get the initial values of the VTEC estimates from GIMs 
        for i in range(rcindx.shape[0]):
            if rcindx[i,j] != 0:
                # vtec
                x0[j*nPara+i] = random.uniform(2,20)
                
        if rcindx[i,j] != 0:
            # vtec
            x0[j*nPara+i+1] = random.uniform(2,20)
            
    # set the instrumental delay of the last station to zero as a constraint
    x0[((j+1)*nPara-1)] = 0
    
    return x0


# In[14]:


def mapping_function(elev1, elev2, optimize_mf = 1):
    
    # the mean radius of the Earth in km
    R = 6371.0
        
    if optimize_mf:
        # the height of th ionospheric layer in km
        h = 506.7
        
        # alpha parameter
        alpha = 0.9782
    
        # get the mapping function
        mf1 = 1.0/((1.0-(((R*np.cos(alpha*elev1))/(R+h))**2))**0.5)
        mf2 = 1.0/((1.0-(((R*np.cos(alpha*elev2))/(R+h))**2))**0.5)
        
    else:
        # the mean radius of the Earth and the height of th ionospheric layer in km
        h = 450.0
    
        # get the mapping function
        mf1 = 1.0/((1.0-(((R*np.cos(elev1))/(R+h))**2))**0.5)
        mf2 = 1.0/((1.0-(((R*np.cos(elev2))/(R+h))**2))**0.5)
    
    return mf1, mf2    


# In[15]:


def include_stations(stations, cs, exSta = []):
    
    # find the indices of the stations to be excluded  
    exStaIndx = [stations.index(i) for i in exSta] 
            
    # find the indices of the observations of the remaining stations; 
    # the corresponding column of the stations will later be deleted automatically
    inindx = [i for i in range(len(cs[:,0,0])) if cs[i,0,0]-1 not in exStaIndx or cs[i,1,0]-1 not in exStaIndx]
    
    return inindx


# In[ ]:





# In[16]:


def vgos_dTEC(path):
    
    ###
    # read the DiffTec.nc file
    try:
        ds = nc.Dataset(path + '/Observables/DiffTec.nc')
    except:
        print('error: the DiffTec.nc file does not exist in the given path')
    
    dtec = ds['diffTec'][:].data
    dtecstd = ds['diffTecStdDev'][:].data    
    
    return dtec, dtecstd


# In[17]:


def vlbi_dTEC(path):
    
    ###
    # read the file
    try:
        ds = nc.Dataset(path + '/ObsDerived/Cal-SlantPathIonoGroup_bX.nc')
    except:
        print('error: the DiffTec.nc file does not exist in the given path')
    
    dtec = ds['Cal-SlantPathIonoGroup'][:,0].data
    dtecstd = ds['Cal-SlantPathIonoGroupSigma'][:,0].data    
    
    return dtec, dtecstd


# In[ ]:





# In[18]:


def v_processing(session, resolution = 60, exSta = [], snr = 0, cutoffangle = 0, optimize_mf = 1, rel_constraints = 1,
                 outlier_detection = 1, minObs = 5, vce = 1, sum_instr_offsets = 0, vgosDB_path = 'Data/vgosDB/', 
                 v_output_path = 'Results/', error_bar = 1, gradient = 1, gims = 1, madrigal = 1, 
                 ionex_path = 'Data/Ionex/', geomagnetic = 0, modip = 1, modip_grid = 1):
    
    # exSta: enter the names of the stations to be left out
    
    # read VGOS/VLBI data
    h0, freq, nSta, stations, stationLLA, stationXYZ, meta_data, dtec, dtecstd, t, v_doy, Sources, s2nr = v_data(session, 
                                                                                                                 exSta,
                                                                                                                 snr,
                                                                                                                 cutoffangle,
                                                                                                                 minObs,
                                                                                                                 vgosDB_path,
                                                                                                                 geomagnetic,
                                                                                                                 modip,
                                                                                                                 modip_grid)
    
    # get the number of Parameters
    nPara, time_windows = nPara_time_window(t, gradient, resolution)    
    nPara = int(nPara)
    # input('Please, enter the time interval in min, i.e. 15, 30, or 60')
    # extract the observations
    freq, meta_data, sta, elev, latIPP, lonIPP, latSta, lonSta, dtec, dtecstd, t, s2nr = extract_observations(freq, s2nr,
                                                                                                              meta_data,
                                                                                                              dtec, dtecstd,
                                                                                                              t)
    
    # get the time windows w/o observations
    rel_cindxe, cindxe, cindxr, rcindx, c = column_index(nSta, nPara, sta[:,0], sta[:,1], t, time_windows, 
                                                         rel_constraints, sum_instr_offsets, gradient)        
        
    # get the initial values
    x0 = initial_values(nSta, nPara, rcindx, gradient)
    
    if outlier_detection:
        
        print('outlier detection is running')
        # eliminate outliers
        freq, meta_data, sta, elev, latIPP, lonIPP, latSta, lonSta, dtec, dtecstd, t, s2nr, x0, orindx = data_snooping(h0, freq,
                                                                                                                       nSta, nPara, 
                                                                                                                       s2nr, meta_data,
                                                                                                                       stationLLA, 
                                                                                                                       stationXYZ, 
                                                                                                                       dtec, dtecstd, 
                                                                                                                       t, time_windows, 
                                                                                                                       optimize_mf, v_doy, 
                                                                                                                       sum_instr_offsets,
                                                                                                                       gradient)
        
        
        # get an update on the time windows w/o observations
        rel_cindxe, cindxe, cindxr, rcindx, c = column_index(nSta, nPara, sta[:,0], sta[:,1], t, time_windows,
                                                             rel_constraints, sum_instr_offsets, gradient)
        
        print('all possible outliers were eliminated')
        
            
    #print(len(t))
    #print(rcindx)
    #print(c)
    
    # refine the estimates    
    x0, sxx, r, Obs2Source = refine_parameters(freq, s2nr, nSta, nPara, x0, meta_data, stationXYZ, dtec, dtecstd, t,
                                               time_windows, optimize_mf, rel_constraints, vce, sum_instr_offsets, gradient)
              
    # map the parameters
    param = mapping_parameters(nSta, nPara, resolution, stations, stationLLA, rcindx, exSta, x0, sxx, 
                               h0, time_windows, session, gradient, gims, madrigal, v_doy, ionex_path)
    
    # save the plots of the remaining stations
    v_plot(session, resolution, stations, stationLLA, int(h0), int(h0) + time_windows[-1],
           param, gims, madrigal, exSta, error_bar, v_output_path)
    
    # save the parameters in a text file
    save_results(param, session, gradient, madrigal, gims, v_output_path)
    
    # calculate VGOS/VLBI bias w.r.t GIMs and Madrigal
    v_bias = v_gims_madr_bias(param)
    
    return #param, v_bias, r, Obs2Source, Sources, t, s2nr


# In[19]:


def data_snooping(h0, freq, nSta, nPara, s2nr, meta_data, stationLLA, stationXYZ, dtec, 
                  dtecstd, t, time_windows, optimize_mf, v_doy, sum_instr_offsets, gradient):
    
    # don't apply VCE because it's too sensitive to outliers
    # don't apply relative constraint
    rel_constraints = 0
    
    # extract the observations
    freq, meta_data, sta, elev, latIPP, lonIPP, latSta, lonSta, dtec, dtecstd, t, s2nr = extract_observations(freq, s2nr,
                                                                                                              meta_data, 
                                                                                                              dtec, dtecstd,
                                                                                                              t)
    
    # get an update on the time windows w/o observations
    rel_cindxe, cindxe, cindxr, rcindx, c = column_index(nSta, nPara, sta[:,0], sta[:,1], t, time_windows, 
                                                         rel_constraints, sum_instr_offsets, gradient)
            
    # get the initial values
    x0 = initial_values(nSta, nPara, rcindx, gradient)
    
    # get the weights
    W = obs_weights(elev, dtecstd, meta_data, stationXYZ, optimize_mf)
        
                
    #
    niter_0 = 1
    nObs = len(t)
    #print('nObs', nObs)
    oindxr = []
    while True:
        
        # get the estimates
        niter_1 = 0
        rchisqr_before = 1
        while True:
            
            # calculate the corrections for the estimates
            x0, sxx, dx, A, rchisqr, r = helmertlsq(rel_cindxe, cindxe, cindxr, x0, freq, nSta,
                                                    nPara, sta[:,0], sta[:,1], elev[:,0], elev[:,1],
                                                    lonIPP[:,0], lonIPP[:,1], lonSta[:,0], lonSta[:,1],
                                                    latIPP[:,0], latIPP[:,1], latSta[:,0], latSta[:,1], 
                                                    dtec, dtecstd, t, time_windows, optimize_mf, W,
                                                    rel_constraints, sum_instr_offsets, gradient)    
                    
            niter_1 += 1         
            #print('rchisqr_1', rchisqr, abs(rchisqr-rchisqr_before))
            # iterate for at least the min. # of iteration, i.e. 3 times
            # break if the change in the reference variance is below the threshold
            # or the number of iterations reaches the max. # of iterations 
            if  abs(rchisqr-rchisqr_before) < 1e-2 and niter_1 > 3 or niter_1 > 1e1:    
                break
            rchisqr_before = rchisqr
            
        # delete the last column representing the instrumental offset of the last station as a constraint
        # delete the columns of the parameters with no observations from the A matrix 
        a = np.delete(A, cindxe.astype(int), 1)
                    
        # form the matric of the lsq
        neqA = np.transpose(a).dot(W).dot(a)
        
        # calculate the co-variance matrix of the estimates    
        QxxA = np.linalg.inv(neqA)
    
        # calculate the co-variance matrix of the residuals
        QvvA = np.linalg.inv(W) - a.dot(QxxA).dot(np.transpose(a))
        
        # calculate the standardized residuals
        r_ = abs(r)/np.sqrt(abs(np.diag(QvvA)))
        
        # get the index of the observation with the maximum normalized residual
        indx = [list(r_).index(max(r_))]
        
        # calculate sigma
        s0 = np.sqrt(rchisqr)
        
        # using the student test, check whether the corresponding observation is an outlier
        # 1- aplha the significance level of the test, and 1 - beta the power of the test.
        # 6.6 corrosponds to alpha = 0.001 and beta = 0.999 >>> confidence level 99.9%
        # 3.29 as a rejection criteria corrosponds to alpha = 0.001  and beta =  >>> confidence level 99.9%
        if r_[indx] > 3.29*s0: # 3.29, 6.6
            #print('indxr', list(abs(r)).index(max(abs(r))), 'maxr', round(max(abs(r)),3), 'cr_', 
            #      round(float(r_[list(abs(r)).index(max(abs(r)))]),3), 'indxr_', indx, 'maxr_', 
            #      round(float(r_[indx]),3), 'cr', round(float(r[indx]),3), 'rej', round(3.29*s0,3))
            
            # if yes, remove it
            # extract the observations
            freq, meta_data, sta, elev, latIPP, lonIPP, latSta, lonSta, dtec, dtecstd, t, s2nr = extract_observations(freq,
                                                                                                                      s2nr,
                                                                                                                      meta_data,
                                                                                                                      dtec,
                                                                                                                      dtecstd, 
                                                                                                                      t,
                                                                                                                      eindx =
                                                                                                                      indx)
            
            # get the weights
            W = obs_weights(elev, dtecstd, meta_data, stationXYZ, optimize_mf, eindx = indx, W = W)
            
            
            oindxr.append(indx[0])
        
            # get an update on the time windows w/o observations
            rel_cindxe, cindxe, cindxr, rcindx, c = column_index(nSta, nPara, sta[:,0], sta[:,1], t, time_windows,
                                                                 rel_constraints, sum_instr_offsets, gradient)
            
        else:
            break    
    
        
        # break if the number of iterations (outliers) reaches 5% of the data
        #niter_0 += 1
        #if niter_0 > int(nObs*5e-1):
            #break
            
    #print(len(oindxr))        
    return freq, meta_data, sta, elev, latIPP, lonIPP, latSta, lonSta, dtec, dtecstd, t, s2nr, x0, oindxr


# In[20]:


def obs_epochs(path):
    
    ###
    # read the TimeUTC.nc file
    try:
        t = nc.Dataset(path + '/Observables/TimeUTC.nc')
    except:
        print('error: the TimeUTC.nc file does not exist in the given path')
    
    # 
    YMD = t['YMDHM'][0,0:3].data
    
    # extract the starting time of the session
    h0 = t['YMDHM'][0,3].data
        
    # extract the epoch of the observation
    h = t['YMDHM'][:,3].data + t['YMDHM'][:,4].data/60 + t['Second'][:].data/(60**2)
    
    # get the starting date
    date0 = datetime.date(2000+t['YMDHM'][0,0].data, t['YMDHM'][0,1].data, t['YMDHM'][0,2].data)    
    for i in range(len(h)):
        # calcuate the ending date       
        date1 = datetime.date(2000+t['YMDHM'][i,0].data, t['YMDHM'][i,1].data, t['YMDHM'][i,2].data)
        # calculate the difference in days between the starting and ending dates
        did = (date1 - date0).days
        # calculate the hours since the start of the session 
        h[i] = h[i] + (24*(did) - h0)
    
    # return the starting time and the epoch
    return h0, h, YMD


# In[21]:


def helmertlsq(rel_cindxe, cindxe, cindxr, x0, freq, nSta, nPara, s1n, s2n, Elev1, Elev2, lonIPP1, 
               lonIPP2, lonSta1, lonSta2, latIPP1, latIPP2, latSta1, latSta2, dtec, dtecstd, t, 
               time_windows, optimize_mf, W, rel_constraints, sum_instr_offsets, gradient):
    
    # initialize some variables
    A = np.zeros(shape = (len(t),nSta*nPara))
    b = np.zeros(shape = (len(t)))
    
    for i in range(len(t)):
        
        # form the A matrix
        A[i,:] = design(x0, freq[i], nSta, nPara, 
                        int(s1n[i]), int(s2n[i]), Elev1[i], Elev2[i], 
                        lonIPP1[i], lonIPP2[i], lonSta1[i], lonSta2[i], 
                        latIPP1[i], latIPP2[i], latSta1[i], latSta2[i],
                        t[i], time_windows, optimize_mf, gradient)
        
        # form the residual vector
        b[i] = observed_computed(x0, freq[i], nSta, nPara, 
                                 int(s1n[i]), int(s2n[i]), Elev1[i], Elev2[i], 
                                 lonIPP1[i], lonIPP2[i], lonSta1[i], lonSta2[i], 
                                 latIPP1[i], latIPP2[i], latSta1[i], latSta2[i], 
                                 dtec[i], t[i], time_windows, optimize_mf, gradient)       
        
    
    if rel_constraints:        
        # get the parameters of the pseudo-observations
        H, h, Wc = pseudo_obs(cindxe, nPara, nSta,x0, gradient)         
        
        # delete the last column representing the instrumental offset of the last station as a constraint
        # delete the columns of the parameters with no observations from the A matrix 
        a = np.delete(A, cindxe.astype(int), 1)
        
        # form the matric of the lsq
        neqA = np.transpose(a).dot(W).dot(a)         
        neqH = np.transpose(H).dot(Wc).dot(H)
        neqT = neqA + neqH 
        
        f = np.transpose(a).dot(W).dot(b) + np.transpose(H).dot(Wc).dot(h)
        
        if sum_instr_offsets:
            # enforce the condition that the sum of instr offsets equal zero
            constr_eq = np.zeros(nSta*nPara)
            for i in range(nSta):
                constr_eq[(i+1)*nPara-1] = 1.0
            constr_eq = np.delete(constr_eq, cindxe.astype(int), 0)
            constr_eq.shape
            
            # concatenate the matrices
            neqT = np.concatenate((neqT, np.expand_dims(np.transpose(constr_eq), axis=1)), axis=1)
            neqT = np.concatenate((neqT, np.expand_dims(np.concatenate((constr_eq,[0]), axis = 0), axis = 0)), axis=0)
            f = np.concatenate((f, [-sum([x0[(i+1)*nPara-1] for i in range(nSta)])]), axis = 0)
            
            # calculate the corrections for the estimates
            dx = np.linalg.inv(neqT).dot(f)  
            
            # get the residuals
            r = a.dot(dx[:-1]) - b
            rh = H.dot(dx[:-1]) - h
        
        else:
            # calculate the corrections for the estimates
            dx = np.linalg.inv(neqT).dot(f)  
        
            # get the residuals
            r = a.dot(dx) - b
            rh = H.dot(dx) - h   
            
        # calculate the degree of freedom, # of obs - # of unknown + # of constrained parameters without obs
        if sum_instr_offsets: 
            dof = len(r)-len(cindxr)+(len(rel_cindxe)-len(cindxe)) + 1
        else:
            dof = len(r)-len(cindxr)+(len(rel_cindxe)-len(cindxe))
        
        # calculate the reduced-chi squared (reference variance)
        rchisqr = (np.transpose(r).dot(W).dot(r) + np.transpose(rh).dot(Wc).dot(rh))/dof
        
        # calculate sigma
        s0 = np.sqrt(rchisqr)
        
        # calculate the co-variance matrix of the estimates
        Qxx = np.linalg.inv(neqT)
        
        # get the formal errors of the estimates
        sx = s0*np.sqrt(abs(np.diag(Qxx)))
        
    else: 
        # delete the last column representing the instrumental offset of the last station as a constraint
        # delete the columns of the parameters with no observations from the A matrix 
        a = np.delete(A, cindxe.astype(int), 1)
    
        # form the matric of the lsq
        neqA = np.transpose(a).dot(W).dot(a)   
        f = np.transpose(a).dot(W).dot(b)
        
        if sum_instr_offsets:
            # enforce the condition that the sum of instr offsets equals zero
            constr_eq = np.zeros(nSta*nPara)
            for i in range(nSta):
                constr_eq[(i+1)*nPara-1] = 1.0
            constr_eq = np.delete(constr_eq, cindxe.astype(int), 0)
            
            # concatenate the matrices
            neqA = np.concatenate((neqA, np.expand_dims(np.transpose(constr_eq), axis=1)), axis=1)
            neqA = np.concatenate((neqA, np.expand_dims(np.concatenate((constr_eq,[0]), axis = 0), axis = 0)), axis=0)
            f = np.concatenate((f, [-sum([x0[(i+1)*nPara-1] for i in range(nSta)])]), axis = 0)
        
            # calculate the corrections for the estimates
            dx = np.linalg.inv(neqA).dot(f)
        
            # get the residuals
            r = a.dot(dx[:-1]) - b
            
        else:
            # calculate the corrections for the estimates
            dx = np.linalg.inv(neqA).dot(f)
        
            # get the residuals
            r = a.dot(dx) - b
        
        if sum_instr_offsets:
            # calculate the degree of freedom
            dof = len(r)-len(cindxr) + 1
        else:
            # calculate the degree of freedom
            dof = len(r)-len(cindxr)
    
        # calculate the reduced-chi squared (reference variance)
        rchisqr = np.transpose(r).dot(W).dot(r)/dof
        
        # calculate sigma
        s0 = np.sqrt(rchisqr)
        
        # calculate the co-variance matrix of the estimates
        Qxx = np.linalg.inv(neqA)
        
        # get the formal errors of the estimates
        sx = s0*np.sqrt(abs(np.diag(Qxx)))
    
    # add the corrections to the estimates and map the formal errors to the estimates
    sxx = np.zeros(nPara*nSta)
    for n, item in enumerate(cindxr):
        x0[item] = x0[item] + dx[n]
        sxx[item] = sx[n]
        
    return x0, sxx, dx, A, rchisqr, r


# In[22]:


def refine_parameters(freq, s2nr, nSta, nPara, x0, meta_data, stationXYZ, dtec, dtecstd, t, 
                      time_windows, optimize_mf, rel_constraints, vce, sum_instr_offsets, gradient):
    
    # extract the observations
    freq, meta_data, sta, elev, latIPP, lonIPP, latSta, lonSta, dtec, dtecstd, t, s2nr = extract_observations(freq, s2nr,
                                                                                                              meta_data,
                                                                                                              dtec, dtecstd,
                                                                                                              t)
    
    # get an update on the time windows w/o observations
    rel_cindxe, cindxe, cindxr, rcindx, c = column_index(nSta, nPara, sta[:,0], sta[:,1], 
                                                         t, time_windows, rel_constraints, sum_instr_offsets, gradient)
        
    
    # get the weights
    W = obs_weights(elev, dtecstd, meta_data, stationXYZ, optimize_mf)
        
    # get the estimates    
    niter_0 = 0
    rchisqr_before = 1
    while True:
        
        # calculate the corrections for the estimates
        x0, sxx, dx, A, rchisqr, r = helmertlsq(rel_cindxe, cindxe, cindxr, x0, freq, nSta, 
                                                nPara, sta[:,0], sta[:,1], elev[:,0], elev[:,1],
                                                lonIPP[:,0], lonIPP[:,1], lonSta[:,0], lonSta[:,1],
                                                latIPP[:,0], latIPP[:,1], latSta[:,0], latSta[:,1], 
                                                dtec, dtecstd, t, time_windows, optimize_mf, W, 
                                                rel_constraints, sum_instr_offsets, gradient)                
        
        niter_0 += 1
        print('rchisqr_0', rchisqr, abs(rchisqr_before-rchisqr))
        # iterate for at least the min. # of iteration, i.e. 3 times
        # break if the change in the reference variance is below the threshold
        # or the number of iterations reaches the max. # of iterations 
        if abs(rchisqr-rchisqr_before) < 1e-2 and niter_0 > 3 or niter_0 > 1e1:    
            break
        rchisqr_before = rchisqr
        
        
    # refine the stochastic model and re-do the adjustment
    # get the observations per source  
    Obs2Source = meta_data[:,0,7]  
    if vce:
        niter_1 = 0    
        while True:
        
            # finesse the stochastic model and redo the adjustment
            W = variance_component_estimation(rel_cindxe, cindxr, Obs2Source, sta, W, r, x0, dx, A)
        
            niter_2 = 0
            rchisqr_before = 1
            while True:
            
                # calculate the corrections for the estimates
                x0, sxx, dx, A, rchisqr, r = helmertlsq(rel_cindxe, cindxe, cindxr, x0, freq, nSta, 
                                                        nPara, sta[:,0], sta[:,1], elev[:,0], elev[:,1],
                                                        lonIPP[:,0], lonIPP[:,1], lonSta[:,0], lonSta[:,1],
                                                        latIPP[:,0], latIPP[:,1], latSta[:,0], latSta[:,1],
                                                        dtec, dtecstd, t, time_windows, optimize_mf, W, 
                                                        rel_constraints, sum_instr_offsets, gradient)
        
                niter_2 += 1         
                #print('rchisqr_1', rchisqr, abs(rchisqr-rchisqr_before))
                # iterate for at least the min. # of iteration, i.e. 3 times
                # break if the change in the reference variance is below the threshold
                # or the number of iterations reaches the max. # of iterations 
                if  abs(rchisqr-rchisqr_before) < 1e-2 and niter_2 > 3 or niter_2 > 1e1:    
                    break
                rchisqr_before = rchisqr
            
        
            niter_1 += 1
            print('rchisqr_2', rchisqr, 1-rchisqr)
            # iterate for at least the min. # of iteration, i.e. 5 times
            # break if the change in the reference variance is below the threshold
            # or the number of iterations reaches the max. # of iterations 
            if abs(1-rchisqr) < 5e-4 and niter_1 >= 3 or niter_1 > 1e1: 
                break   
    
    return x0, sxx, r, Obs2Source


# In[23]:


def variance_component_estimation(rel_cindxe, cindxr, Obs2Source, sta, W, r, x0,
                                  dx, A, source_based = 1, baseline_based = 1):
    
    # apply VCE only once the data is free from outliers
    
    # delete the column of the parameters with no observation but are relatively constraints
    a = np.delete(A,rel_cindxe,1)
    
    # get the normal equations
    neqA = np.transpose(a).dot(W).dot(a)
    
    # calculate the co-variance matrix of the estimates    
    QxxA = np.linalg.inv(neqA)
    
    # calculate the co-variance matrix of the residuals
    QvvA = np.linalg.inv(W) - a.dot(QxxA).dot(np.transpose(a))
    
    # calculate the redundancy matrix
    RA = QvvA.dot(W)
    #print(sum(np.diag(RA)))
    
    # get the baselines
    baseline = [str(int(sta[i,0])) + ' - ' + str(int(sta[i,1])) for i in range(len(sta[:,0]))] 
    
    # get the stations
    stations = sorted(set(list(set(sta[:,0])) + list(set(sta[:,1]))))
    
    # save the input weighting matrix to be used in the estimation of the variance components
    W0 = W
    
    # apply source-based VCE
    if source_based:
        
        indx = {} # indices of residuals per source
        vPs = {} # variance component per source 
        
        for i in set(Obs2Source):            
            
            # get the indices of residuals per source
            indx[i] = [j for j in range(len(r))  if Obs2Source[j] == i]
        
            # get the variance component of unit weight per source group
            vPs[i] = np.transpose(r[indx[i]]).dot(np.diag(W0[indx[i],indx[i]])).dot(r[indx[i]])/sum(RA[indx[i],indx[i]])
            #print(vPs[i],len(indx[i]))
        
            # scale the weight of each group by its variance component
            W[indx[i],indx[i]] = W[indx[i],indx[i]]/vPs[i]
            
    
    # apply baseline_based VCE
    if baseline_based:
        
        indx = {} # indices of residuals per baseline
        vPb = {} # variance component per baseline
        
        for i in sorted(set(baseline)):
            
            # get the indices of residuals per baseline
            indx[i] = [j for j in range(len(baseline))  if i in baseline[j]]
        
            # get the variance component of unit weight per source group
            vPb[i] = np.transpose(r[indx[i]]).dot(np.diag(W0[indx[i],indx[i]])).dot(r[indx[i]])/sum(RA[indx[i],indx[i]]) 
            #print(vPb[i],len(indx[i]))
        
            # scale the weight of each group by its variance component
            W[indx[i],indx[i]] = W[indx[i],indx[i]]/vPb[i]
    
    return W


# In[24]:


def pseudo_obs(cindxe, nPara, nSta, x0, gradient):
    
    if gradient:
        # two gradients: Gn and Gs
        g = 2
    else:
        # one gradient: Gns
        g = 1
    
    # initialize some variables for the design matrix of the pseudo-observations  
    H = np.zeros(shape=(nSta*(nPara-1-g-1),nSta*nPara))    
    # sub-constrain matrix of H
    Hi = np.zeros(shape=(nPara-1-g-1,nPara-g-1)) 
    # sub-constrain matrix of W
    Wc = np.zeros(shape=(nSta*(nPara-1-g-1),nSta*(nPara-1-g-1)))
    # vector of residuals
    h = np.zeros(shape=(nSta*(nPara-1-g-1)))
    
    # sigma of delta VTEC
    std_deltaV = 30    
    
    # get those matrices
    for n in range(nSta):
        for i in range(Hi.shape[0]):
            Hi[i,i] = 1
            Hi[i, i+1] = -1            
        
        # VTECs
        H[n*(nPara-1-g-1):(n+1)*(nPara-1-g-1),n*nPara:(n+1)*nPara-g-1] = Hi
        Wc[n*(nPara-1-g-1):(n+1)*(nPara-1-g-1),n*(nPara-1-g-1):(n+1)*(nPara-1-g-1)] = np.diag([1/std_deltaV**2 for j in range(nPara-1-g-1)])
        h[n*(nPara-1-g-1):(n+1)*(nPara-1-g-1)] = -(x0[n*nPara:(n+1)*nPara-1-g-1] - x0[n*nPara+1:(n+1)*nPara-g-1])
    
      
    # delete the last column representing the instrumental offset of the last station as a constraint
    # delete the columns of the parameters / time windows with no observations
    H = np.delete(H, cindxe.astype(int), 1)
    
    # find the rows corresponding to the missing parameters
    sub_rows = [((i+1)//nPara)*(nPara-1-g-1)+(i+1)%nPara-1 for i in cindxe 
                if (i+1)%nPara != nPara-g-1 and (i+1)%nPara != nPara-2 and (i+1)%nPara != nPara-1 and (i+1)%nPara != 0] 
    rows = [i for i in sorted(set(sub_rows + list(np.array(sub_rows)-1))) if i != -1]
    
    # delete those rows 
    H = np.delete(H, rows, 0)
    h = np.delete(h, rows, 0)
    Wc = np.delete(Wc, rows, 0)
    Wc = np.delete(Wc, rows, 1)
        
    return H, h, Wc


# In[25]:


def obs_weights(elev, dtecstd, cs, stationXYZ, optimize_mf, eindx = [], W = []):
    
    if eindx:
        # delete the row and column of the observations flagged as an outlier
        W = np.delete(W,eindx, 0)
        W = np.delete(W,eindx, 1)
        
    else:
        # calculate the weight matrix from scratch if no observations flagged as an outliers
            
        # calculate the elevation-dependent weights of the observations
        # weight is proportional to elevation angle
        ew1 = np.sin(elev[:,0])
        ew2 = np.sin(elev[:,1])
        ew = ew1*ew2
    
        # calculate the weights based on the standard deviations of the dtec
        tw = 1/dtecstd**2
        sw = tw/max(tw)
        
        # calculate the final weights
        W = np.diag(sw*ew)
        
    return W


# In[ ]:





# In[26]:


def global_ionospheric_maps(nSta, nPara, h0, resolution, time_windows, stationLLA, v_doy, gims, ionex_path = 'Data/Ionex/'):
    
    # get VTEC per station from GIMs
    
    # get the epochs of the estimates
    epochs = int(h0) + time_windows
    
    # initialize some variables
    gims_vtec = np.zeros(shape=(time_windows.shape[0], nSta))
    
    try:
        # loop over the stations
        for j in range(nSta):
            # for every station, extract the time series of the VTEC for the corresponding days to VGOS/VLBI session
            vtec_series = {}
            i = 0
            for year, days in v_doy.items():
                for day in days: 
                    # get the directory to the GIMs file
                    directory = ionex_path + year + '/' + day
                    # get the TEC maps
                    tecmaps = get_tecmaps(ionex_local_path(directory))
                    # extract the maps
                    vtec_series[i] = [get_tec(t, stationLLA[j,0], stationLLA[j,1]) for t in tecmaps]
                    
                    # keep track of the number of files                   
                    i+=1
        
            # get the epochs of the maps
            g_epochs = list(np.arange(0,24+24/(len(vtec_series[0])-1),24/(len(vtec_series[0])-1)))+list(24+np.arange(0,24+24/(len(vtec_series[1])-1),24/(len(vtec_series[1])-1)))
            # stack the epochs and the 
            g_vtec = np.column_stack((g_epochs, vtec_series[0] + vtec_series[1]))
            # interpolate between the maps as often as needed; i.e. based on the resolution
            gims_vtec[:,j] = np.interp(epochs, g_vtec[:,0], g_vtec[:,1])
    
    except:
        gims = 0
        
    return gims, gims_vtec


# In[ ]:





# In[76]:


def save_results(param, session, gradient, madrigal, gims, v_output_path = 'Results/'):
    
    # extract the year 
    year = 2000 + int(session[0:2])
    path = v_output_path + str(year) + '/' + session + '/'
    # create the path if missing
    if not os.path.exists(path):
        os.makedirs(path)
        
    # open a text file   
    file_object = open(path + session +'.txt','w') # 'n' for new
    
    # write the header
    if madrigal and gims:
        file_object.write('station date vlbi/vgos_vtec v_vtec_sigma gims_vtec madr_vtec'+'\n')
    elif gims:
        file_object.write('station date vlbi/vgos_vtec v_vtec_sigma gims_vtec'+'\n')
    elif madrigal:
        file_object.write('station date vlbi/vgos_vtec v_vtec_sigma madr_vtec'+'\n')    
    else:
        file_object.write('station date vlbi/vgos_vtec v_vtec_sigma'+'\n')
        
    for station in param.keys():
        for item in param[station]['vtec'][:]:
            file_object.write(station + ' ' + str(item).replace("'", "").replace('[','').replace(']','').strip() +'\n')
    file_object.write('\n')
    
    if gradient:
        # two gradients: Gn and Gn
        # append the ionospheric gradients to the file
        file_object.write('station date Gn Gn_sigma Gs Gs_sigma'+'\n')
    else:
        # one gradient: Gns
        # append the ionospheric gradients to the file
        file_object.write('station date Gns Gns_sigma'+'\n')
        
    for station in param.keys():
        file_object.write(station + ' ' + str(param[station]['iono_grad'][:]).replace("'", "").replace('[','').replace(']','').strip() +'\n')
    file_object.write('\n')
    
    # append the instrumental offsets to the file
    file_object.write('station date instr_offset io_sigma'+'\n')
    for station in param.keys():
        file_object.write(station + ' ' + str(param[station]['instr_offset'][:]).replace("'", "").replace('[','').replace(']','').strip() +'\n')
            
    file_object.close()


# In[ ]:





# In[28]:


def extract_observations(freq, s2nr, meta_data, dtec, dtecstd, t, eindx = []):
    
    ## delete any observations flagged as an outliers
    if eindx:
        
        # the time tag and the integer hours
        t = np.delete(t,eindx,0) 
    
        # the dtec and their standard deviations
        dtec = np.delete(dtec,eindx,0)
        dtecstd = np.delete(dtecstd,eindx,0)
    
        # the frequency
        freq = np.delete(freq,eindx,0)
    
        # the signal to noise ratio
        s2nr = np.delete(s2nr, eindx,0)
    
        # the meta data
        meta_data = np.delete(meta_data,eindx,0)
    
    
    ## extract observations
    # extract the number of the station
    sta = np.zeros(shape = (len(meta_data[:,0,0]),2))
    sta[:,0] = [int(meta_data[i,0,0]) for i in range(len(meta_data[:,0,0]))]
    sta[:,1] = [int(meta_data[i,1,0]) for i in range(len(meta_data[:,1,0]))]

    # extract the elevation angle of the iono piercing points
    elev = meta_data[:,:,1] 
    
    # extract the latitude and longitude of the iono piercing points
    latIPP = meta_data[:,:,3]    
    lonIPP = meta_data[:,:,4] 
    
    # extract the latitude and longitude of the VGOS/VLBI stations
    latSta = meta_data[:,:,5]     
    lonSta = meta_data[:,:,6] 
        
    return freq, meta_data, sta, elev, latIPP, lonIPP, latSta, lonSta, dtec, dtecstd, t, s2nr


# In[228]:


def v_data(session, exSta = [], snr = 15, cutoffangle = 5, minObs = 5, 
           vgosDB_path = 'Data/vgosDB/', geomagnetic = 0, modip = 1, modip_grid = 1):
    
    if 'VG' in session:
        
        ### get the data    
        # extract the observations 
        year = 2000 + int(session[0:2])
        session_path = vgosDB_path + str(year) + '/' + session + '/'
        nSta, meta_data, stations, stationLLA, stationXYZ, sources = BsElAzIPPLLA(session, geomagnetic, 
                                                                                  modip, modip_grid, 
                                                                                  path = session_path) 
               
        # get the signal to noise ratio of the observations
        s2nr = nc.Dataset(session_path+'Observables/SNR_bX.nc')['SNR'][:].data
        
        # get the ionospheric delays  in TECU
        dtec, dtecstd = vgos_dTEC(path = session_path)
        
        # get the epoch of the observations
        h0, hrs, YMD = obs_epochs(path = session_path)
        
        # get the freq in MHz and convert it to GHz
        freq = nc.Dataset(session_path + 'Observables/RefFreq_bX.nc')['RefFreq'][:].data
        freq =  np.array([float(freq*1e-3) for i in range(len(hrs[:]))])                
        
        
        ### preprocess the data        
        # get the indices of the observations from sources that were scanned more than the minObs 
        sindx = []
        Obs2Source = meta_data[:,0,7]
        for i in set(Obs2Source):
            xindx = [j for j in range(len(Obs2Source)) if Obs2Source[j] == i]
            if len(xindx) > minObs:
                sindx = sindx + xindx        
        
        # get the observations with signal to noise ratio more than snr
        snrindx = [list(s2nr).index(s2nr[i]) for i in range(len(s2nr)) if s2nr[i] > snr]
    
        # get the indices of the observations with an elevation angle more than the cut off angle   
        caindx = [i for i in range(len(meta_data[:,0,1])) 
                          if np.rad2deg(meta_data[i,0,1]) > cutoffangle and np.rad2deg(meta_data[i,1,1]) > cutoffangle]
    
        # get the indices of observations with non-zero standard deviation
        # obs. w. zero sta. dev. are basically made with the twin telescopes, i.e., Onsala13SW and Onsala13NE, as a baseline
        nzindx = [i for i in range(len(dtecstd)) if dtecstd[i] != 0]
                
        # get the indices of the observations corresponding to the stations that are to be exiled
        inindx = include_stations(stations, meta_data, exSta)
        
        # find the common indices
        indx = np.intersect1d(sindx, np.intersect1d(np.intersect1d(snrindx, nzindx), np.intersect1d(caindx, inindx)))
        
        # extract the corresponding observations  
        meta_data, hrs = meta_data[indx,:,:], hrs[indx]
        dtec, dtecstd = dtec[indx], dtecstd[indx]
        freq = freq[indx]        
        s2nr = s2nr[indx]
      
        # extract the time tag and the integer hours
        t = hrs[:]
    
        # find the day of year (DOY) of VGOS/VLBI session to be used in GIMs  
        days = doy(YMD)
        v_doy = {}    
        # save the days to their corresponding years
        if int(days[1]) > int(days[0]):
            v_doy[str(year)] = days
        else:
            v_doy[str(year + 1)] = days[1]
            
        return h0, freq, nSta, stations, stationLLA, stationXYZ, meta_data, -dtec, dtecstd, t, v_doy, sources, s2nr
        
    elif 'XB' in session or 'XA' in session:
        
        ### get the data    
        # extract the observations 
        year = 2000 + int(session[0:2])
        session_path = vgosDB_path + str(year) + '/' + session + '/'
        nSta, meta_data, stations, stationLLA, stationXYZ, sources = BsElAzIPPLLA(session, geomagnetic, 
                                                                                  modip, modip_grid, 
                                                                                  path = session_path) 
        
        
        # get the signal to noise ratio of the observations
        s2nrX = nc.Dataset(session_path+'Observables/SNR_bX.nc')['SNR'][:].data
        s2nrS = nc.Dataset(session_path+'Observables/SNR_bS.nc')['SNR'][:].data
        
        # get the ionospheric delays in seconds
        dtec, dtecstd = vlbi_dTEC(path = session_path)        
        
        # get the epoch of the observations
        h0, hrs, YMD = obs_epochs(path = session_path)        
    
        # get the effective freq in MHz and then converted to GHz
        freq = nc.Dataset(session_path + 'ObsDerived/EffFreq_bX.nc')['FreqGroupIono'][:].data*1e-3
        #freq = np.array([8.59549 for i in freq])
        
        # get the reference freq of X-band and S-band in MHz and converted to GHz
        fs = nc.Dataset(session_path + 'Observables/RefFreq_bS.nc')['RefFreq'][:].data*1e-3
        fx = nc.Dataset(session_path + 'Observables/RefFreq_bX.nc')['RefFreq'][:].data*1e-3
        if len(fs) == 1:
            fs =  np.array([float(fs) for i in range(len(hrs[:]))])
            
        if len(fx) == 1:
            fx =  np.array([float(fx) for i in range(len(hrs[:]))])
        
        
        ### preprocess the data     
        # get the indices of the observations from sources that were scanned more than the minObs 
        sindx = []
        Obs2Source = meta_data[:,0,7]
        for i in set(Obs2Source):
            xindx = [j for j in range(len(Obs2Source)) if Obs2Source[j] == i]
            if len(xindx) > minObs:
                sindx = sindx + xindx
    
        # get the indices of the observatins with a signal to noise ration more than snr
        snrindxX = [list(s2nrX).index(s2nrX[i]) for i in range(len(s2nrX)) if s2nrX[i] > snr]
        snrindxS = [list(s2nrS).index(s2nrS[i]) for i in range(len(s2nrS)) if s2nrS[i] > snr]        
        snrindx = list(set(snrindxX + snrindxS)) 
    
        # get the indices of the observations with an elevation angle more than the cut off angle   
        caindx = [i for i in range(len(meta_data[:,0,1])) 
                          if np.rad2deg(meta_data[i,0,1]) > cutoffangle and np.rad2deg(meta_data[i,1,1]) > cutoffangle]
        
        # find the indices of non-zero frequences
        indxf = [i for i in range(len(fs)) if fs[i] != 0 and fx[i] !=0]
        
        # get the indices of observations with non-zero standard deviation
        # obs. w. zero sta. dev. are basically made with the twin telescopes, i.e., Onsala13SW and Onsala13NE, as a baseline
        nzindx = [i for i in range(len(dtecstd)) if dtecstd[i] != 0]
        
        # get the indices of the observations corresponding to the stations that are to be exiled
        inindx = include_stations(stations, meta_data, exSta)
        
        # find the common indices
        indx = np.intersect1d(np.intersect1d(sindx, snrindx), 
                              np.intersect1d(np.intersect1d(nzindx,caindx), np.intersect1d(indxf, inindx)))
        
        # extract the corresponding observations  
        meta_data, hrs = meta_data[indx,:,:], hrs[indx]
        dtec, dtecstd = dtec[indx], dtecstd[indx]
        freq = freq[indx] 
        fs, fx = fs[indx], fx[indx] 
        s2nr = np.column_stack((s2nrS,s2nrX))[indx,:]
        
        # convert the dtec from sec to TECU using eq.2 in SEKIDO
        f = (fs**2)*(fx**2)/(fx**2 - fs**2)
        dtec, dtecstd = dtec*(40.3*1e18)/f/299792458, dtecstd*(40.3*1e18)/f/299792458                
              
        # extract the time tag and the integer hours
        t = hrs[:]
    
        # find the day of year (DOY) of VGOS/VLBI session to be used in GIMs  
        days = doy(YMD)
        v_doy = {}    
        # save the days to their corresponding years
        if int(days[1]) > int(days[0]):
            v_doy[str(year)] = days
        else:
            v_doy[str(year + 1)] = days[1]
    
        return h0, freq, nSta, stations, stationLLA, stationXYZ, meta_data, dtec, dtecstd, t, v_doy, sources, s2nr
    
    else:
        raise Exception(session + ' does not end with XA, XB or VG. Please, provide the correct name of the session')
    


# In[ ]:





# In[30]:


def mapping_parameters(nSta, nPara, resolution, stations, stationLLA, rcindx, exSta, x, sx,
                       h0, time_windows, session, gradient, gims, madrigal, v_doy, ionex_path):
    
    # initialize some variables
    param = {station: {'vtec':[],'iono_grad':[],'instr_offset':[]}
             for i, station in enumerate(stations) if station not in exSta}    
        
    # get the time tag
    time_tag = []
    date_tag = []
    for i in int(h0) + time_windows: 
        # append the time tag to the list
        time_tag.append(str(datetime.timedelta(hours = i-24*math.floor(i/24))).rjust(2,'0'))
        # get the date of the next day
        nxtdate = datetime.date(2000+int(session[:2]),datetime.datetime.strptime(session[2:5], "%b").month,int(session[5:7])) + datetime.timedelta(days=math.floor(i/24))
        # append the date tag to the list
        date_tag.append(nxtdate.strftime("%Y")+'/'+nxtdate.strftime("%m").rjust(2,'0')+'/'+nxtdate.strftime("%d").rjust(2,'0'))
    
    # get the vtec values from GIMs
    if gims:
        gims, gims_vtec = global_ionospheric_maps(nSta, nPara, h0, resolution, time_windows, 
                                                  stationLLA, v_doy, gims, ionex_path)
    # get the VTECs from madrigal
    if madrigal:
        epochs = int(h0) + time_windows
        madrigal, madr = vtec_madrigal(session, stations, exSta, stationLLA, epochs[0], epochs[-1], madrigal) 
        
    # loop over the stations
    for i, station in enumerate(stations):            
        if station not in exSta:
            
            if gradient:
                # two gradients: Gn and Gs
                # initialize some variables
                vtec = np.empty(shape = (nPara-3,6)).astype(str)
                iono_grad = np.empty(shape = (5)).astype(str)
                instr_offset = np.empty(shape = (3)).astype(str)
                
                # get the date
                vtec[:,0] = date_tag
                iono_grad[0] = date_tag[0]
                instr_offset[0] = date_tag[0]
        
                # get the time tags
                vtec[:,1] = time_tag                 
                
                # get the VLBI/VGOS parameters
                vtec[:,2] = [str(np.round(item,3)) for item in x[i*nPara:(i+1)*nPara-3]]
                iono_grad[1] = str(np.round(x[(i+1)*nPara-3],3))
                iono_grad[3] = str(np.round(x[(i+1)*nPara-2],3))
                instr_offset[1] = str(np.round(x[(i+1)*nPara-1],3))
        
                # get their formal errors
                vtec[:,3] = [str(np.round(item,3)) for item in sx[i*nPara:(i+1)*nPara-3]]   
                iono_grad[2] = str(np.round(sx[(i+1)*nPara-3],3))
                iono_grad[4] = str(np.round(sx[(i+1)*nPara-2],3))
                instr_offset[2] = str(np.round(sx[(i+1)*nPara-1],3))
                
                # get VTECs from GIMs     
                if gims:
                    vtec[:,4] = [str(np.round(item,3)) for item in gims_vtec[:,i]] 
                else: 
                    vtec[:,4] = ''
                    
                # get VTECs from Madrigal
                if madrigal:
                    if madr[station].any():
                        vtec[:,5] = [str(np.round(item,3)) for item in np.interp(epochs, madr[station][:,0], madr[station][:,2])] 
                else: 
                    vtec[:,5] = ''
            
            else:
                # one gradient: Gns
                # initialize some variables
                vtec = np.empty(shape = (nPara-2,6)).astype(str)
                iono_grad = np.empty(shape = (3)).astype(str)
                instr_offset = np.empty(shape = (3)).astype(str)
                
                # get the date
                vtec[:,0] = date_tag
                iono_grad[0] = date_tag[0]
                instr_offset[0] = date_tag[0]
        
                # get the time tags
                vtec[:,1] = time_tag                 
                
                # get the VLBI/VGOS parameters
                vtec[:,2] = [str(np.round(item,3)) for item in x[i*nPara:(i+1)*nPara-2]]
                iono_grad[1] = str(np.round(x[(i+1)*nPara-2],3))
                instr_offset[1] = str(np.round(x[(i+1)*nPara-1],3))
        
                # get their formal errors
                vtec[:,3] = [str(np.round(item,3)) for item in sx[i*nPara:(i+1)*nPara-2]]   
                iono_grad[2] = str(np.round(sx[(i+1)*nPara-2],3))
                instr_offset[2] = str(np.round(sx[(i+1)*nPara-1],3))
            
                # get VTECs from GIMs     
                if gims:
                    vtec[:,4] = [str(np.round(item,3)) for item in gims_vtec[:,i]] 
                else: 
                    vtec[:,4] = ''
                    
                # get VTECs from Madrigal
                if madrigal:
                    if madr[station].any():
                        vtec[:,5] = [str(np.round(item,3)) for item in np.interp(epochs, madr[station][:,0], madr[station][:,2])] 
                else: 
                    vtec[:,5] = ''                    
                
            
            # get the indices of the time windows with observations
            indx = [j for j in range(rcindx.shape[0]) if rcindx[j,i] != 0]
            if rcindx[-1,i] != 0:
                indx = indx + [int(indx[-1])+1]
                
            # save the parameters in the dictionary
            param[station]['vtec'] = vtec[indx,:]
            param[station]['iono_grad'] = iono_grad
            param[station]['instr_offset'] = instr_offset                
                               
                            
    return param


# In[ ]:





# In[ ]:





# In[31]:


def nPara_time_window(t, gradient = 1, resolution = 60):
    
    startPoint = math.floor(min(t)) 
    endPoint = math.ceil(max(t))
    
    # or resolution == 30 or resolution == 60 or resolution == 120 or resolution == 180: 
    if 240 >= resolution >= 15:
        # eith Gn and Gs, or Gns
        if gradient:
            # two gradients: Gn and Gs
            # get the number of parameters per station
            # VTECs, Gn, Gs, and Instr
            nPara = (math.floor((endPoint - startPoint)*(60/resolution))+1)+1+1+1
        else:
            # one gradient: Gns
            # get the number of parameters per station
            # VTECs, Gns, and Instr
            nPara = (math.floor((endPoint - startPoint)*(60/resolution))+1)+1+1
            
        # generate the time windows
        indices = np.arange(int((endPoint - startPoint)*(60/resolution)+1))
        time_windows = indices*(resolution/60)
            
        return nPara, time_windows
        
    else:
        return print('Please, enter a resolution between 15 and 240 in min')
        # return print('Please, enter the correct resolution in min, i.e. 15, 30, or 60')


# In[32]:


def column_index(nSta, nPara, s1n, s2n, t, time_windows, rel_constraints, sum_instr_offsets, gradient):
    
    # handle the gradient
    if gradient:
        # two gradients: Gn and Gs
        g = 2
    else:
        # one gradient: Gns
        g = 1
        
    # extract the number of observation per time interval per station
    c1 = np.zeros(shape = (nPara-1-g-1,nSta)) # 1st station in the baseline
    c2 = np.zeros(shape = (nPara-1-g-1,nSta)) # 2nd station in the baseline
        
    for i, item in enumerate(s1n):
        indx = [w for w in range(len(time_windows)-1) if time_windows[w] <= t[i] <time_windows[w+1] ]
        c1[indx[0], int(item-1)] +=1
        
    for i, item in enumerate(s2n):
        indx = [w for w in range(len(time_windows)-1) if time_windows[w] <= t[i] <time_windows[w+1] ]
        c2[indx[0], int(item-1)] +=1
    
    # conacate the lists of the stations
    c = c1+c2
    
    # define the (remaining) indices of the time windows with observations
    rcindx = np.ones(shape = (c.shape[0],c.shape[1]))
        
    # number of parameters per station per hour
    nPs = 2 + g + 1
    # save the index of the parameters that don't have sufficient observations and are to be eliminated
    cindxe = []
    cindxr = [i for i in range(0,nSta*nPara)]
    for i in range(c.shape[1]):
        # if a station has no obs for the whole session, save the index of the instrumental delay and the gradients
        if (c[:,i] == 0).all():
            cindxe.append((i+1)*nPara-1)
            if gradient:
                # two gradients: Gn and Gs
                cindxe.append((i+1)*nPara-2)
                cindxe.append((i+1)*nPara-3)
            else:
                # one gradient: Gns
                cindxe.append((i+1)*nPara-2)
            
        # if a station has no obs for certain hours, save the index of the VTEC parameters
        for j in range(c.shape[0]):
            if c[j,i] == 0: # < nPs
                # stations, hours, parameter index in A matrix order
                cindxe.append(i*nPara+j)               
                # save the index of the station and the time window
                rcindx[j,i] = 0
                # deal with the last parameter in the series
                if j == len(c[:,i])-1:
                    cindxe.append(i*nPara+j+1)
    
    # change cindxe from list to np.array
    cindxe = np.array(cindxe)
    
    # save the indices of the parameters with no observations to be used in VCE
    rel_cindxe = np.array(sorted(set(list(cindxe) + [nSta*nPara-1])))
    
    # if relative constraints are applied,
    if rel_constraints:         
        indx = []
        # re-fill the gaps
        for i in range(rcindx.shape[1]):
            for j in range(rcindx.shape[0]):
                if rcindx[j,i] == 0:
                    # check whether the missing obs is bounded with obs
                    if (rcindx[0:j,i] == 1).any():
                        if (rcindx[j:rcindx.shape[0],i] == 1).any():
                            # if yes, change its value to 1
                            rcindx[j,i] = 1
                            
                            # save the index of the corresponding parameter                            
                            indx.append(list(cindxe).index(i*nPara+j))
                            
        # don't delete those parameters
        cindxe = np.delete(cindxe,indx, 0)
                            
    if not sum_instr_offsets:        
        # delete also the last column representing the instrumental offset of the last station as a constraint
        cindxe = np.array(sorted(set(list(cindxe) + [nSta*nPara-1])))
    
    # get the indices of the remaining parameters
    cindxr = np.delete(cindxr,cindxe.astype(int), 0)       
    
    return rel_cindxe, cindxe, cindxr, rcindx, c


# In[33]:


def vtec_madrigal(session, stations, exSta, stationLLA, startTime, endTime, madrigal = 0, path = 'Data/Madrigal/'):
    
    # create a dictionry for months
    m2n = {m:i+1 for i, m in enumerate(['JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN', 'JUL', 'AUG', 'SEP', 'OCT', 'NOV','DEC'])}
    
    # get the dates
    date1 = datetime.date(2000+int(session[:2]),m2n[session[2:5]],int(session[5:7])) 
    date2 = date1 + datetime.timedelta(days=1)       
    
    # get the names of files
    files = ['gps'+date1.strftime('%y')+date1.strftime('%m')+date1.strftime('%d'),
             'gps'+date2.strftime('%y')+date2.strftime('%m')+date2.strftime('%d')]
    
    # create a dict for madrigal VTECs per station
    madr = {station:np.array([]) for station in stations}
    try:
        for station in stations:
            if station not in exSta:
                # initiate some variables
                ymadr, xmadr = [], []
                count = 0
        
                # get Madrigal VTECs if exists
                for file in files:
        
                    if os.path.isfile(path + file + 'g.001.nc'):
                        file = file + 'g.001.nc'                  
                    elif os.path.isfile(path + file + 'g.002.nc'):
                        file = file + 'g.002.nc'
                    else:
                        raise Exception('file could not be found in the given directory')
            
                    ds = nc.Dataset(path + file)
                    
                    # get the latitude and longitude indices of the station 
                    # 1x1 degree in lat x lon - grid resolution
                    latIndx, lonIndx = -1, -1                    
                    diff = abs(ds['gdlat'][:].data - stationLLA[stations.index(station),0])
                    if (diff  <= 1).any: # lat
                        latIndx = list(diff).index(min(diff))
                    
                    diff = abs(ds['glon'][:].data - stationLLA[stations.index(station),1])
                    if (diff  <= 1).any(): # lon
                        lonIndx = list(diff).index(min(diff))
                    
                    # if a nearby bin was found, extract its value.
                    if latIndx >= 0 and lonIndx >= 0:
                        for i, item in enumerate(ds['tec'][:, latIndx, lonIndx]):
                            if not np.isnan(item):
                                ymadr.append(item)
                                xmadr.append(i*5/60+24*count) # convert the epoch index into hours, 5 min resolution
                
                        count +=1         
        
                # if there is data, extract the values corresponding to VLBI/VGOS
                if ymadr:
        
                    # get the index of the starting point
                    for j, item in enumerate(xmadr):
                        if item >= startTime:
                            sindx = j                
                            break
                        else:
                            sindx = j
    
                    # get the index of the ending point
                    for j, item in enumerate(xmadr):           
                        if item >= endTime:
                            eindx = j-1
                            break
                        else:
                            eindx = j-1
    
                    # get the window length of savgol filter
                    if int(len(ymadr)/8)%2:
                        window_length = int(len(ymadr)/8)
                    else:
                        window_length = int(len(ymadr)/8)+1
    
                    # get the poly order
                    if window_length <= 5:
                        ployorder = window_length - 1
                    else:
                        ployorder = 5
    
                    # smooth the x data and get only the data corresponding to the given 
                    ysmth = signal.savgol_filter(ymadr,window_length,ployorder)
            
                    # stack the epochs, the original VTECs and the smoothed VTECs
                    madr[station] = np.column_stack((xmadr[sindx:eindx], ymadr[sindx:eindx], ysmth[sindx:eindx]))
            
    except:
        madrigal = 0
        
    return madrigal, madr


# In[ ]:





# In[34]:


def v_gims_madr_bias(param): 
    
    # get the stations
    stations = list(param.keys())
    
    # define the dict for VLBI/VGOS bias w.r.t. GIMs and Madr
    v_bias = {'gims':{'rms':{}, 'mean':{}}, 'madrigal':{'rms':{}, 'mean':{}}}
    
    # get the bias per station
    for i, station in enumerate(stations):
        # get the b
        if param[station]['vtec'][0,4]:
            diff1 = abs(param[station]['vtec'][:,4].astype(float) - param[station]['vtec'][:,2].astype(float))
            v_bias['gims']['rms'][station] = round(np.sqrt(np.mean(diff1**2)),3)
            v_bias['gims']['mean'][station] = round(np.mean(diff1),3)
        
        if param[station]['vtec'][0,5]:
            diff = abs(param[station]['vtec'][:,5].astype(float) - param[station]['vtec'][:,2].astype(float))
            v_bias['madrigal']['rms'][station] = round(np.sqrt(np.mean(diff**2)),3)
            v_bias['madrigal']['mean'][station] = round(np.mean(diff),3)
         
    return v_bias


# In[ ]:





# In[256]:


def v_plot(session, resolution, stations, stationLLA, startTime, endTime, 
           param, gims, madrigal, exSta, error_bar, v_output_path = 'Results/'):
          
    # create a figure    
    # get_ipython().run_line_magic('matplotlib', 'notebook')
    plt.rcParams["figure.figsize"] = (10,4)
    matplotlib.use('Agg')
    
    # get the label for the results
    if 'VG' in session:
        vlabel = 'VGOS'
    else: # 'XA' or 'XB' in session:
        vlabel = 'VLBI'
    
    # get the VTECs from Madrigal
    if madrigal:
        madrigal, madr = vtec_madrigal(session, stations, exSta, stationLLA, startTime, endTime, madrigal)
        
    # get the biases
    v_bias = v_gims_madr_bias(param)
        
    # create a dictionry for months
    m2n = {m:i+1 for i, m in enumerate(['JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN', 'JUL', 'AUG', 'SEP', 'OCT', 'NOV','DEC'])}
    
    # loop over the stations
    for station in stations:
        # exclude the problematic stations
        if station not in exSta: #in 'WETTZ13S':#
            
            # get the observation epochs
            epochs = []
            # get the indices
            indx = []
            for i, item in enumerate(param[station]['vtec']):                 
                
                # get the observation date and the session date                
                d = item[0].split('/')
                obsDate = datetime.date(int(d[0]), int(d[1].rjust(2,'0')), int(d[2]))
                sessionDate = datetime.date(2000+int(session[:2]),m2n[session[2:5]],int(session[5:7]))
                
                # get the observation epoch
                ep = item[1].split(':')
                epoch = float(ep[0])+float(ep[1])/60+float(ep[2])/60**2  + 24*(obsDate - sessionDate).days  
                                
                if i:
                    # check whether there is a jump in the observation epochs and whether this is the last epoch
                    if (epoch - epoch0) != resolution/60 or i == len(param[station]['vtec'][:,0]) - 1:                         
                        
                        # append the index to the list of indices & the epoch to the list of epochs if it's the last epoch
                        if  i == len(param[station]['vtec'][:,0]) - 1:
                            indx.append(i)
                            epochs.append(epoch)
                                                    
                        # plot the VTECs from VLBI/VGOS
                        if error_bar:
                            plt.errorbar(epochs, param[station]['vtec'][indx,2].astype(float), 
                                         yerr = param[station]['vtec'][indx,3].astype(float), capsize=1, elinewidth=0.5,
                                         markeredgewidth=2, ls='-', color = 'g', barsabove=True, label = vlabel) # , fmt='o'  + ' NE'
#                             plt.errorbar(epochs, param['ONSA13SW']['vtec'][indx,2].astype(float), 
#                                          yerr = param['ONSA13SW']['vtec'][indx,3].astype(float), capsize=1, elinewidth=0.5,
#                                          markeredgewidth=2, ls='-', color = 'sienna', alpha=0.8, barsabove=True, label = vlabel + ' SW') # , fmt='o'
                        else:
                            plt.plot(epochs, param[station]['vtec'][indx,2].astype(float), '-g', label = vlabel)
                        
                        # plot the VTECs from GIMs
                        if gims:
                            if param[station]['vtec'][indx,4][0]:
                                plt.plot(epochs, param[station]['vtec'][indx,4].astype(float), '.--b', alpha=0.8, label = 'GIMs')
                        
                        # plot the VTECs from Madrigal if any
                        if madrigal:
                            if madr[station].any():
                                # get the index of the starting point
                                for k, m in enumerate(madr[station][:,0]):
                                    if m >= epochs[0]:
                                        sindx = k    
                                        break
                                    else:
                                        sindx = k
    
                                # get the index of the ending point
                                for k, m in enumerate(madr[station][:,0]):           
                                    if m >= epochs[-1]:
                                        eindx = k-1
                                        break
                                    else:
                                        eindx = k-1
                            
                                # plot the original and smoothed Madrigal VTECs
                                plt.plot(madr[station][sindx:eindx,0], madr[station][sindx:eindx,1], c='0.8', ls='dotted', label = 'MTMs')
                                plt.plot(madr[station][sindx:eindx,0], madr[station][sindx:eindx,2], '-y', label = 'SMTMs')
                                                        
                        # reset the epochs and indices
                        indx = []
                        epochs = []
                
                # append  the index to the list of indices and the epoch to the list of epochs
                indx.append(i)
                epochs.append(epoch) 
                
                # save the epoch
                epoch0 = epoch                      
            
#             # write down the rms w.r.t. GIMs and SMTMs
#             ax = plt.gca()
#             if gims: #17.3 32.5
#                 ax.text(17.3, 5.5, 'RMS w.r.t. GIMs    = ' + str(round(v_bias['gims']['rms'][station],1)).rjust(3,'0'), 
#                         color="b", ha = 'left', va="bottom") 
                
#             if madrigal:
# #                 if param[station]['vtec'][0,5]:
# #                     diff = abs(param[station]['vtec'][:,5].astype(float) - param[station]['vtec'][:,2].astype(float))
# #                     v_bias['madrigal']['rms'][station] = round(np.sqrt(np.mean(diff**2)),3)
# #                     v_bias['madrigal']['mean'][station] = round(np.mean(diff),3)
#                     #37.2
#                 ax.text(17.3, 4.6, 'RMS w.r.t. SMTMs = ' + str(round(v_bias['madrigal']['rms'][station],1)).rjust(3,'0'), 
#                         color="y", ha = 'left', va="bottom") 
            
            # add a title and some labels
            plt.title(station + ' on ' + session)
            plt.xlabel('UTC hour')
            plt.ylabel('VTEC (TECU)')
            #plt.xlim(left = startTime-1, right = endTime+1) #left = h0-1, right = h0+26
            plt.ylim()
            plt.legend() # , bbox_to_anchor=(0.225,1)
            
            # set the labels of the x-axis
            locs, old_labels = plt.xticks()
            labels = [str(i-24*(i//24)) for i in locs]
            plt.xticks(locs, labels)  
            plt.xlim(left = startTime-1, right = endTime+1) #left = h0-1, right = h0+26
                       
            # create the following path if it doesn't exist
            path = v_output_path + str(2000+int(session[:2])) + '/' + session + '/' #  'VTEC Time Series/' #
            if not os.path.exists(path):
                os.makedirs(path)
                
            # save the plot
            plt.savefig(path + station + ' on ' + session + '.jpg')
    
            # close all the figures
            plt.close('all')
            


# In[36]:


def v_read_file(session, v_output_path = 'Results/'):
    
    # get VLBI/VGOS-derived VTEC
    file = open(v_output_path + str(2000+int(session[:2])) + '/' + session + '/' 
                + session + '.txt', 'r').read().split('station')
    
    # get the stations
    stations = list(sorted(set([line.split()[0] for line in file[1].split('\n')[1:-2]])))
    
    # create a dictionary for different types of data in the text file
    param = {station: {'vtec': [], 'iono_grad':[], 'instr_offset': []} for station in stations}
    
    # keep track of lines per station
    l2s_list = []
    for line in file[1].split('\n')[1:-2]:
        items = line.split()
        if items[0] in l2s_list:
            param[items[0]]['vtec'] = np.row_stack((param[items[0]]['vtec'],items[1:])).astype('str')
        else:
            param[items[0]]['vtec'] = items[1:]
        l2s_list = list(set(l2s_list + [items[0]]))
        
    # keep track of lines per station
    l2s_list = []
    for line in file[2].split('\n')[1:-2]:
        items = line.split()
        if items[0] in l2s_list:
            param[items[0]]['iono_grad'] = np.row_stack((param[items[0]]['iono_grad'],items[1:])).astype('str')
        else:
            param[items[0]]['iono_grad'] = items[1:]
        l2s_list = list(set(l2s_list + [items[0]]))
        
    # keep track of lines per station
    l2s_list = []
    for line in file[3].split('\n')[1:-1]:
        items = line.split()
        if items[0] in l2s_list:
            param[items[0]]['instr_offset'] = np.row_stack((param[items[0]]['instr_offset'],items[1:])).astype('str')
        else:
            param[items[0]]['instr_offset'] = items[1:]
        l2s_list = list(set(l2s_list + [items[0]]))
    
    return param


# In[36]:




# In[ ]:



# plot_analysis_results(param, v_output_path = 'Results_own_modip_grid/')


# In[343]:


def plot_analysis_results(param, v_output_path = 'Results/', ylim_bias = 10, ylim_instr = 10, ylim_grad = 10):
    
    ###
    # get the summary of all the sessions
    vgos_stations, vlbi_stations, svgkey, svlkey, vgos_sPs, vlbi_sPs = summarise_sessions(param)
    
    
    ### plot the summary
    
    # create a figure  
    # get_ipython().run_line_magic('matplotlib', 'notebook')
    plt.rcParams["figure.figsize"] = (10,4)
    matplotlib.use('Agg')
    
    # get the dates of the first and last sesssions
    keys = sorted(svgkey.keys())
    sDate = datetime.datetime.strptime(str(keys[0][0])+str(keys[0][1])+str(keys[0][2]),"%y%m%d").date() 
    eDate = datetime.datetime.strptime(str(keys[-1][0])+str(keys[-1][1])+str(keys[-1][2]),"%y%m%d").date()
    
    # plot the biases per station
    for indx, station in enumerate(vgos_stations):       
            
        # get the dates to be plotted on the x-axis
        x = [datetime.datetime.strptime(str(key[0])+ '/'+str(key[1])+'/'+str(key[2]),"%y/%m/%d").date() 
             for i, key in enumerate(sorted(svgkey.keys())) if indx in vgos_sPs[svgkey[key]].keys()]
         
        # get the biases to be plotted on the y-axis
        yGIMs =  [float(vgos_sPs[svgkey[key]][indx]['gims']) 
               for i, key in enumerate(sorted(svgkey.keys())) if indx in vgos_sPs[svgkey[key]].keys()]
        
        yMadr =  [float(vgos_sPs[svgkey[key]][indx]['madrigal']) 
               for i, key in enumerate(sorted(svgkey.keys())) if indx in vgos_sPs[svgkey[key]].keys()]
    
        # plot the biases as bars
        plt.bar(x, yGIMs, width=10, color='purple', align='center', label = 'RMS w.r.t. GIMs')
        plt.bar(x, yMadr, width=10, color='y', align='center', alpha = 0.8, label = 'RMS w.r.t. SMTMs')
         
        # add a title and some labels
        plt.title(station)
        plt.xlabel('Session Date')
        plt.ylabel('RMS (TECU)')
        plt.xlim(sDate - datetime.timedelta(days=15), eDate + datetime.timedelta(days=15)) # adjust the dates dynamically
        plt.ylim(0,ylim_bias)
    
        # get the axises of the current figure and adjust the format of its x-axis labels
        ax = plt.gca()
        date_form = matplotlib.dates.DateFormatter("%Y-%m-%d")
        ax.xaxis.set_major_formatter(date_form)
        ax.xaxis.set_major_locator(matplotlib.dates.MonthLocator(interval=2))
    
        # draw the mean of the biases as a horizontal line
#         ax.axhline(np.mean(yGIMs), color='purple', linewidth=1, alpha = 0.6)
#         ax.axhline(np.mean(yMadr), color='y', linewidth=1, alpha = 0.6)

        
#         xPos =  sDate + datetime.timedelta(days=(eDate - sDate).days/8) # datetime.date(2018,3,1) # 
#         ax.text(xPos, np.mean(yGIMs), 'mean = ' + str(round(np.mean(yGIMs),2)).rjust(3,'0') +' $\pm$ '+ 
#                 str(round(np.std(yGIMs),2)).rjust(3,'0'), color="purple", va="bottom") 
#         ax.text(xPos, np.mean(yMadr), 'mean = ' + str(round(np.mean(yMadr),2)).rjust(3,'0') + ' $\pm$ '+
#                 str(round(np.std(yMadr),2)).rjust(3,'0'), color="y", va="top")

        # draw the median of the biases as a horizontal line and write the value on top of it
        ax.axhline(np.median(yGIMs), color='purple', linewidth=1, alpha = 0.6)
        ax.axhline(np.median(yMadr), color='y', linewidth=1, alpha = 0.6)

        
        xPos = datetime.date(2018,3,1) # sDate + datetime.timedelta(days=(eDate - sDate).days/8) #
        ax.text(xPos, np.median(yGIMs), 'median = ' + str(round(np.median(yGIMs),2)).rjust(3,'0') + 
                ' $\pm$ '+ str(round(scipy.stats.median_abs_deviation(yGIMs),2)).rjust(3,'0'), color="purple", va="bottom")
        ax.text(xPos, np.median(yMadr), 'median = ' + str(round(np.median(yMadr),2)).rjust(3,'0') + 
                ' $\pm$ '+ str(round(scipy.stats.median_abs_deviation(yMadr),2)).rjust(3,'0'), color="y", va="top")
            
        # display the exact value of the bars that exceed the limits on the y-axis  
        for i, v in enumerate(yGIMs):
            if v > ylim_bias:# and i == len(yGIMs)-1:                
                ax.text(x[i]- datetime.timedelta(days=5),v/2.2, str(v).rjust(3,'0'), color='purple', ha='right', rotation='vertical', fontsize=10)
        
        for i, v in enumerate(yMadr):
            if v > ylim_bias:# and i == len(yGIMs)-1:
                ax.text(x[i]- datetime.timedelta(days=5),v/3.35, str(v).rjust(3,'0'), color='y', ha='right', rotation='vertical', fontsize=10)
                ax.text(x[i]- datetime.timedelta(days=2),v/2.5, ' and ', color='k', ha='right', rotation='vertical', fontsize=10)
                
        # make a legend for both plots
        leg = plt.legend(loc='upper left', bbox_to_anchor=(0.07,1))
    
        # get the current figure and automatically adjust the labels
        fig = plt.gcf()
        fig.autofmt_xdate()
    
        # rotate the labels
        plt.xticks(rotation=45)
         
        # create the output path if it doesn't exist
        path = v_output_path + 'Inter-technique Baises/'
        if not os.path.exists(path):
            os.makedirs(path)
        
        # save the figure
        plt.savefig(path + station + '.jpg', bbox_inches='tight')
        
        # close the figure
        plt.close('all')
        
        
    # plot instrumental offsets per station for all sessions
    for indx, station in enumerate(vgos_stations):
        
        # get the dates to be plotted on the x-axis
        x = [datetime.datetime.strptime(str(key[0])+ '/'+str(key[1])+'/'+str(key[2]),"%y/%m/%d").date() 
             for i, key in enumerate(sorted(svgkey.keys())) if indx in vgos_sPs[svgkey[key]].keys()]#if vgos_sPs[svgkey[key]][indx][2]]
    
        # get the offsets and their errors to be plotted on the y-axis
        y =  [float(vgos_sPs[svgkey[key]][indx]['instr_offset'][0]) 
              for i, key in enumerate(sorted(svgkey.keys())) if indx in vgos_sPs[svgkey[key]].keys()]#if vgos_sPs[svgkey[key]][indx][2]]
        
        yerror =  [float(vgos_sPs[svgkey[key]][indx]['instr_offset'][1]) 
                   for i, key in enumerate(sorted(svgkey.keys())) if indx in vgos_sPs[svgkey[key]].keys()]#if vgos_sPs[svgkey[key]][indx][2]]
    
        # plot the offsets as bars with errorbars
        plt.bar(x, y, yerr=yerror, width=10, color='purple', align='center', label = 'Instrumental Offsets')
            
        # add a title and some labels
        plt.title(station)
        plt.xlabel('Session Date')
        plt.ylabel('Instr. Offsets (TECU)')
        plt.xlim(sDate - datetime.timedelta(days=15), eDate + datetime.timedelta(days=15))
        plt.ylim(-ylim_instr,ylim_instr)
                    
        # get the axises of the current figure and adjust the format of its x-axis labels
        ax = plt.gca()
        date_form = matplotlib.dates.DateFormatter("%Y-%m-%d")
        ax.xaxis.set_major_formatter(date_form)
        ax.xaxis.set_major_locator(matplotlib.dates.MonthLocator(interval=2))
        
        # xPos =  sDate + datetime.timedelta(days=(eDate - sDate).days/4) # datetime.date(2018,3,1) # 
        # ax.text(xPos, np.mean(y), 'mean = ' + str(round(np.mean(y),2)).rjust(3,'0') +' $\pm$ '+ str(round(np.std(y),2)).rjust(3,'0'), color="k", va="bottom") 
        
        # disply the exact value of the bar
        for i, v in enumerate(y):
            if v > ylim_instr or v < -ylim_instr and i == 2:
                ax.text(x[i]-datetime.timedelta(days=5),v/4, str(v).rjust(3,'0'), color='k', ha='right', rotation='vertical', fontsize=10)
        
        
#         for i, v in enumerate(y):
#             if v > ylim_instr or v < -ylim_instr:
#                 if i == 0:
#                     ax.text(x[i]-datetime.timedelta(days=25),v/5, str(v).rjust(2,'0'), color='k', ha='left', rotation='vertical', fontsize=10)
#                 elif i == 1:
#                     ax.text(x[i]+datetime.timedelta(days=30),v/5, str(v).rjust(2,'0'), color='k', ha='right', rotation='vertical', fontsize=10)
 
        
        # make a legend for both plots
        leg = plt.legend()
        
        # get the current figure and automatically adjust the labels
        fig = plt.gcf()
        fig.autofmt_xdate()
    
        # rotate the labels
        plt.xticks(rotation=45)
         
        # create the output path if it doesn't exist
        path = v_output_path + 'Instrumental Offsets/'
        if not os.path.exists(path):
            os.makedirs(path)
        
        # save the figure
        plt.savefig(path + station + '.jpg', bbox_inches='tight')
        
        # close the figure
        plt.close('all')
        
        
    # plot the gradients per station
    for indx, station in enumerate(vgos_stations):       
            
        # get the dates to be plotted on the x-axis
        x = [datetime.datetime.strptime(str(key[0])+ '/'+str(key[1])+'/'+str(key[2]),"%y/%m/%d").date() 
             for i, key in enumerate(sorted(svgkey.keys())) if indx in vgos_sPs[svgkey[key]].keys()]
         
        # get the gradients to be plotted on the y-axis
        Gn =  [float(vgos_sPs[svgkey[key]][indx]['iono_grad'][0]) 
               for i, key in enumerate(sorted(svgkey.keys())) if indx in vgos_sPs[svgkey[key]].keys()]
        
        Gs =  [float(vgos_sPs[svgkey[key]][indx]['iono_grad'][2]) 
               for i, key in enumerate(sorted(svgkey.keys())) if indx in vgos_sPs[svgkey[key]].keys()]
    
        # plot the biases as bars
        plt.bar(x, Gn, width=10, color='purple', align='center', label = 'north gradient')
        plt.bar(x, Gs, width=10, color='y', align='center', alpha = 0.8, label = 'south gradient')
         
        # add a title and some labels
        plt.title(station)
        plt.xlabel('Session Date')
        plt.ylabel('Gradient')
        plt.xlim(sDate - datetime.timedelta(days=15), eDate + datetime.timedelta(days=15)) # adjust the dates dynamically
        plt.ylim(-ylim_grad,ylim_grad)
    
        # get the axises of the current figure and adjust the format of its x-axis labels
        ax = plt.gca()
        date_form = matplotlib.dates.DateFormatter("%Y-%m-%d")
        ax.xaxis.set_major_formatter(date_form)
        ax.xaxis.set_major_locator(matplotlib.dates.MonthLocator(interval=2))
    
        # draw the mean of the biases as a horizontal line
#         ax.axhline(np.mean(yGIMs), color='purple', linewidth=1, alpha = 0.6)
#         ax.axhline(np.mean(yMadr), color='y', linewidth=1, alpha = 0.6)

        
#         xPos =  sDate + datetime.timedelta(days=(eDate - sDate).days/8) # datetime.date(2018,3,1) # 
#         ax.text(xPos, np.mean(yGIMs), 'mean = ' + str(round(np.mean(yGIMs),2)).rjust(3,'0') +' $\pm$ '+ 
#                 str(round(np.std(yGIMs),2)).rjust(3,'0'), color="purple", va="bottom") 
#         ax.text(xPos, np.mean(yMadr), 'mean = ' + str(round(np.mean(yMadr),2)).rjust(3,'0') + ' $\pm$ '+
#                 str(round(np.std(yMadr),2)).rjust(3,'0'), color="y", va="top")

#         # draw the median of the biases as a horizontal line and write the value on top of it
#         ax.axhline(np.median(yGIMs), color='purple', linewidth=1, alpha = 0.6)
#         ax.axhline(np.median(yMadr), color='y', linewidth=1, alpha = 0.6)

        
#         xPos = datetime.date(2018,3,1) # sDate + datetime.timedelta(days=(eDate - sDate).days/8) #
#         ax.text(xPos, np.median(yGIMs), 'median = ' + str(round(np.median(yGIMs),2)).rjust(3,'0') + 
#                 ' $\pm$ '+ str(round(scipy.stats.median_abs_deviation(yGIMs),2)).rjust(3,'0'), color="purple", va="bottom")
#         ax.text(xPos, np.median(yMadr), 'median = ' + str(round(np.median(yMadr),2)).rjust(3,'0') + 
#                 ' $\pm$ '+ str(round(scipy.stats.median_abs_deviation(yMadr),2)).rjust(3,'0'), color="y", va="top")
            
        # display the exact value of the bars that exceed the limits on the y-axis  
        for i, v in enumerate(Gn):
            if v > ylim_grad and x[i] > x[0] + datetime.timedelta(days=900):# and i == len(yGIMs)-1:  +datetime.timedelta(days=11)              
                ax.text(x[i],  1, str(v).rjust(3,'0'), color='purple', ha='center', rotation='vertical', fontsize=9)
            if v < -ylim_grad:# and i == len(yGIMs)-1:                
                ax.text(x[i], -8.5, str(v).rjust(3,'0'), color='purple', ha='center', rotation='vertical', fontsize=9)
                
        for i, v in enumerate(Gs):
            if v > ylim_grad and i == 11:
                ax.text(x[i],  6, str(v).rjust(3,'0'), color='k', ha='center', rotation='vertical', fontsize=9)
            if v > ylim_grad and x[i] > x[0] + datetime.timedelta(days=900)  :# and i == len(yGIMs)-1:
                ax.text(x[i],  6, str(v).rjust(3,'0'), color='k', ha='center', rotation='vertical', fontsize=9)
            if  v < -ylim_grad:# and i == len(yGIMs)-1:
                ax.text(x[i], -8.5, str(v).rjust(3,'0'), color='k', ha='center', rotation='vertical', fontsize=9)
                    
        # make a legend for both plots
        leg = plt.legend(loc='upper left', bbox_to_anchor=(0.07,1))
    
        # get the current figure and automatically adjust the labels
        fig = plt.gcf()
        fig.autofmt_xdate()
    
        # rotate the labels
        plt.xticks(rotation=45)
         
        # create the output path if it doesn't exist
        path = v_output_path + 'Gradients/'
        if not os.path.exists(path):
            os.makedirs(path)
        
        # save the figure
        plt.savefig(path + station + '.jpg', bbox_inches='tight')
        
        # close the figure
        plt.close('all')
        
        
        
        
#     # double check whether you want the uncertainties to be plotted
#     # create a variable for the uncertainties
#     unc = {}
    
#     # plot vtec mean uncertainties per station
#     for indx, station in enumerate(vgos_stations):
        
#         # get the dates to be plotted on the x-axis
#         x = [datetime.datetime.strptime(str(key[0])+'/'+str(key[1])+'/'+str(key[2]),"%y/%m/%d").date() 
#              for i, key in enumerate(sorted(svgkey.keys())) if indx in vgos_sPs[svgkey[key]].keys()]#[indx]]
    
#         # get the mean uncertainties to be plotted on the y-axis
#         y =  [np.mean(vgos_sPs[svgkey[key]][indx]['vtec_std'].astype(float)) 
#               for i, key in enumerate(sorted(svgkey.keys())) if indx in vgos_sPs[svgkey[key]].keys()]#[indx][indx][0]]
        
#         # save the mean uncertainty per station
#         unc[station] = y
        
#         # get the standard deviation of the mean uncertainties for the y-axis
#         yerror =  [np.std(vgos_sPs[svgkey[key]][indx]['vtec_std'].astype(float))
#                    for i, key in enumerate(sorted(svgkey.keys())) if indx in vgos_sPs[svgkey[key]].keys()]#[indx][indx][0]]
        
#         # plot the biases as bars
#         plt.bar(x, y, yerr=yerror, width=10, color='purple', align='center', label = 'uncertainty')
            
#         # add a title and some labels
#         plt.title(station)
#         plt.xlabel('Session Date')
#         plt.ylabel('RMS (TECU)')
#         plt.xlim(sDate - datetime.timedelta(days=15), eDate + datetime.timedelta(days=15)) # adjust the dates dynamically
#         plt.ylim(0,0.5) # 0,10 # make this dynamic
    
#         # get the axises of the current figure and adjust the format of its x-axis labels
#         ax = plt.gca()
#         date_form = matplotlib.dates.DateFormatter("%Y-%m-%d")
#         ax.xaxis.set_major_formatter(date_form)
#         ax.xaxis.set_major_locator(matplotlib.dates.MonthLocator(interval=2))
    
#         # draw the mean of the biases as a horizontal line
#         ax.axhline(np.mean(y), color='y', linewidth=1, alpha = 0.6)
        
#         xPos =  sDate + datetime.timedelta(days=(eDate - sDate).days/4) # datetime.date(2018,3,1) # 
#         ax.text(xPos, np.mean(y), 'mean = ' + str(round(np.mean(y),2)).rjust(3,'0') +' $\pm$ '+ str(round(np.std(y),2)).rjust(3,'0'), color="k", va="bottom") 
            
# #         # display the exact value of the bar    
# #         for i, v in enumerate(yGIMs):
# #             if v > 10 or v < -10 and i == len(yGIMs)-1:
# #                 ax.text(x[i],v/2.5, str(v).rjust(3,'0'), color='k', ha='right', rotation='vertical', fontsize=10)
                
#         # make a legend for both plots
#         leg = plt.legend()
    
#         # get the current figure and automatically adjust the labels
#         fig = plt.gcf()
#         fig.autofmt_xdate()
    
#         # rotate the labels
#         plt.xticks(rotation=45)
         
#         # create the output path if it doesn't exist
#         path = v_output_path + 'v_VTECs_uncertainties/'
#         if not os.path.exists(path):
#             os.makedirs(path)
        
#         # save the figure
#         plt.savefig(path + station + '.jpg', bbox_inches='tight')
        
#         # close the figure
#         plt.close('all')
        
#     return unc


# In[309]:


def summarise_sessions(param):
    
    # print and plot the VLBI/VGOS biases w.r.t GIMs and Madr, VLBI/VGOS instrumental offsets, and VLBI/VGOS uncertainty
    
    # get VGOS bias w.r.t. GIMs and Madrigal TEC maps per session               
    v_bias = {}
    for session in param.keys():
        v_bias[session] = v_gims_madr_bias(param[session])
    
    # get all VLBI/VGOS stations in these sessions
    vgos_stations = []
    vlbi_stations = []
    for session in list(v_bias.keys()):
        if 'VG' in session:
            vgos_stations = list(sorted(set(vgos_stations+list(v_bias[session]['gims']['rms'].keys()))))
        elif 'XA' or 'XB' in session:
            vlbi_stations = list(sorted(set(vlbi_stations+list(v_bias[session]['gims']['rms'].keys()))))
    
    # get the session information per station
    vgos_sPs = {}
    vlbi_sPs = {}
    for session in list(v_bias.keys()):
        if 'VG' in session:
            vgos_sPs[session] = {}
            for i, station in enumerate(v_bias[session]['gims']['rms']):
                indx = vgos_stations.index(station)
                vgos_sPs[session][indx] = {'gims':str(round(float(v_bias[session]['gims']['rms'][station]),3)), 
                                           'madrigal':str(round(float(v_bias[session]['madrigal']['rms'][station]),3)), 
                                           'instr_offset':param[session][station]['instr_offset'][1:3], 
                                           'iono_grad':param[session][station]['iono_grad'][1:],
                                           'vtec_std':param[session][station]['vtec'][:,3]}
        elif 'XA' or 'XB' in session:
            vlbi_sPs[session] = {} 
            for i, station in enumerate(v_bias[session]['gims']['rms']):
                indx = vlbi_stations.index(station)
                vlbi_sPs[session][indx] = {'gims':str(round(float(v_bias[session]['gims']['rms'][station]),3)), 
                                           'madrigal':str(round(float(v_bias[session]['madrigal']['rms'][station]),3)), 
                                           'instr_offset':param[session][station]['instr_offset'][1:3],
                                           'iono_grad':param[session][station]['iono_grad'][1:],
                                           'vtec_std':param[session][station]['vtec'][:,3]}
    
    
    # create a dict to convert months' names to numbers
    m2n = {m:i+1 for i, m in enumerate(['JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN', 'JUL', 'AUG', 'SEP', 'OCT', 'NOV', 'DEC'])}
    
    # create a dict to sort the sessions by date
    svgkey = {}
    for key in vgos_sPs.keys(): 
        # tuple: year, month, day
        svgkey[(int(key[0:2]),m2n[key[2:5]],int(key[5:7]))] = key

    svlkey = {}
    for key in vlbi_sPs.keys():
        # tuple: year, month, day
        svlkey[(int(key[0:2]),m2n[key[2:5]],int(key[5:7]))] = key
        
    
    return vgos_stations, vlbi_stations, svgkey, svlkey, vgos_sPs, vlbi_sPs


# In[311]:


# # problematic stations
# psl = {session:[] for session in param.keys()}
# psl['17DEC04VG'] = ['RAEGYEB']
# psl['17DEC05VG'] = ['RAEGYEB']
# psl['17DEC06VG'] = ['RAEGYEB']
# psl['17DEC07VG'] = ['RAEGYEB']
# psl['19FEB04VG'] = ['GGAO12M']
# psl['19JUL22VG'] = ['KOKEE12M']
# psl['20JAN21VG'] = ['ISHIOKA']
# psl['20OCT13VG'] = ['WETTZ13S']
# psl['21JAN21VG'] = ['RAEGYEB']
# psl['21FEB01VG'] = ['RAEGYEB']


# In[ ]:


# # delete the problematic stations if exists
# for session in param.keys():
#     if psl[session]:
#         if psl[session][0] in param[session].keys():
#             del param[session][psl[session][0]]


# In[ ]:
