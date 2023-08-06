

# Import the libraries
import argparse

import os
import sys

import numpy as np
import datetime

# from ftplib import FTP_TLS
# import subprocess
# import datetime
# import time
# import tarfile
# import shutil

# from unlzw3 import unlzw

# import download_madrigal

# import os
# import re
# import subprocess
# from scipy.io import loadmat
# import netCDF4 as nc
# import shelve
# import csv

# import numpy as np
# import statistics
# import math
# import pyproj
# import random

# from scipy.optimize import least_squares
# import matplotlib.pylab as plt
# import matplotlib.cm
# import matplotlib.colors
# import matplotlib
# matplotlib.use('Agg')

# import collections
# from scipy import signal

# import aacgmv2



import v_download
import v_test



# Create the parser
my_parser = argparse.ArgumentParser(description='Derive VTECs from Geodetic VLBI/VGOS Observations')

# Add the arguments
# time window arguments
my_parser.add_argument('-s', '--startDate', type=str, metavar='', required=True, help='start date of the time window to be searched for VGOS sessions, e.g. 2020/12/31')
my_parser.add_argument('-e', '--endDate', type=str, metavar='', required=True, help='end date of the time window to be searched for VGOS session, e.g. 2021/06/21')

# download arguments
my_parser.add_argument('-dv', '--download_vgos', action='store_true', help='downlaod VGOS sessions?')
my_parser.add_argument('-p', '--path', type=str, metavar='', help='path to data', default='/Data/')


# processing arguments 
my_parser.add_argument('-pv', '--process_vgos', action='store_true', help='process VGOS sessions?')
my_parser.add_argument('-r', '--resolution', type=int, help='temporal resolution of VTEC time series in minutes, e.g. 60', default = 60)
my_parser.add_argument('-rel', '--rel_constraints', action='store_false', help='apply relative constraints?')
my_parser.add_argument('-vce', '--variance_component', action='store_false', help='estimate variance component per radio source per baseline?')
my_parser.add_argument('-out', '--outlier_detection', action='store_true', help='eliminate all significant outliers?')
my_parser.add_argument('-c', '--cutoffangle', type=int, help='cut-off angle in degrees, e.g. 5', default = 5)
my_parser.add_argument('-snr', '--s2nr_threshold', type=int, help='signal to noise ratio threshold, e.g. 15', default = 15)

my_parser.add_argument('-gims', '--GIMs', action='store_false', help='compare with Global Ionosphere Maps?')
my_parser.add_argument('-madr', '--Madrigal', action='store_false', help='compare with Madrigal TEC Maps?')

my_parser.add_argument('-g', '--gradient', action='store_false', help='estimate only one gradient, e.g. Gns?')
my_parser.add_argument('-soi', '--sum_instr_offsets', action='store_false', help='apply the condition that the sum of instrumental offsets equals zero?')
my_parser.add_argument('-geom', '--geomagnetic_lat', action='store_true', help='use geomagnetic lat?') 
my_parser.add_argument('-modip', '--modified_dip_lat', action='store_false', help='use modip lat?')
my_parser.add_argument('-mdlg', '--modified_dip_lat_grid', action='store_false', help='use modip grid?') 
my_parser.add_argument('-eb', '--error_bar', action='store_false', help='display error bars?')
my_parser.add_argument('-mf', '--mapping_function', action='store_false', help='use the modified mapping function?')


# Execute parse_args()
args = my_parser.parse_args()


sessions = []
# download
if args.download_vgos:    
    sessions = v_download.v_download(args.startDate, args.endDate)
    

# rename the sessions for consistency purposes
path = 'Data/vgosDB/'
years = os.listdir(path)
for year in years:
    # rename the folder for consistency, e.g. 19MAY21VG
    session_list = os.listdir(path + year + '/')
    for session in session_list:
        if len(session) > 9:
            os.rename(path +  year + '/' + session, path +  year + '/' + session[:9])                
        
        
# get the names of the sessions
path = 'Data/vgosDB/'
if not sessions:
    # from datetime import date, timedelta
    sdate = datetime.datetime.strptime(args.startDate, '%Y/%m/%d').date()   # start date
    edate = datetime.datetime.strptime(args.endDate, '%Y/%m/%d').date()   # end date        
    p_sessions = [(sdate + datetime.timedelta(days=i)).strftime('%y%b%d').upper()+'VG' for i in range((edate - sdate ).days + 1)]
    
    sessions = [session for session in p_sessions if os.path.exists(path + str(2000 + int(session[0:2])) + '/' + session + '/')]

    
print(sessions)
# print(vars(args))

# process
if args.process_vgos:       
    for session in sessions:  
        try:
            v_test.v_processing(session, resolution = args.resolution, optimize_mf = args.mapping_function, 
                                rel_constraints = args.rel_constraints, outlier_detection = args.outlier_detection, 
                                cutoffangle = args.cutoffangle, vce = args.variance_component, snr = args.s2nr_threshold, 
                                gims = args.GIMs, madrigal = args.Madrigal, sum_instr_offsets = args.sum_instr_offsets, 
                                error_bar = args.error_bar, gradient = args.gradient, geomagnetic = args.geomagnetic_lat,
                                modip = args.modified_dip_lat, modip_grid = args.modified_dip_lat_grid,
                                v_output_path = 'Results/', exSta = []) 
            
        except:
            print('failed to process session: ', session)

            
    
    
