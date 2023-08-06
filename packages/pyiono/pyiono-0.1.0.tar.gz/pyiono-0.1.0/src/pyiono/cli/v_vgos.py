

import os
import re
from scipy.io import loadmat
import netCDF4 as nc
import csv
import shutil

import numpy as np
import statistics
import math
import pyproj
import random

from scipy.optimize import least_squares
import matplotlib.pylab as plt
import matplotlib
matplotlib.use('Agg')

import datetime
import time

from scipy import signal
import scipy

from magnetic_field_calculator import MagneticFieldCalculator

import v_data
import IPP
import v_lsq
import v_rps_results
import v_analysis


class v_vgos:
    
    def __ini__(self):
        pass

    
    @classmethod
    def v_processing(cls, logger, session, resolution = 60, exSta = [], snr = 0, cutoffangle = 0, modified_mf = 1, rel_constraints = 1,
                     outlier_detection = 1, minObs = 5, vce = 1, sum_instr_offsets = 0, v_input_path = '', 
                     v_output_path = '', error_bar = 1, gradient = 1, gims = 1, madrigal = 1,                
                     geomagnetic = 0, modip = 1, modip_grid = 1, plot_format = 'jpg'):

        '''This function derives VTEC time series from geodetic VLBI/VGOS observations above VLBI/VGOS sites.'''

        # get the path
        if v_input_path: 
            vgosDB_path = os.path.join(v_input_path + 'Data/vgosDB/')
            ionex_path = os.path.join(v_input_path + 'Data/Ionex/')
            madrigal_path = os.path.join(v_input_path + 'Data/Madrigal/')     

        else:
            vgosDB_path = os.path.join('Data/vgosDB/')
            ionex_path = os.path.join('Data/Ionex/')
            madrigal_path = os.path.join('Data/Madrigal/')

        if v_output_path:  
            if 'VG' in session:
                v_output_path = os.path.join(v_output_path, 'Results/VGOS/')
            elif 'XA' in session or 'XB' in session:
                v_output_path = os.path.join(v_output_path, 'Results/VLBI/')
        else:
            if 'VG' in session:
                v_output_path = os.path.join('Results/VGOS/')
            elif 'XA' in session or 'XB' in session:
                v_output_path = os.path.join('Results/VLBI/')
        
        # read VGOS/VLBI data
        h0, freq, nSta, stations, stationLLA, stationXYZ, meta_data, dtec, dtecstd, t, v_doy, Sources, s2nr = \
        v_data.v_data.v_data(logger, session, exSta, snr, cutoffangle, minObs, vgosDB_path, geomagnetic, modip, modip_grid)
               
        # get the number of Parameters
        nPara, time_windows = v_lsq.v_lsq.nPara_time_window(logger, t, gradient, resolution)    
        nPara = int(nPara)
                
        # extract the observations
        freq, meta_data, sta, elev, latIPP, lonIPP, latSta, lonSta, dtec, dtecstd, t, s2nr = \
        v_data.v_data.extract_observations(logger, freq, s2nr, meta_data, dtec, dtecstd, t)

        # get the time windows w/o observations
        rel_cindxe, cindxe, cindxr, rcindx, c = v_lsq.v_lsq.column_index(logger, nSta, nPara, sta[:,0], sta[:,1], t, time_windows,
                                                                         rel_constraints, sum_instr_offsets, gradient)        

        # get the initial values
        x0 = v_lsq.v_lsq.initial_values(logger, nSta, nPara, rcindx, gradient)

        if outlier_detection:

            logger.info('outlier detection is running .. ')
            # eliminate outliers
            freq, meta_data, sta, elev, latIPP, lonIPP, latSta, lonSta, dtec, dtecstd, t, s2nr, x0, orindx = \
            v_lsq.v_lsq.data_snooping(logger, h0, freq, nSta, nPara, s2nr, meta_data, stationLLA, stationXYZ, 
                                      dtec, dtecstd, t,time_windows, modified_mf, v_doy, sum_instr_offsets, gradient)


            # get an update on the time windows w/o observations
            rel_cindxe, cindxe, cindxr, rcindx, c = v_lsq.v_lsq.column_index(logger, nSta, nPara, sta[:,0], sta[:,1], t, time_windows,
                                                                             rel_constraints, sum_instr_offsets, gradient)

            logger.info('all possible outliers were eliminated.')


        # refine the estimates    
        x0, sxx, r, Obs2Source = v_lsq.v_lsq.refine_parameters(logger, freq, s2nr, nSta, nPara, x0, meta_data, 
                                                               stationXYZ, dtec, dtecstd, t, time_windows, modified_mf,
                                                               rel_constraints, vce, sum_instr_offsets, gradient)
        
        # map the parameters
        param = v_lsq.v_lsq.mapping_parameters(logger, nSta, nPara, resolution, stations, stationLLA, rcindx, exSta, x0, sxx, h0,
                                               time_windows, session, gradient, gims, madrigal, v_doy, ionex_path, madrigal_path)
        
        # save the plots of the remaining stations
        v_rps_results.v_rps_results.v_plot(logger, session, resolution, stations, stationLLA, int(h0), int(h0) + time_windows[-1],
                                           param, gims, madrigal, exSta, error_bar, madrigal_path, v_output_path, plot_format)
        
        # save the parameters in a text file
        v_rps_results.v_rps_results.save_results(logger, param, session, gradient, madrigal, gims, v_output_path)


        return param


