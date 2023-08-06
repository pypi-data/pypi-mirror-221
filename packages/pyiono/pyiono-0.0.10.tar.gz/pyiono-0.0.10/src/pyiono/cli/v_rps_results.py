
import os
import re
from scipy.io import loadmat
import netCDF4 as nc
import csv
import shutil

import numpy as np
import datetime

from scipy.optimize import least_squares
import matplotlib.pylab as plt
import matplotlib
matplotlib.use('Agg')

import GTMs
import v_analysis
import g_gnss

class v_rps_results:

    def __ini__(self):
        pass
        
        
    @classmethod
    def v_plot(cls, logger, session, resolution, stations, stationLLA, startTime, endTime, param, 
               gims, madrigal, exSta, error_bar, madrigal_path, v_output_path = 'Results/VGOS/',
               plot_format = 'jpg'):

        '''This function plots the VTEC time series for geodetic VLBI/VGOS stations.'''

        # create a figure    
        # %matplotlib notebook
        plt.rcParams["figure.figsize"] = (10,4)
        # adjust the linewidth
        plt.rcParams['lines.linewidth'] = 2
        plt.rcParams['axes.linewidth'] = 1.5
        # adjust the font
        plt.rcParams.update({'font.size': 10})
        

        # get the VTECs from Madrigal
        if madrigal:
            madrigal, madr = GTMs.Global_TEC_Maps.VTEC_MTMs(logger, session, stations, exSta, stationLLA,
                                                                startTime, endTime, madrigal, madrigal_path)

        # get the biases
        v_bias = v_analysis.v_analysis.v_gims_mtms_bias(logger, param)

        # create a dictionry for months
        m2n = {m:i+1 for i, m in enumerate(['JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN', 'JUL', 'AUG', 'SEP', 'OCT', 'NOV','DEC'])}
                
                        
        # loop over the stations
        for station in stations: 
            # exclude the problematic stations
            if station not in exSta: 
                
                # get the label for the results
                if 'VG' in session:
                    vlabel = f'{station} (VGOS)'
                else: # 'XA' or 'XB' in session:
                    vlabel = f'{station} (VLBI)'

                # get the observation epochs
                epochs = []
                obsDTs = []
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
                    
                    # get the observation full epoch
                    obsDateTime = datetime.datetime(int(d[0]), int(d[1].rjust(2,'0')), 
                                                    int(d[2]), int(ep[0]), int(ep[1]), int(ep[2]))

                    if i:
                        # check whether there is a jump in the observation epochs and whether this is the last epoch
                        if (epoch - epoch0) != resolution/60 or i == len(param[station]['vtec'][:,0]) - 1:                         

                            # append the index to the list of indices & the epoch to the list of epochs if it's the last epoch
                            if  i == len(param[station]['vtec'][:,0]) - 1:
                                indx.append(i)
                                epochs.append(epoch)
                                obsDTs.append(obsDateTime)
                                
                            # plot the VTECs from VLBI/VGOS
                            if error_bar:
                                plt.errorbar(obsDTs, param[station]['vtec'][indx,2].astype(float), 
                                             yerr = param[station]['vtec'][indx,3].astype(float), capsize=1.5,
                                             markeredgewidth=2, ls='-', c = 'forestgreen', alpha=1, barsabove=True, label = vlabel)
                                    
                            else:
                                plt.plot(obsDTs, param[station]['vtec'][indx,2].astype(float),
                                         c='forestgreen', ls='-', alpha=1, label = vlabel)

                            # plot the VTECs from GIMs
                            if gims:                                
                                if param[station]['vtec'][indx,4][0] not in '_':
                                    plt.plot(obsDTs, param[station]['vtec'][indx,4].astype(float),
                                             c='deepskyblue', ls='-', alpha=1, label = 'GIMs')

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
                                    
                                    # get the epochs
                                    madrx = [datetime.datetime(2000+int(session[:2]),m2n[session[2:5]],int(session[5:7]), 0, 0) 
                                             + datetime.timedelta(hours=i) 
                                             for i in madr[station][sindx:eindx,0]]
                                    
                                    # plot the original and smoothed Madrigal VTECs
                                    plt.plot(madrx, madr[station][sindx:eindx,1], c='0.75', ls='dotted',  label = 'MTMs')
                                    plt.plot(madrx, madr[station][sindx:eindx,2], '-y', label = 'SMTMs')

                            # reset the epochs and indices
                            indx = []
                            epochs = []
                            obsDTs = []

                    # append  the index to the list of indices and the epoch to the list of epochs
                    indx.append(i)
                    epochs.append(epoch) 
                    obsDTs.append(obsDateTime)

                    # save the epoch
                    epoch0 = epoch                      

                # write down the rms w.r.t. GIMs and SMTMs
                ax = plt.gca()

    
                # add a title and some labels
                plt.xlabel('UTC')
                plt.ylabel('VTEC (TECU)')
                plt.ylim() 
                plt.xlim()

                plt.legend(ncol = 1, fancybox=True) 
                

                # show the background grid
                plt.grid(c='0.2', linewidth=0.1)

                # adjust the format of its x-axis labels
                date_form = matplotlib.dates.DateFormatter("%Y-%m-%d %H:%M")
                ax.xaxis.set_major_formatter(date_form)
                ax.xaxis.set_major_locator(matplotlib.dates.HourLocator(interval=2))
                # set the format of the y-axis labels
                ax.yaxis.set_major_formatter(matplotlib.ticker.FormatStrFormatter('%.1f'))
                

                # get the current figure and automatically adjust the labels
                fig = plt.gcf()
                fig.autofmt_xdate()

                # rotate the labels
                plt.xticks(rotation=45)       
                
                # set the background colour
                ax.set_facecolor('xkcd:white')
                fig.patch.set_facecolor('xkcd:white')
                
                # create the following path if it doesn't exist
                path = os.path.join(v_output_path + str(2000+int(session[:2])) + '/' + session + '/') #  'VTEC Time Series/' #
                if not os.path.exists(path):
                    os.makedirs(path)

                # save the plot
                plt.savefig(os.path.join(path + f'{station}_on_{session}.{plot_format}'),bbox_inches='tight', dpi=1000)

                # close all the figures
                plt.close('all')
    
    
    @classmethod
    def save_results(cls, logger, param, session, gradient, madrigal, gims, v_output_path = 'Results/VGOS/'):

        '''This function saves the estimated parameters in a text file.'''

        # extract the year 
        year = 2000 + int(session[0:2])
        path = os.path.join(v_output_path + str(year) + '/' + session + '/')
        # create the path if missing
        if not os.path.exists(path):
            os.makedirs(path)

        # open a text file   
        with open(path + session +'.txt','w') as file: # 'n' for new

            # write the header
            if 'VG' in session:
                file.write('{0:^9}'.format('station') + '{0:^12}'.format('date') + '{0:^10}'.format('epoch') +
                                  '{0:^9}'.format('vgos_vtec') + '{0:^14}'.format('v_vtec_sigma') + '{0:^11}'.format('gims_vtec') +
                                  '{0:^11}'.format('madr_vtec') + '\n')
            elif 'XA' in session or 'XB' in session:
                file.write('{0:^9}'.format('station') + '{0:^12}'.format('date') + '{0:^10}'.format('epoch') +
                                  '{0:^9}'.format('vlbi_vtec') + '{0:^14}'.format('v_vtec_sigma') + '{0:^11}'.format('gims_vtec') +
                                  '{0:^11}'.format('madr_vtec') + '\n')

            for station in param.keys():
                for item in param[station]['vtec'][:]:
                    file.write('{0:^9}'.format(station) + '{0:^12}'.format(item[0]) + '{0:^10}'.format(item[1]) +
                                      '{0:^9}'.format(item[2]) + '{0:^14}'.format(item[3]) + '{0:^11}'.format(item[4]) +
                                      '{0:^11}'.format(item[5]) + '\n')

            file.write('\n')    

            # append the VTEC bias w.r.t. GIMs and SMTMs to the file
            v_bias = v_analysis.v_analysis.v_gims_mtms_bias(logger, param)
            file.write('{0:^9}'.format('station') + '{0:^20}'.format('bias w.r.t. GIMs') +
                              '{0:^20}'.format('bias w.r.t. SMTMs') +  '\n')

            for station in param.keys():
                if v_bias['gims']['rms'][station] and v_bias['mtms']['rms'][station]:
                    file.write('{0:^9}'.format(station) + '{0:^20}'.format(v_bias['gims']['rms'][station]) + 
                                      '{0:^20}'.format(v_bias['mtms']['rms'][station]) + '\n')

            file.write('\n')

            if gradient:
                # two gradients: Gn and Gn
                # append the ionospheric gradients to the file
                file.write('{0:^9}'.format('station') + '{0:^12}'.format('date') + '{0:^9}'.format('Gn') +
                                  '{0:^10}'.format('Gn_sigma') + '{0:^9}'.format('Gs') + 
                                  '{0:^10}'.format('Gs_sigma') + '\n')
                for station in param.keys():
                    item = param[station]['iono_grad'][:]
                    file.write('{0:^9}'.format(station) + '{0:^12}'.format(item[0]) + '{0:^9}'.format(item[1]) +
                                  '{0:^10}'.format(item[2]) + '{0:^9}'.format(item[3]) + 
                                  '{0:^10}'.format(item[4]) + '\n')

            else:
                # one gradient: Gns
                # append the ionospheric gradients to the file
                file.write('{0:^9}'.format('station') + '{0:^12}'.format('date') + '{0:^9}'.format('Gns') +
                                  '{0:^11}'.format('Gns_sigma') +  '\n')
                for station in param.keys():
                    item = param[station]['iono_grad'][:]
                    file.write('{0:^9}'.format(station) + '{0:^12}'.format(item[0]) + '{0:^9}'.format(item[1]) +
                                      '{0:^11}'.format(item[2]) + '\n')

            file.write('\n')

            # append the instrumental offsets to the file
            file.write('{0:^9}'.format('station') + '{0:^12}'.format('date') + '{0:^14}'.format('instr_offset') +
                              '{0:^10}'.format('io_sigma') +  '\n')
            for station in param.keys():
                item = param[station]['instr_offset'][:]
                file.write('{0:^9}'.format(station) + '{0:^12}'.format(item[0]) + '{0:^14}'.format(item[1]) +
                                  '{0:^10}'.format(item[2]) + '\n')

        file.close()
    

    @classmethod
    def v_read_file(cls, logger, session, v_output_path = 'Results/VGOS/'):

        '''This function reads the file of the estimated parameters.'''

        # get VLBI/VGOS-derived VTEC
        with open(os.path.join(v_output_path + str(2000+int(session[:2])) + '/' + session + '/' + session + '.txt'), 'r') as file:
            file_content = file.read().split('station')

            # get the stations
            stations = list(sorted(set([line.split()[0] for line in file_content[1].split('\n')[1:-2]])))

            # create a dictionary for different types of data in the text file
            param = {station: {'vtec': [], 'iono_grad':[], 'instr_offset': []} for station in stations}

            # keep track of lines per station
            l2s_list = []
            for line in file_content[1].split('\n')[1:-2]:
                items = line.split()
                if items[0] in l2s_list:
                    param[items[0]]['vtec'] = np.row_stack((param[items[0]]['vtec'],items[1:])).astype('str')
                else:
                    param[items[0]]['vtec'] = items[1:]
                l2s_list = list(set(l2s_list + [items[0]]))

            # keep track of lines per station
            l2s_list = []
            for line in file_content[3].split('\n')[1:-2]:
                items = line.split()
                if items[0] in l2s_list:
                    param[items[0]]['iono_grad'] = np.row_stack((param[items[0]]['iono_grad'],items[1:])).astype('str')
                else:
                    param[items[0]]['iono_grad'] = items[1:]
                l2s_list = list(set(l2s_list + [items[0]]))

            # keep track of lines per station
            l2s_list = []
            for line in file_content[4].split('\n')[1:-1]:
                items = line.split()
                if items[0] in l2s_list:
                    param[items[0]]['instr_offset'] = np.row_stack((param[items[0]]['instr_offset'],items[1:])).astype('str')
                else:
                    param[items[0]]['instr_offset'] = items[1:]
                l2s_list = list(set(l2s_list + [items[0]]))
                
        file.close()

        return param
    