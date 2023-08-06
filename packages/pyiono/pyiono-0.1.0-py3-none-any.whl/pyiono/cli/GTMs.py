
import os
import re

import numpy as np
import statistics
import math
import pyproj
import random
import netCDF4 as nc

import datetime
import time

from scipy import signal

import multiprocessing

import GIMs_Helpers


class Global_TEC_Maps:
    
    def __ini__(self):
        pass
        
    @classmethod
    def VTEC_GIMs(cls, logger, h0, resolution, time_windows,
                                stationLLA, ionex_doy, gims, ionex_path = 'Data/Ionex/'):

        '''This function extracts VTEC time series from global ionosphere maps at a given location.'''

        # get VTEC per station from GIMs

        # get the epochs of the estimates
        epochs = int(h0) + time_windows
        
        try:
            with multiprocessing.Pool() as pool:                
                data = [(stationLLA, year, day, ionex_path) for year in ionex_doy.keys() for day in ionex_doy[year]]
                results = pool.starmap(GIMs_Helpers.Helpers.extract_series, data)
                            
            # epochs per station (sps)
            eps = sum([list(np.array(item[0]) + 24*i) for i, item in enumerate(results)], [])
            
            # vtec time series per station (vps)
            ns = len(results) # number of vtec time series per station
            vps = np.array([sum([item[1][i] for item in results],[]) for i in range(stationLLA.shape[0])]).transpose()
            
            # interpolate the vtec time series as often as needed according to the resolution
            gims_vtec = np.round(np.array([np.interp(epochs, eps, vps[:,i]) for i in range(0, vps.shape[1], 1)]).transpose(), 3)
                    
        except Exception as e:
            logger.error('failed to find/process the ionex file --> global ionospheric maps is excluded.')
            # logger.debug(e)
            gims_vtec = np.array([])
            gims = 0

        return gims, gims_vtec
    
    
    @classmethod
    def VTEC_MTMs(cls, logger, session, stations, exSta, stationLLA, startTime, endTime, madrigal = 1, path = 'Data/Madrigal/'):

        '''This function extracts VTEC time series from Madrigal TEC maps (MTMs) at a given location. It also smoothes the time series using the Savitzky–Golay filter.'''

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
                        elif os.path.isfile(path + file + 'g.003.nc'):
                            file = file + 'g.003.nc'
                        elif os.path.isfile(path + file + 'g.004.nc'):
                            file = file + 'g.004.nc'
                        elif os.path.isfile(path + file + 'g.005.nc'):
                            file = file + 'g.005.nc'
                        else:
                            logger.info('could not find the Madrigal files in the given directory')
                                                    
                        ds = nc.Dataset(os.path.join(path + file))

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
                        
                        # close the dataset
                        ds.close()
                        
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
                                eindx = j
                                break
                            else:
                                eindx = j

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
                        #print(window_length, ployorder)
                        # smooth the x data and get only the data corresponding to the given 
                        ysmth = signal.savgol_filter(ymadr,window_length,ployorder)

                        # stack the epochs, the original VTECs and the smoothed VTECs
                        madr[station] = np.column_stack((xmadr[sindx:eindx], ymadr[sindx:eindx], ysmth[sindx:eindx]))
            
        except Exception as e:        
            logger.error('failed to find/process the Madrigal file --> Madrigal TEC maps is excluded.')
            # logger.debug(e)
            madrigal = 0

        return madrigal, madr
    