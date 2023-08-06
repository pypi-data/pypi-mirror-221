

import numpy as np
import statistics
import math
import pyproj
import random
import os

import datetime
import time

from magnetic_field_calculator import MagneticFieldCalculator

import multiprocessing

class IPP:
    
    def __ini__(self):
        pass
    
    @classmethod
    def get_geomagnetic_lats(cls, logger, lats, lons):

        '''This function calculates the geomagnetic latitude.'''

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
    

    @classmethod
    def get_dip_grid(cls, logger, session):

        '''This function generates the grid of the magnetic dips from IGRF13. 

        The grid spatial resolution is 2.5 x 5 degrees in latitude and longitude. '''

        # create an object for calculating the magnetic dip 
        calculator = MagneticFieldCalculator(model='IGRF', revision='13', custom_url='https://example.com')

        # create a multiprocessing pool
        with multiprocessing.Pool() as p:
            # generate a grid of 2.5x5 in latxlon
            results = p.starmap(calculator.calculate,
                                [(lat, lon, None, None, None, str(2000+int(session[:2])), None) 
                                 for lat in np.arange(90,-92.5,-2.5) 
                                 for lon in np.arange(-180, 185, 5)])


        # extract the dips and reshape the grid
        m_dips = np.deg2rad(np.array([result['field-value']['inclination']['value'] for result in results]).reshape((73, 73)))

        return m_dips        

    
    @classmethod
    def interpolate_dips(cls, logger, grid, lat, lon):

        '''This function bivariately interpolates for the magnetic dip from a grid of 2.5 x 5 degrees in latitude x longitude.'''

        # bivariately interpolate for the magnetic dip from a grid of 2.5 x 5 degrees in lat x lon

        # convert the latitude and longitude from radian to degrees    
        lat, lon = np.rad2deg(lat), np.rad2deg(lon)

        # get the indice of the latitude and longitude of the 4 grid points surrounding the site of VGOS/VLBI station or IPP
        latu = math.floor((90 - lat)*(grid.shape[0]-1)/(180)) # upper latitude
        latl = math.ceil((90 - lat)*(grid.shape[0]-1)/(180)) # lower latitude
        lonr = math.ceil((180 + lon)*(grid.shape[1]-1)/360) # right longitude
        lonl = math.floor((180 + lon)*(grid.shape[1]-1)/360) # left longitude

        # get the TEC values at the surrounding points
        Eul = grid[latu,lonl]
        Eur = grid[latu,lonr]
        Ell = grid[latl,lonl]
        Elr = grid[latl,lonr]

        # get the difference in lat and lon between the VGOS/VLBI station and the lower, left corner
        dlatl = 2.5 - (87.5 - lat)%2.5
        dlonl = 5 - (180 - lon)%5 # (180 + lon)%5

        # get the weights of the surrounding points
        p = dlonl/2.5
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

    
    @classmethod
    def get_modips(cls, logger, session, lats, lons):

        '''This function calculates the modip latitude from IGRF13 at a given location.'''

        # convert from radian to degrees
        lats, lons = np.rad2deg(lats), np.rad2deg(lons)

        # create a dictionry for months
        m2n = {m:i+1 for i, m in enumerate(['JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN', 'JUL', 'AUG', 'SEP', 'OCT', 'NOV','DEC'])}

        # 
        date = str(2000+int(session[:2])) + '-' + str(m2n[session[2:5]])+'-'+session[5:7]

        # create an object for calculating the magnetic dip 
        calculator = MagneticFieldCalculator(model='IGRF', revision='13', custom_url='https://example.com')

        # create a multiprocessing pool
        with multiprocessing.Pool() as p:
            # generate a grid of 2.5x5 in latxlon
            results = p.starmap(calculator.calculate, [(lat, lons[i], None, None, None, None,date) for i, lat in enumerate(lats)])

        # reshape the grid
        m_dips = np.deg2rad(np.array([result['field-value']['inclination']['value'] 
                                      for result in results]).reshape((lons.shape[0])))

        modips = np.arctan(m_dips/np.sqrt(np.cos(np.deg2rad(lats))))

        return modips        

    
    @classmethod
    def IPP_LLA(cls, logger, session, stationLLA, meta_data, geomagnetic, modip, modip_grid):

        '''This function calculates the latitude and longitude of ionospheric pierce point.'''

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
            meta_data[n,i,3] = cls.get_geomagnetic_lats(logger, meta_data[:,:,3], meta_data[:,:,4])

            # get the geomagnetic latitude for all the stations
            meta_data[n,i,3] = cls.get_geomagnetic_lats(logger, meta_data[:,:,5], meta_data[:,:,6])


        elif modip:
            if modip_grid:            
                # use the grid for fast solution            
                if os.path.isfile('dips_' + str(2000+int(session[:2]))+'.txt'):
                    # load the grid
                    with open('dips_' + str(2000+int(session[:2])) + '.txt', 'r') as file:
                        dips = np.array([line.split() for line in file.readlines()]).astype(float)
                    file.close()
                else:
                    # calcuate the dips from scratch
                    dips = cls.get_dip_grid(logger, session)
                    with open('dips_' + str(2000+int(session[:2])) +'.txt', 'w') as file: # change the date to year
                        np.savetxt(file, dips, fmt='%s')
                    file.close()

                # get the modifed dip latitude for IPPs
                meta_data[:,0,3] = np.array([cls.interpolate_dips(logger, dips, lat, meta_data[i,0,4]) 
                                             for i, lat in enumerate(meta_data[:,0,3])])
                meta_data[:,1,3] = np.array([cls.interpolate_dips(logger, dips, lat, meta_data[i,1,4]) 
                                             for i, lat in enumerate(meta_data[:,1,3])])

                # get the modifed dip latitude for all the stations
                smodips = [cls.interpolate_dips(logger, dips, item[0], item[1]) for item in np.deg2rad(stationLLA)]
                meta_data[:,0,5] = [smodips[int(item)-1] for item in meta_data[:,0,0]]
                meta_data[:,1,5] = [smodips[int(item)-1] for item in meta_data[:,1,0]]


            else:
                # calculate for all points for accurate solution
                # get the modifed latitude for IPPs
                meta_data[:,0,3] = cls.get_modips(logger, session, meta_data[:,0,3], meta_data[:,0,4])
                meta_data[:,1,3] = cls.get_modips(logger, session, meta_data[:,1,3], meta_data[:,1,4])

                # get the modifed latitude for all the stations
                smodips = [cls.get_modips(logger, session, np.array([item[0]]), np.array([item[1]])) 
                           for item in np.deg2rad(stationLLA[:,:2])]
                # map them to the observations
                meta_data[:,0,5] = [smodips[int(item)-1] for item in meta_data[:,0,0]]
                meta_data[:,1,5] = [smodips[int(item)-1] for item in meta_data[:,1,0]]

        return meta_data
    