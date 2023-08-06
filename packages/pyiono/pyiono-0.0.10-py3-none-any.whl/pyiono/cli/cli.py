# Import the libraries
import argparse
from configparser import ConfigParser
import logging

import os
import sys

import numpy as np
import datetime

import v_download
import v_data
import v_vgos
import g_gnss
import v_analysis


class argument_management:
    
    def __ini__(self):
        pass
    
    @classmethod
    def parse_arguments(cls, ini_file: str):

        """ This function read the arguments from the command line."""

        # cnfiguration file
        config = ConfigParser()
        _ = config.read(ini_file)

        # Create the parser
        my_parser = argparse.ArgumentParser(description='It derives VTECs from Geodetic VLBI/VGOS Observations')

        # verbose
        my_parser.add_argument('-v', '--verbose', action='store_false', help='stop displaying the logging in the console, e.g., -v')
        # time window arguments
        my_parser.add_argument('-s', '--startDate', type=str, metavar='', required=False, 
                               help='set the start date of the time window to be searched for VGOS sessions, e.g. -s 2020/12/31.')
        my_parser.add_argument('-e', '--endDate', type=str, metavar='', required=False,
                               help='set the end date of the time window to be searched for VGOS session, e.g., -e 2021/06/21')

        # VLBI/VGOS download arguments
        my_parser.add_argument('-dvg', '--download_VGOS_VG', action='store_true', 
                               help='downlaod VGOS 24-hour sessions ending with VG, e.g., -dvg')
        my_parser.add_argument('-dxa', '--download_VLBI_XA', action='store_true',
                               help='downlaod geodetic VLBI 24-hour sessions ending with XA, e.g., -dxa')
        my_parser.add_argument('-dxb', '--download_VLBI_XB', action='store_true',
                               help='downlaod geodetic VLBI XB sessions ending with XB, e.g., -dxb')
        my_parser.add_argument('-dg', '--download_GIMs', type=int, 
                               default=int(config.get(section = 'default', option = 'download_GIMs')),
                               help='downlaod global ionospheric maps (GIMs) corresponding to VGOS 24-hour sessions, e.g., -dg')
        my_parser.add_argument('-dm', '--download_MTMs', type=int, 
                               default=int(config.get(section = 'default', option = 'download_MTMs')),
                               help='downlaod Madrigal TEC maps (MTMs) corresponding to VGOS 24-hour sessions, e.g., -dm')


        # VLBI/VGOS processing arguments 
        my_parser.add_argument('-pvg', '--process_VGOS_VG', action='store_true',
                               help='process VGOS 24-hour sessions that end with VG, e.g., -pvg')
        my_parser.add_argument('-pxa', '--process_VLBI_XA', action='store_true',
                               help='process VLBI 24-hour sessions that end with XA, e.g., -pxa')
        my_parser.add_argument('-pxb', '--process_VLBI_XB', action='store_true', 
                               help='process VLBI 24-hour sessions that end with XB, e.g., -pxb')
        my_parser.add_argument('-exp', '--exclude_problematic_stations', 
                               default=int(config.get(section = 'default', option = 'exclude_problematic_stations')), 
                               help='exclude the problematic stations listed in the PSL file, e.g., -exp 1')
        my_parser.add_argument('-c', '--cut_off_angle', type=int, default = int(config.get(section = 'default', option = 'cut_off_angle')),
                               help='set the cut-off angle in degrees, e.g., -c 5')
        my_parser.add_argument('-snr', '--s2nr_threshold', type=int, 
                               default = int(config.get(section = 'default', option = 's2nr_threshold')),
                               help='set the signal-to-noise ratio threshold, e.g., -snr 15')
        my_parser.add_argument('-od', '--outlier_detection',   type=int, 
                               default=int(config.get(section = 'default', option = 'outlier_detection')),
                               help='eliminate all significant outliers. This process could be computationally expensive, e.g., -od 1')    

        my_parser.add_argument('-vr', '--v_resolution', type = int,
                               default =  int(config.get(section = 'default', option = 'v_resolution')),
                               help='set the temporal resolution in minutes for deriving VTEC time series from VLBI/VGOS observations, \
                               e.g., -vr 60')

        my_parser.add_argument('-soi', '--sum_instr_offsets', type=int, 
                               default=int(config.get(section = 'default', option = 'sum_instr_offsets')),
                               help='apply the condition that the sum of instrumental offsets equals zero, e.g., -soi 1')
        my_parser.add_argument('-rel', '--rel_constraints', type=int, 
                               default=int(config.get(section = 'default', option = 'rel_constraints')),
                               help='apply the relative constraints, e.g., -rel 1')
        my_parser.add_argument('-vce', '--variance_component', type=int, 
                               default=int(config.get(section = 'default', option = 'variance_component')),
                               help='apply the variance component estimation per radio source per baseline or satellite, e.g., -vce 1')    

        my_parser.add_argument('-cwg', '--compare_with_GIMs', type=int, 
                               default=int(config.get(section = 'default', option = 'compare_with_GIMs')),
                               help='compare with Global Ionosphere Maps (GIMs), e.g., -cwg 1')
        my_parser.add_argument('-cwm', '--compare_with_MTMs', type=int, 
                               default=int(config.get(section = 'default', option = 'compare_with_MTMs')),
                               help='compare with Madrigal TEC Maps (MTMs), e.g., -cwm 1')
        my_parser.add_argument('-ss', '--summarise_sessions', type=int, 
                               default=int(config.get(section = 'default', option = 'summarise_sessions')),
                               help='plot the VTEC RMS differences, VTEC uncertainties, gradients, instrumental offsets of \
                               all the processed sessions, e.g., -ss 1')

        my_parser.add_argument('-eb', '--error_bar', type=int, default=int(config.get(section = 'default', option = 'error_bar')), 
                               help='display the error bars, e.g., -eb 1')


        # GNSS processing arguments 
        my_parser.add_argument('-pg', '--process_gnss', action='store_true',
                               help='process GNSS observations from ground stations, e.g., -pg')
        my_parser.add_argument('-gr', '--g_resolution', type=int, 
                               default = int(config.get(section = 'default', option = 'g_resolution')),
                               help='set the temporal resolution in minutes, e.g., 60, for deriving VTEC time series from GNSS observations, e.g., -gr 60')


        # Common VLBI/VGOS/GNSS Processing Arguments
        my_parser.add_argument('-geom', '--geomagnetic_lat', type=int,
                               default=int(config.get(section = 'default', option = 'geomagnetic_lat')),
                               help= 'use the geomagnetic latitude.') 
        my_parser.add_argument('-modip', '--modified_dip_lat', type=int,
                               default=int(config.get(section = 'default', option = 'modified_dip_lat')), 
                               help= 'use the geographic lat instead of modip lat.')
        my_parser.add_argument('-mdlg', '--modified_dip_lat_grid', type=int, 
                               default=int(config.get(section = 'default', option = 'modified_dip_lat_grid')), 
                               help='interpolate from the dip grid instead of calcuating it directly from IGRF13.')
        my_parser.add_argument('-g', '--two_gradients', type=int, 
                               default=int(config.get(section = 'default', option = 'two_gradients')), 
                               help='estimate north and south gradients instead of north/south gradient, e.g., -g 1')
        my_parser.add_argument('-mf', '--modified_mf', type=int, 
                               default=int(config.get(section = 'default', option = 'modified_mf')),
                               help='use the modified mapping function instead of the standard mapping function, e.g., -mf 1')
        my_parser.add_argument('-pf', '--plot_format', type=str,
                               default=config.get(section = 'default', option = 'plot_format'),
                               help = 'set the plot format, e.g., -pf png.')

        # path
        my_parser.add_argument('-dp', '--download_path', type=str,
                               default=config.get(section = 'default', option='download_path'),
                               help='define the full path to where you want to save the data, e.g., -dp C:/Users/John Doe/Desktop/')
        my_parser.add_argument('-in', '--input_path', type=str,
                               default=config.get(section = 'default', option = 'input_path'),
                               help='define the full path to where you have the data folder, e.g., -in C:/Users/John Doe/Desktop/')
        my_parser.add_argument('-out', '--output_path', type=str,
                               default=config.get(section = 'default', option = 'output_path'),
                               help='define the full path to where you want to save the results, e.g., -out C:/Users/John Doe/Desktop/')


        ### Execute parse_args()
        args, unknown = my_parser.parse_known_args()
        # print(vars(args))

        return args

    
    @classmethod
    def check_arguments(cls, args, logger):

        ###  check whether there is conflict in the arguments              
        
        # geomagnetic frames
        if args.geomagnetic_lat and args.modified_dip_lat:
            logger.critical('You cannot use different frames for the latitudes of IPP and VLBI/VGOS/GNSS station. ' +
                            'Please, specify either geomagnetic_lat or modified_dip_lat.') 
            sys.exit()    
    
    
