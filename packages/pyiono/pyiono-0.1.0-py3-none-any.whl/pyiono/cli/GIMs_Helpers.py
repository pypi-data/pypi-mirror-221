
import os
import re

import numpy as np
import math

class Helpers:
    
    def __ini__(self):
        pass
    
    
    @classmethod
    # parase the ionospheric map 
    def parse_map(cls, tec_map, exponent = -1):
        
        '''This function parses GIMs.'''
        
        # analyse the maps and then stack them in a numpy array
        tec_map = re.split('.*END OF TEC MAP', tec_map)[0]
        return np.stack([np.fromstring(l, sep=' ') for l in re.split('.*LAT/LON1/LON2/DLON/H\\n',tec_map)[1:]])*10**exponent
    
    
    @classmethod
    # get the GIMs file
    def get_tec_maps(cls, filename):
        '''This function reads and parses the ionex file.'''
        with open(filename) as file:
            # read the file content
            ionex = file.read()
            
            # get the exponent
            for line in ionex.split('\n'):
                if line.find('EXPONENT') != -1:
                    exponent = float(line.split()[0])
                    
            # get the maps
            tec_maps = [cls.parse_map(t, exponent) for t in ionex.split('START OF TEC MAP')[1:]]
            
            # get the epochs of the maps
            tec_maps_epochs = list(np.arange(0, 24+24/(len(tec_maps)-1), 24/(len(tec_maps)-1)))
            
        file.close()
        return tec_maps_epochs, tec_maps
    
    
    @classmethod
    # extract the VTEC at a specific location using Bivariate Interpolation
    def get_tec(cls, tec_map, lat, lon):
        
        '''This function spatially interpolates GIMs for VTECs at a given location. '''
        
        # get the indices of the latitudes and longitudes of the 4 GIMs points surrounding the site of VGOS/VLBI station
        latu = math.floor((87.5 - lat)*(tec_map.shape[0]-1)/(2*87.5)) # upper latitude
        latl = math.ceil((87.5 - lat)*(tec_map.shape[0]-1)/(2*87.5)) # lower latitude
        lonr = math.ceil((180 + lon)*(tec_map.shape[1]-1)/360) # right longitude
        lonl = math.floor((180 + lon)*(tec_map.shape[1]-1)/360) # left longitude

        # get the TEC values at the surrounding points
        Eul = tec_map[latu,lonl]
        Eur = tec_map[latu,lonr]
        Ell = tec_map[latl,lonl]
        Elr = tec_map[latl,lonr]

        # get the difference in lat and lon between the VGOS/VLBI station and the lower, left corner
        dlatl = 2.5 - (87.5 - lat)%2.5
        dlonl = 5 - (180 - lon)%5 # (180 + lon)%5 # 

        # get the weights of the surrounding points
        q = dlatl/2.5
        p = dlonl/5
        
        Wul = (1 - p)*q # upper, left point
        Wur = p*q # upper, right point
        Wll = (1 - q)*(1 - p) # lower, left point
        Wlr = (1 - q)*p # lower, right point

        E = round(sum([Wul*Eul, Wur*Eur, Wll*Ell, Wlr*Elr]), 3)

        return E
    

    @classmethod
    def ionex_local_path(cls, directory):
        
        '''This function obtains the directory to the ionex file'''
        
        # get the file name and return its directory
        file = os.listdir(directory)
        return directory + '/' + file[0]
    
    
    @classmethod
    def extract_series(cls, lat_lon, year, day, ionex_path):
        
        '''This function extracts the VTEC time series from GIMs'''
        
        # get the directory to the GIMs file
        directory = ionex_path + year + '/' + day
        
        # get the TEC maps
        vtec_epochs, tec_maps = cls.get_tec_maps(cls.ionex_local_path(directory))
        
        # extract the maps and return the vtec series of the day
        vtec_series = [[cls.get_tec(tec_map, item[0], item[1]) for tec_map in tec_maps] for i, item in enumerate(lat_lon)]
        
        return vtec_epochs, vtec_series
    
    