class pipeline:
    
    def __ini__(self):
        pass
    
    @classmethod
    def execute_pipeline(cls, args, logger):

        ''' This function execute the pipeline. '''  
        
        ### download VLBI/VGOS sessions and/or obtain the name of the sessions
        
        # create a variable for VLBI/VGOS sessions 
        v_sessions, vgos_sessions, vlbi_sessions = [], [], []
        
        # download VLBI/VGOS sessions
        if args.download_VGOS_VG or args.download_VLBI_XA or args.download_VLBI_XB:  
            
            # get the session extension
            Ext = []
            if args.download_VGOS_VG:
                Ext = Ext + ['VG.tgz']
            if args.download_VLBI_XA:
                Ext = Ext + ['XA.tgz']
            if args.download_VLBI_XB:
                Ext = Ext + ['XB.tgz']

            # download VBLI/VGOS sessions
            v_sessions = v_download.file_download.v_download(logger, args.startDate, args.endDate,
                                                             ionex = args.download_GIMs, madrigal = args.download_MTMs,
                                                             extension = Ext, download_path = args.download_path)

            if v_sessions:
                # keep only the names of sessions to be processed                
                if args.process_VGOS_VG:
                    vgos_sessions = vgos_sessions + [session  for session in v_sessions if 'VG' in session if session not in vgos_sessions]
                if args.process_VLBI_XA:
                    vlbi_sessions = vlbi_sessions + [session  for session in v_sessions if 'XA' in session if session not in vlbi_sessions]
                if args.process_VLBI_XB:
                    vlbi_sessions = vlbi_sessions + [session  for session in v_sessions if 'XB' in session if session not in vlbi_sessions]
                    
            else:
                if args.download_VGOS_VG:
                    logger.info('no VGOS 24-hour session ending with VG was found in the given time window.')

                if args.download_VLBI_XA:
                    logger.info('no VLBI 24-hour session ending with XA was found in the given time window')

                if args.download_VLBI_XB:
                    logger.info('no VLBI 24-hour session ending with XB was found in the given time window.')
                

                
        # get the names of the sessions
        if args.process_VGOS_VG or args.process_VLBI_XA or args.process_VLBI_XB:  

            # get the path to VGOSDB
            vgosDB_path = args.input_path + 'Data/vgosDB/'

            # create a list of sessions
            sdate = datetime.datetime.strptime(args.startDate, '%Y/%m/%d').date()   # start date
            edate = datetime.datetime.strptime(args.endDate, '%Y/%m/%d').date()   # end date 

            session_list = []
            if args.process_VGOS_VG:           
                session_list = session_list + [(sdate + datetime.timedelta(days=i)).strftime('%y%b%d').upper() + 'VG' 
                                               for i in range((edate - sdate ).days + 1)]

            if args.process_VLBI_XA:         
                session_list = session_list + [(sdate + datetime.timedelta(days=i)).strftime('%y%b%d').upper() + 'XA' 
                                               for i in range((edate - sdate ).days + 1)]                 

            if args.process_VLBI_XB:
                session_list = session_list + [(sdate + datetime.timedelta(days=i)).strftime('%y%b%d').upper() + 'XB' 
                                               for i in range((edate - sdate ).days + 1)]

            # keeps only sessions that exist
            v_sessions = [session for session in session_list if os.path.exists(vgosDB_path + str(2000 + int(session[0:2]))
                                                                                + '/' + session + '/')]
            if v_sessions:                
                # keep only the names of sessions to be processed
                if args.process_VGOS_VG:
                    vgos_sessions = vgos_sessions + [session  for session in v_sessions if 'VG' in session if session not in vgos_sessions]
                if args.process_VLBI_XA:
                    vlbi_sessions = vlbi_sessions + [session  for session in v_sessions if 'XA' in session if session not in vlbi_sessions]
                if args.process_VLBI_XB:
                    vlbi_sessions = vlbi_sessions + [session  for session in v_sessions if 'XB' in session if session not in vlbi_sessions]

            else:
                logger.info(f'no session was found in the given path: {vgosDB_path}')


        ### process VGOS data
        if args.process_VGOS_VG:

            if args.exclude_problematic_stations:
                # get the list of problematic stations
                psl = v_data.v_data.exclude_problematic_stations(logger, vgos_sessions, v_input_path = args.input_path)
            else:
                psl = {session:[] for session in vgos_sessions}

            param = {}
            for session in vgos_sessions: 
                try:
                    logger.info(f'Attempting to process VGOS session {session} ..')

                    param[session] = v_vgos.v_vgos.v_processing(logger, session, resolution = args.v_resolution, 
                                                                modified_mf = args.modified_mf, rel_constraints = args.rel_constraints, 
                                                                outlier_detection = args.outlier_detection,
                                                                cutoffangle = args.cut_off_angle, vce = args.variance_component,
                                                                snr = args.s2nr_threshold, gims = args.compare_with_GIMs,
                                                                madrigal = args.compare_with_MTMs, 
                                                                sum_instr_offsets = args.sum_instr_offsets,
                                                                error_bar = args.error_bar, gradient = args.two_gradients,
                                                                geomagnetic = args.geomagnetic_lat, modip = args.modified_dip_lat,
                                                                modip_grid = args.modified_dip_lat_grid, v_input_path = args.input_path,
                                                                v_output_path = args.output_path, exSta = psl[session],
                                                                plot_format = args.plot_format) 

                    logger.info(f'Successfully processed VGOS session {session}.')

                except Exception as e:                
                    logger.error(f'failed to process VGOS session {session}!')
                    logger.debug(e)
            
            if args.summarise_sessions:
                if param:
                    logger.info('Attempting to analyse the processed VGOS sessions ..')
                    try:
                        v_analysis.v_analysis.plot_vgos_analysis_results(logger, param, gradient = args.two_gradients,
                                                                         v_output_path = args.output_path,  
                                                                         plot_format = args.plot_format)                    
                        logger.info('Successfully analysed the processed VGOS sessions.')
                    except Exception as e:
                        logger.error('failed to analyse the processed VGOS sessions!')
                        logger.debug(e)

                        
        ### process VLBI data
        if args.process_VLBI_XA or args.process_VLBI_XB:

            if args.exclude_problematic_stations:
                # get the list of problematic stations
                psl = v_data.v_data.exclude_problematic_stations(logger, vlbi_sessions, v_input_path = args.input_path)
            else:
                psl = {session:[] for session in vlbi_sessions}

            param = {}
            for session in vlbi_sessions: 
                try:
                    logger.info(f'Attempting to process VLBI session {session} ..')

                    param[session] = v_vgos.v_vgos.v_processing(logger, session, resolution = args.v_resolution, 
                                                                modified_mf = args.modified_mf, rel_constraints = args.rel_constraints, 
                                                                outlier_detection = args.outlier_detection,
                                                                cutoffangle = args.cut_off_angle, vce = args.variance_component,
                                                                snr = args.s2nr_threshold, gims = args.compare_with_GIMs,
                                                                madrigal = args.compare_with_MTMs, 
                                                                sum_instr_offsets = args.sum_instr_offsets,
                                                                error_bar = args.error_bar, gradient = args.two_gradients,
                                                                geomagnetic = args.geomagnetic_lat, modip = args.modified_dip_lat,
                                                                modip_grid = args.modified_dip_lat_grid, v_input_path = args.input_path,
                                                                v_output_path = args.output_path, exSta = psl[session],
                                                                plot_format = args.plot_format) 

                    logger.info(f'Successfully processed VLBI session {session}.')

                except Exception as e:                
                    logger.error(f'failed to process VLBI session {session}!')
                    logger.debug(e)
            
            if args.summarise_sessions:
                if param:
                    logger.info('Attempting to analyse the processed VLBI sessions ..')
                    try:
                        v_analysis.v_analysis.plot_vlbi_analysis_results(logger, param, gradient = args.two_gradients,
                                                                         v_output_path = args.output_path,
                                                                         plot_format = args.plot_format)
                        logger.info('Successfully analysed the processed VLBI sessions.')
                    except Exception as e:
                        logger.error('failed to analyse the processed VLBI sessions!')
                        logger.debug(e)
                    
    
        ### process GNSS data
        if args.process_gnss:

            # create a list of sessions
            sdate = datetime.datetime.strptime(args.startDate, '%Y/%m/%d').date()   # start date
            edate = datetime.datetime.strptime(args.endDate, '%Y/%m/%d').date()   # end date        
            session_list = [(sdate + datetime.timedelta(days=i)).strftime('%y%b%d').upper() for i in range((edate - sdate ).days + 1)]

            # keeps only sessions that exist
            g_path = os.path.join(args.input_path + 'Data/GNSS/')
            g_sessions=[session for session in session_list 
                        if os.path.isfile(os.path.join(g_path+str(2000+int(session[0:2]))+'/'+session+'.TEC'))]
            
            # processing GNSS data
            for session in g_sessions:   
                logger.info(f'Attempting to process GNSS campaign {session} ..')
                try:
                    x, sxx = g_gnss.g_gnss.g_processing(logger, session, resolution = args.g_resolution, 
                                                        cutoffangle = args.cut_off_angle, vce = args.variance_component, 
                                                        modified_mf = args.modified_mf, geomagnetic = args.geomagnetic_lat,
                                                        modip = args.modified_dip_lat, modip_grid = args.modified_dip_lat_grid,
                                                        outlier_detection = args.outlier_detection, rel_constraints = args.rel_constraints,
                                                        g_input_path = args.input_path, g_output_path = args.output_path, 
                                                        plot_format = args.plot_format)
                    # logger.info(f'Successfully processed GNSS campaign {session}.')
                except Exception as e:
                    logger.error(f'failed to process GNSS data!')                
                    logger.debug(e)
        

def main():   
    
    # Some logging
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    
    consoleHandler = logging.StreamHandler()
    consoleHandler.setLevel(logging.DEBUG)
        
    # get the arguments
    if sys.argv[1].endswith('.ini'):
        args = argument_management.parse_arguments(ini_file = sys.argv[1])
    else:
        default_ini_file = 'config.ini'
        args = argument_management.parse_arguments(ini_file = default_ini_file)
    
    # add a console handler if asked
    if args.verbose:
        logger.addHandler(consoleHandler)
        
    # set the format
    formatter = logging.Formatter('%(asctime)s %(filename)s:%(lineno)d %(levelname)s - %(message)s', '%Y-%m-%d %H:%M:%S')
    consoleHandler.setFormatter(formatter)    
    
    # log which ini file will be used
    if sys.argv[1].endswith('.ini'):
        logger.info(f'The ini file {sys.argv[1]} will be used.')
    else:
        logger.info(f'The default ini file {default_ini_file} will be used.')
        
    # check the arguments for conflicts
    argument_management.check_arguments(args, logger)
        
    # execute the pipeline
    pipeline.execute_pipeline(args, logger)    
    
if __name__ == '__main__':
    main()
    
