
import os
import re
import csv
import shutil

import numpy as np
import statistics
import math
import random

import matplotlib.pylab as plt
import matplotlib
matplotlib.use('Agg')
import datetime
import time

import scipy


class v_analysis:
    
    def __ini__(self):
        pass

    
    @classmethod
    def v_gims_mtms_bias(cls, logger, pps): 

        '''This function calculates the VTEC bias of VLBI/VGOS w.r.t. to GIMS and MTMs per session.'''
        # get the stations
        stations = list(pps.keys())

        # define the dict for VLBI/VGOS bias w.r.t. GIMs and Madr
        v_bias = {'gims':{'rms':{}, 'mean':{}}, 'mtms':{'rms':{}, 'mean':{}}}

        # get the bias per station
        for i, station in enumerate(stations):
            
            # get the b
            if pps[station]['vtec'][0,4] not in '_':
                diff = abs(pps[station]['vtec'][:,4].astype(float) - pps[station]['vtec'][:,2].astype(float))
                v_bias['gims']['rms'][station] = str(round(np.sqrt(np.mean(diff**2)),3))
                v_bias['gims']['mean'][station] = str(round(np.mean(diff),3))
            else:
                v_bias['gims']['rms'][station] = ''
                v_bias['gims']['mean'][station] = ''

            
            if pps[station]['vtec'][0,5] not in '_':
                diff = abs(pps[station]['vtec'][:,5].astype(float) - pps[station]['vtec'][:,2].astype(float))
                v_bias['mtms']['rms'][station] = str(round(np.sqrt(np.mean(diff**2)),3))
                v_bias['mtms']['mean'][station] = str(round(np.mean(diff),3))
            else:
                v_bias['mtms']['rms'][station] = ''
                v_bias['mtms']['mean'][station] = ''

        return v_bias
    
    
    @classmethod
    def summarise_sessions(cls, logger, param):

        '''This function summarises the estimated parameters per session for further analysis.'''

        # print and plot the VLBI/VGOS biases w.r.t GIMs and Madr, VLBI/VGOS instrumental offsets, and VLBI/VGOS uncertainty

        # get VGOS bias w.r.t. GIMs and madrigal TEC maps per session               
        v_bias = {}
        for session in param.keys():
            v_bias[session] = cls.v_gims_mtms_bias(logger, param[session])

        # get all VLBI/VGOS stations in these sessions
        vgos_stations = []
        vlbi_stations = []
        for session in  param.keys():
            if 'VG' in session:
                vgos_stations = list(sorted(set(vgos_stations+list(param[session].keys()))))
            elif 'XA' or 'XB' in session:
                vlbi_stations = list(sorted(set(vlbi_stations+list(param[session].keys()))))

        # get the session information per station
        vgos_sPs = {}
        vlbi_sPs = {}
        # loop over the sessions
        for session in param.keys():
            # handle VGOS sessions
            if 'VG' in session:
                vgos_sPs[session] = {}
                # loop over the stations
                for i, station in enumerate(param[session].keys()):
                    indx = vgos_stations.index(station)
                    vgos_sPs[session][indx] = {}
                    # get the VTEC bias w.r.t. GIMs
                    if v_bias[session]['gims']['rms'][station]:
                        vgos_sPs[session][indx]['gims'] = str(round(float(v_bias[session]['gims']['rms'][station]),3))
                    else:
                        vgos_sPs[session][indx]['gims'] = ''

                    # get the VTEC Bias w.r.t. SMTMs
                    if v_bias[session]['mtms']['rms'][station]:
                        vgos_sPs[session][indx]['mtms'] = str(round(float(v_bias[session]['mtms']['rms'][station]),3))
                    else:
                        vgos_sPs[session][indx]['mtms'] = ''

                    # get the instrumental offset, gradients and VTEC uncertainties
                    vgos_sPs[session][indx]['instr_offset'] = param[session][station]['instr_offset'][1:3] 
                    vgos_sPs[session][indx]['iono_grad'] = param[session][station]['iono_grad'][1:]
                    vgos_sPs[session][indx]['vtec_std'] = param[session][station]['vtec'][:,3]

            # handle VLBI sessions
            elif 'XA' or 'XB' in session:
                vlbi_sPs[session] = {} 
                # loop over the stations
                for i, station in enumerate(param[session].keys()):
                    indx = vlbi_stations.index(station)
                    vlbi_sPs[session][indx] = {}
                    # get the VTEC Bias w.r.t. GIMs
                    if v_bias[session]['gims']['rms'][station]:
                        vlbi_sPs[session][indx]['gims'] = str(round(float(v_bias[session]['gims']['rms'][station]),3))
                    else:
                        vlbi_sPs[session][indx]['gims'] = ''

                    # get the VTEC Bias w.r.t. SMTMs
                    if v_bias[session]['mtms']['rms'][station]:
                        vlbi_sPs[session][indx]['mtms'] = str(round(float(v_bias[session]['mtms']['rms'][station]),3))
                    else:
                        vlbi_sPs[session][indx]['mtms'] = ''

                    # get the instrumental offset, gradients and VTEC uncertainties
                    vlbi_sPs[session][indx]['instr_offset'] = param[session][station]['instr_offset'][1:3] 
                    vlbi_sPs[session][indx]['iono_grad'] = param[session][station]['iono_grad'][1:]
                    vlbi_sPs[session][indx]['vtec_std'] = param[session][station]['vtec'][:,3]


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
    


    @classmethod
    def plot_vlbi_analysis_results(cls, logger, param, gradient = 1, plot_vb = 1, plot_io = 1, plot_g = 1, plot_unc = 1,
                                   v_output_path = '', ylim_bias = 10, ylim_instr = 10, ylim_grad = 0.18, ylim_unc = 0.5, 
                                   plot_format = 'png'):

        '''This function plots the VTEC biases for VLBI stations w.r.t. GIMs and SMTMs. It also plots the ionospheric gradients, 
        instrumental offsets, and uncertainties of VTEC time series for all processed sessions per station.'''

        # get the path
        if v_output_path:  
            v_output_path = os.path.join(v_output_path + 'Results/VLBI/')
        else:
            v_output_path = os.path.join('Results/VLBI/')


        ###
        # get the summary of all the sessions
        vgos_stations, vlbi_stations, svgkey, svlkey, vlbi_sPs, vlbi_sPs = cls.summarise_sessions(logger, param)    

        ### plot the summary

        # create a figure  
        # %matplotlib notebook
        plt.rcParams["figure.figsize"] = (10,4)
        # adjust the linewidth
        plt.rcParams['lines.linewidth'] = 2
        plt.rcParams['axes.linewidth'] = 1.5
        # adjust the font
        plt.rcParams.update({'font.size': 10})

        # get the dates of the first and last sesssions
        keys = sorted(svlkey.keys())
        sDate = datetime.datetime.strptime(str(keys[0][0])+str(keys[0][1])+str(keys[0][2]),"%y%m%d").date() 
        eDate = datetime.datetime.strptime(str(keys[-1][0])+str(keys[-1][1])+str(keys[-1][2]),"%y%m%d").date()

        if plot_vb:

            # clear the directory if exist. Otherwise, create it
            path = os.path.join(v_output_path + 'Inter-technique Biases/')
            if os.path.exists(path):            
                shutil.rmtree(path)
                os.makedirs(path)
            else:
                os.makedirs(path)
                
            
            # plot the biases per station
            for indx, station in enumerate(vlbi_stations):   
                try:
                    # get the dates to be plotted on the x-axis
                    xGIMs = [datetime.datetime.strptime(str(key[0])+ '/'+str(key[1])+'/'+str(key[2]),"%y/%m/%d").date() 
                             for i, key in enumerate(sorted(svlkey.keys()))
                             if indx in vlbi_sPs[svlkey[key]].keys() and vlbi_sPs[svlkey[key]][indx]['gims']]

                    xMadr = [datetime.datetime.strptime(str(key[0])+ '/'+str(key[1])+'/'+str(key[2]),"%y/%m/%d").date() 
                             for i, key in enumerate(sorted(svlkey.keys()))
                             if indx in vlbi_sPs[svlkey[key]].keys() and vlbi_sPs[svlkey[key]][indx]['mtms']]

                    # get the biases to be plotted on the y-axis
                    yGIMs =  [float(vlbi_sPs[svlkey[key]][indx]['gims']) 
                              for i, key in enumerate(sorted(svlkey.keys())) 
                              if indx in vlbi_sPs[svlkey[key]].keys() and vlbi_sPs[svlkey[key]][indx]['gims']]

                    
                    yMadr =  [float(vlbi_sPs[svlkey[key]][indx]['mtms']) 
                              for i, key in enumerate(sorted(svlkey.keys())) 
                              if indx in vlbi_sPs[svlkey[key]].keys() and vlbi_sPs[svlkey[key]][indx]['mtms']]
                    
                                        
                    # plot the biases as histogram
                    if xGIMs:
                        plt.hist(yGIMs, bins=np.arange(0,max(yGIMs), 0.2), edgecolor='black', linewidth=0.5,
                                 color='purple', label = f'VTEC RMS of {station} w.r.t. GIMs')
                    if xMadr:
                        plt.hist(yMadr, bins=np.arange(0,max(yMadr), 0.2), edgecolor='black', linewidth=0.5,
                                 color='y', alpha = 0.8, label = f'VTEC RMS of {station} w.r.t. SMTMs')  
                        
                    if xGIMs or xMadr:
                        
                        plt.xlabel('VTEC RMS (TECU)')
                        plt.ylabel('Frequency')
                        plt.legend()
                        plt.grid(c='0.2', linewidth=0.1)
                        plt.savefig(os.path.join(path + f'{station}_hist.{plot_format}'), bbox_inches='tight', dpi=1000)
                    
                    # clear the figure    
                    plt.clf()                    

                    # plot the biases as bars
                    if xGIMs:
                        plt.bar(xGIMs, yGIMs, width=6, color='purple', 
                                align='center', label = f'VTEC RMS of {station} w.r.t. GIMs')
                    if xMadr:
                        plt.bar(xMadr, yMadr, width=6, color='y', 
                                align='center', alpha = 0.8, label = f'VTEC RMS of {station} w.r.t. SMTMs')
                        
                    # display the value of the bars that exceed the limits on the y-axis  
                    for i, v in enumerate(yGIMs):
                        if yMadr[i] > ylim_bias and yGIMs[i] > ylim_bias: 
                            ax.text(xGIMs[i] + datetime.timedelta(days=7), ylim_bias - 1.5, 
                                    f'{ylim_bias}.0+', color='k', ha='left', rotation='vertical')
                            break

                        elif yMadr[i] > ylim_bias: 
                            ax.text(xMadr[i] + datetime.timedelta(days=7), 3.5, 
                                    f'{ylim_bias}.0+', color='y', ha='right', rotation='vertical') 
                            break
                            
                        elif yGIMs[i] > ylim_bias: 
                            ax.text(xGIMs[i] + datetime.timedelta(days=7), ylim_bias - 3.5,
                                    f'{ylim_bias}.0+', color='purple', ha='left', rotation='vertical')
                            break

                    # add some labels
                    # plt.xlabel('Session Date')
                    plt.ylabel('VTEC RMS (TECU)')
                    plt.xlim(sDate - datetime.timedelta(days=15), eDate + datetime.timedelta(days=15)) # adjust the dates dynamically
                    plt.ylim(0,ylim_bias)

                    plt.xlabel('Session Date')

                    # get the axises of the current figure 
                    ax = plt.gca()
                    # adjust the format of its x-axis labels
                    date_form = matplotlib.dates.DateFormatter("%Y-%m-%d")
                    ax.xaxis.set_major_formatter(date_form)
                    ax.xaxis.set_major_locator(matplotlib.dates.MonthLocator(interval=2))
                    # set the format of the y-axis labels
                    ax.yaxis.set_major_formatter(matplotlib.ticker.FormatStrFormatter('%.1f'))

                    # draw the median of the biases as a horizontal line and write the value on top of it
                    # draw a horizontal line at the medain value                    
                    xPos = sDate + datetime.timedelta(days=(eDate - sDate).days/12) 

                    if xGIMs:
                        ax.axhline(np.median(yGIMs), color='purple', linewidth=1, alpha = 0.6)
                        ax.text(xPos, np.median(yGIMs)+0.1, 'median RMS = ' + str(round(np.median(yGIMs),2)).rjust(3,'0').ljust(4,'0') +
                                ' $\pm$ '+ str(round(scipy.stats.median_abs_deviation(yGIMs),2)).rjust(3,'0').ljust(4,'0'), 
                                color="purple", va="bottom", fontsize=9)
                    if xMadr:
                        ax.axhline(np.median(yMadr), color='y', linewidth=1, alpha = 0.6)
                        ax.text(xPos, np.median(yMadr)-0.2, 'median RMS = ' + str(round(np.median(yMadr),2)).rjust(3,'0').ljust(4,'0') + 
                                ' $\pm$ '+ str(round(scipy.stats.median_abs_deviation(yMadr),2)).rjust(3,'0').ljust(4,'0'), 
                                color="y", va="top", fontsize=9)


                    # make a legend for both plots
                    if xGIMs or xMadr:
                        leg = plt.legend(loc='upper left', bbox_to_anchor=(0.02,1))

                    # get the current figure and automatically adjust the labels
                    fig = plt.gcf()
                    fig.autofmt_xdate()

                    # rotate the labels
                    plt.xticks(rotation=45)

                    # set the background colour
                    ax.set_facecolor('xkcd:white')
                    fig.patch.set_facecolor('xkcd:white')

                    # show the background grid
                    plt.grid(c='0.2', linewidth=0.1)

                    # create the output path if it doesn't exist
                    path = os.path.join(v_output_path + 'Inter-technique Biases/')
                    if not os.path.exists(path):
                        os.makedirs(path)

                    # save the figure
                    if xGIMs or xMadr:
                        plt.savefig(os.path.join(path + f'{station}_bar.{plot_format}'), bbox_inches='tight', dpi=1000)

                    # clear the figure
                    plt.clf()
            
                except Exception as e:
                    # close the figure
                    plt.close('all')
                    
                    logger.error(f'failed to plot the RMS differences of station {station}')
                    logger.debug(e)

        if plot_io:

            # clear the directory if exist. Otherwise, create it
            path = os.path.join(v_output_path + 'Instrumental Offsets/')
            if os.path.exists(path):
                shutil.rmtree(path)
                os.makedirs(path)
            else:
                os.makedirs(path)

            # plot instrumental offsets per station for all sessions
            for indx, station in enumerate(vlbi_stations):
                try:

                    # get the dates to be plotted on the x-axis
                    x = [datetime.datetime.strptime(str(key[0])+ '/'+str(key[1])+'/'+str(key[2]),"%y/%m/%d").date() 
                         for i, key in enumerate(sorted(svlkey.keys())) if indx in vlbi_sPs[svlkey[key]].keys()]

                    # get the offsets and their errors to be plotted on the y-axis
                    y =  [float(vlbi_sPs[svlkey[key]][indx]['instr_offset'][0]) 
                          for i, key in enumerate(sorted(svlkey.keys())) if indx in vlbi_sPs[svlkey[key]].keys()]

                    yerror =  [float(vlbi_sPs[svlkey[key]][indx]['instr_offset'][1]) 
                               for i, key in enumerate(sorted(svlkey.keys())) if indx in vlbi_sPs[svlkey[key]].keys()]

                    # plot the offsets as bars with errorbars
                    plt.bar(x, y, yerr=yerror, error_kw=dict(lw=0.8, capsize=1, capthick=0.7),
                            width=6, color='purple', align='center', label = f'instrumental offset of {station}')
                    
                    # display the value of the bar
                    for i, v in enumerate(y):
                        if v > ylim_instr:
                            ax.text(x[i] - datetime.timedelta(days=7), 3.5,
                                    f'{ylim_grad}.0+', color='k', ha='right', rotation='vertical')
                            break
                    
                    for i, v in enumerate(y):
                        if v < -ylim_instr:
                            ax.text(x[i] - datetime.timedelta(days=7), -9.5,
                                    f'{ylim_grad}.0+', color='k', ha='right', rotation='vertical')
                            break

                    # add some labels
                    plt.xlabel('Session Date')
                    plt.ylabel('Instr. Offsets (TECU)')
                    plt.xlim(sDate - datetime.timedelta(days=15), eDate + datetime.timedelta(days=15))
                    plt.ylim(-ylim_instr,ylim_instr)


                    # get the axises of the current figure 
                    ax = plt.gca()
                    # adjust the format of its x-axis labels
                    date_form = matplotlib.dates.DateFormatter("%Y-%m-%d")
                    ax.xaxis.set_major_formatter(date_form)
                    ax.xaxis.set_major_locator(matplotlib.dates.MonthLocator(interval=2))
                    # set the format of the y-axis labels
                    ax.yaxis.set_major_formatter(matplotlib.ticker.FormatStrFormatter('%.1f'))


                    # make a legend for both plots
                    leg = plt.legend(loc='upper left', bbox_to_anchor=(0.02,1))

                    # get the current figure and automatically adjust the labels
                    fig = plt.gcf()
                    fig.autofmt_xdate()

                    # rotate the labels
                    plt.xticks(rotation=45)

                    # set the background colour
                    ax.set_facecolor('xkcd:white')
                    fig.patch.set_facecolor('xkcd:white')

                    # show the background grid
                    plt.grid(c='0.2', linewidth=0.1)

                    # save the figure
                    plt.savefig(os.path.join(path + f'{station}.{plot_format}'), bbox_inches='tight', dpi=1000)

                    # clear the figure
                    plt.clf()
            
                except Exception as e:
                    # clear the figure
                    plt.clf()
                    
                    logger.error(f'failed to plot the instrumental offsets for station {station}')
                    logger.debug(e)
            


        if plot_g:

            # clear the directory if exist. Otherwise, create it.
            path = os.path.join(v_output_path + 'Gradients/')
            if os.path.exists(path):
                shutil.rmtree(path)
                os.makedirs(path)
            else:
                os.makedirs(path)

            # plot the gradients per station
            for indx, station in enumerate(vlbi_stations):      
                
                try:

                    # get the dates to be plotted on the x-axis
                    x = [datetime.datetime.strptime(str(key[0])+ '/'+str(key[1])+'/'+str(key[2]),"%y/%m/%d").date() 
                     for i, key in enumerate(sorted(svlkey.keys())) if indx in vlbi_sPs[svlkey[key]].keys()]
                    
                    if gradient:

                        # get the gradients to be plotted on the y-axis
                        Gn =  [float(vlbi_sPs[svlkey[key]][indx]['iono_grad'][0])*np.pi/180
                               for i, key in enumerate(sorted(svlkey.keys())) if indx in vlbi_sPs[svlkey[key]].keys()]

                        Gs =  [float(vlbi_sPs[svlkey[key]][indx]['iono_grad'][2])*np.pi/180
                               for i, key in enumerate(sorted(svlkey.keys())) if indx in vlbi_sPs[svlkey[key]].keys()]

                        # get the quality of the north and south gradients
                        qGn =  [float(vlbi_sPs[svlkey[key]][indx]['iono_grad'][1])*np.pi/180
                                for i, key in enumerate(sorted(svlkey.keys())) if indx in vlbi_sPs[svlkey[key]].keys()]

                        qGs =  [float(vlbi_sPs[svlkey[key]][indx]['iono_grad'][3])*np.pi/180
                                for i, key in enumerate(sorted(svlkey.keys())) if indx in vlbi_sPs[svlkey[key]].keys()]


                        # plot the biases as bars
                        plt.bar(x, Gn, yerr=qGn, error_kw=dict(lw=0.8, capsize=1, capthick=0.7),
                                width=6, color='purple', align='center', label = f'north gradient of {station}')
                        plt.bar(x, Gs, yerr=qGs, error_kw=dict(lw=0.8, capsize=1, capthick=0.7),
                                width=6, color='y', align='center', alpha = 0.8, label = f'south gradient of {station}')
                        
                        # display the value of the bars that exceed the limits on the y-axis  
                        for i, v in enumerate(Gn):
                            if v > ylim_grad and not indx:           
                                ax.text(x[i] - datetime.timedelta(days=7), ylim_grad - 0.05,
                                        f'{ylim_grad}+', color='purple', ha='right', rotation='vertical')
                                break
                        
                        for i, v in enumerate(Gs):
                            if v < -ylim_grad and not indx:           
                                ax.text(x[i] - datetime.timedelta(days=7), ylim_grad - 0.05,
                                        f'{ylim_grad}+', color='purple', ha='right', rotation='vertical')
                                break
                                
                    else:
                        
                        # get the gradients to be plotted on the y-axis
                        Gns =  [float(vlbi_sPs[svlkey[key]][indx]['iono_grad'][0])*np.pi/180
                                for i, key in enumerate(sorted(svlkey.keys())) if indx in vlbi_sPs[svlkey[key]].keys()]

                        # get the quality of the north and south gradients
                        qGns =  [float(vlbi_sPs[svlkey[key]][indx]['iono_grad'][1])*np.pi/180
                                 for i, key in enumerate(sorted(svlkey.keys())) if indx in vlbi_sPs[svlkey[key]].keys()]
                        
                        # plot the biases as bars
                        plt.bar(x, Gns, yerr=qGns, error_kw=dict(lw=0.8, capsize=1, capthick=0.7),
                                width=6, color='purple', align='center', label = f'north/south gradient of {station}')
                        
                        # display the value of the bars that exceed the limits on the y-axis  
                        for i, v in enumerate(Gns):
                            if abs(v) > ylim_grad and not indx:           
                                ax.text(x[i] - datetime.timedelta(days=7), ylim_grad - 0.05,
                                        f'{ylim_grad}+', color='purple', ha='right', rotation='vertical')
                                break


                    # add some labels
                    plt.xlabel('Session Date')
                    plt.ylabel('Gradient (TECU/deg)')
                    plt.xlim(sDate - datetime.timedelta(days=15), eDate + datetime.timedelta(days=15)) # adjust the dates dynamically
                    plt.ylim(-ylim_grad,ylim_grad)


                    # get the axises of the current figure 
                    ax = plt.gca()
                    # adjust the format of its x-axis labels
                    date_form = matplotlib.dates.DateFormatter("%Y-%m-%d")
                    ax.xaxis.set_major_formatter(date_form)
                    ax.xaxis.set_major_locator(matplotlib.dates.MonthLocator(interval=2))
                    # set the format of the y-axis labels
                    ax.yaxis.set_major_formatter(matplotlib.ticker.FormatStrFormatter('%.3f'))


                    # make a legend for both plots
                    leg = plt.legend(loc='upper left', bbox_to_anchor=(0.02,1))

                    # get the current figure and automatically adjust the labels
                    fig = plt.gcf()
                    fig.autofmt_xdate()

                    # rotate the labels
                    plt.xticks(rotation=45)

                    # set the background colour
                    ax.set_facecolor('xkcd:white')
                    fig.patch.set_facecolor('xkcd:white')

                    # show the background grid
                    plt.grid(c='0.2', linewidth=0.1)

                    # save the figure
                    plt.savefig(os.path.join(path + f'{station}.{plot_format}'), bbox_inches='tight', dpi=1000)

                    # clear the figure
                    plt.clf()
            
                except Exception as e:
                    # clear the figure
                    plt.clf()
                    
                    logger.error(f'failed to plot the ionospheric gradients of station {station}')
                    logger.debug(e)


        if plot_unc:

            # clear the directory if exist. Otherwise, create it.
            path = os.path.join(v_output_path + 'VTECs_uncertainties/')
            if os.path.exists(path):
                shutil.rmtree(path)
                os.makedirs(path)
            else:
                os.makedirs(path)

            # plot vtec mean uncertainties per station
            for indx, station in enumerate(vlbi_stations):
                
                try:

                    # get the dates to be plotted on the x-axis
                    x = [datetime.datetime.strptime(str(key[0])+'/'+str(key[1])+'/'+str(key[2]),"%y/%m/%d").date() 
                         for i, key in enumerate(sorted(svlkey.keys())) if indx in vlbi_sPs[svlkey[key]].keys()]#[indx]]

                    # get the mean uncertainties to be plotted on the y-axis
                    y =  [round(np.median(vlbi_sPs[svlkey[key]][indx]['vtec_std'].astype(float)),2)
                          for i, key in enumerate(sorted(svlkey.keys())) if indx in vlbi_sPs[svlkey[key]].keys()]#[indx][indx][0]]
                    
                    
                    plt.hist(y, bins=np.arange(0,max(y),0.01), edgecolor='black', linewidth=0.5,
                             color='purple', label = f'VTEC uncertainty of {station}')
                    plt.xlabel('Sigma VTEC (TECU)')
                    plt.ylabel('Frequency')
                    plt.legend()
                    plt.grid(c='0.2', linewidth=0.1)
                    plt.savefig(os.path.join(path + f'{station}_hist.{plot_format}'), bbox_inches='tight', dpi=1000)
                    
                    # clear the figure
                    plt.clf()

                    # plot the biases as bars
                    plt.bar(x, y, width=6, color='purple', align='center', label = f'VTEC uncertainty of {station}')

                    # add some labels
                    # plt.xlabel('Session Date')
                    plt.ylabel(f'Sigma VTEC (TECU)')
                    plt.xlim(sDate - datetime.timedelta(days=15), eDate + datetime.timedelta(days=15)) # adjust the dates dynamically
                    plt.ylim(0,ylim_unc) 


                    # get the axises of the current figure 
                    ax = plt.gca()
                    # adjust the format of its x-axis labels
                    date_form = matplotlib.dates.DateFormatter("%Y-%m-%d")
                    ax.xaxis.set_major_formatter(date_form)
                    ax.xaxis.set_major_locator(matplotlib.dates.MonthLocator(interval=2))
                    # set the format of the y-axis labels
                    ax.yaxis.set_major_formatter(matplotlib.ticker.FormatStrFormatter('%.1f'))

                    # draw the mean of the biases as a horizontal line
                    ax.axhline(np.median(y), color='y', linewidth=1, alpha = 0.6)

                    # sDate + datetime.timedelta(days=(eDate - sDate).days/12) # datetime.date(2018,1,31) #
                    xPos =  sDate + datetime.timedelta(days=(eDate - sDate).days/12)
                    
                    ax.text(xPos, np.median(y)+0.02, 'median uncertainty = ' + str(round(np.median(y),2)).rjust(3,'0').ljust(4,'0') +
                            ' $\pm$ '+ str(round(scipy.stats.median_abs_deviation(y),2)).rjust(3,'0').ljust(4,'0'), 
                            color="y", va="bottom", fontsize=9)

                    # make a legend for both plots
                    leg = plt.legend(loc='upper left', bbox_to_anchor=(0.02,1))

                    # show the background grid
                    plt.grid(c='0.2', linewidth=0.1)

                    # get the current figure and automatically adjust the labels
                    fig = plt.gcf()
                    fig.autofmt_xdate()

                    # rotate the labels
                    plt.xticks(rotation=45)

                    # set the background colour
                    ax.set_facecolor('xkcd:white')
                    fig.patch.set_facecolor('xkcd:white')

                    # save the figure
                    plt.savefig(os.path.join(path + f'{station}_bar.{plot_format}'), bbox_inches='tight', dpi=1000)


                    # clear the figure
                    plt.clf()
            
                except Exception as e:
                    # clear the figure
                    plt.clf()
                    
                    logger.error(f'failed to plot the VTEC uncertainty of station {station}')
                    logger.debug(e)
                    

    @classmethod
    def plot_vgos_analysis_results(cls, logger, param, gradient = 1, plot_vb = 1, plot_io = 1, plot_g = 1, plot_unc = 1,
                                   v_output_path = '', ylim_bias = 10, ylim_instr = 10, ylim_grad = 0.18, ylim_unc = 0.5, 
                                   plot_format = 'png'):

        '''This function plots the VTEC biases for VGOS stations w.r.t. GIMs and SMTMs. It also plots the ionospheric gradients, 
        instrumental offsets, and uncertainties of VTEC time series for all processed sessions per station.'''

        # get the path
        if v_output_path:  
            v_output_path = os.path.join(v_output_path + 'Results/VGOS/')
        else:
            v_output_path = os.path.join('Results/VGOS/')


        ###
        # get the summary of all the sessions
        vgos_stations, vlbi_stations, svgkey, svlkey, vgos_sPs, vlbi_sPs = cls.summarise_sessions(logger, param)    

        ### plot the summary

        # create a figure  
        # %matplotlib notebook
        plt.rcParams["figure.figsize"] = (10,4)
        # adjust the linewidth
        plt.rcParams['lines.linewidth'] = 2
        plt.rcParams['axes.linewidth'] = 1.5
        # adjust the font
        plt.rcParams.update({'font.size': 10})

        # get the dates of the first and last sesssions
        keys = sorted(svgkey.keys())
        sDate = datetime.datetime.strptime(str(keys[0][0])+str(keys[0][1])+str(keys[0][2]),"%y%m%d").date() 
        eDate = datetime.datetime.strptime(str(keys[-1][0])+str(keys[-1][1])+str(keys[-1][2]),"%y%m%d").date()

        if plot_vb:

            # clear the directory if exist. Otherwise, create it
            path = os.path.join(v_output_path + 'Inter-technique Biases/')
            if os.path.exists(path):            
                shutil.rmtree(path)
                os.makedirs(path)
            else:
                os.makedirs(path)
                
            
            # plot the biases per station
            for indx, station in enumerate(vgos_stations):   
                try:
                    # get the dates to be plotted on the x-axis
                    xGIMs = [datetime.datetime.strptime(str(key[0])+ '/'+str(key[1])+'/'+str(key[2]),"%y/%m/%d").date() 
                             for i, key in enumerate(sorted(svgkey.keys()))
                             if indx in vgos_sPs[svgkey[key]].keys() and vgos_sPs[svgkey[key]][indx]['gims']]

                    xMadr = [datetime.datetime.strptime(str(key[0])+ '/'+str(key[1])+'/'+str(key[2]),"%y/%m/%d").date() 
                             for i, key in enumerate(sorted(svgkey.keys()))
                             if indx in vgos_sPs[svgkey[key]].keys() and vgos_sPs[svgkey[key]][indx]['mtms']]

                    # get the biases to be plotted on the y-axis
                    yGIMs =  [float(vgos_sPs[svgkey[key]][indx]['gims']) 
                              for i, key in enumerate(sorted(svgkey.keys())) 
                              if indx in vgos_sPs[svgkey[key]].keys() and vgos_sPs[svgkey[key]][indx]['gims']]

                    
                    yMadr =  [float(vgos_sPs[svgkey[key]][indx]['mtms']) 
                              for i, key in enumerate(sorted(svgkey.keys())) 
                              if indx in vgos_sPs[svgkey[key]].keys() and vgos_sPs[svgkey[key]][indx]['mtms']]
                    
                                        
                    # plot the biases as histogram
                    if xGIMs:
                        plt.hist(yGIMs, bins=np.arange(0,max(yGIMs), 0.2), edgecolor='black', linewidth=0.5,
                                 color='purple', label = f'VTEC RMS of {station} w.r.t. GIMs')
                    if xMadr:
                        plt.hist(yMadr, bins=np.arange(0,max(yMadr), 0.2), edgecolor='black', linewidth=0.5,
                                 color='y', alpha = 0.8, label = f'VTEC RMS of {station} w.r.t. SMTMs')  
                    if xGIMs or xMadr:
                        
                        plt.xlabel('VTEC RMS (TECU)')
                        plt.ylabel('Frequency')
                        plt.xlim()
                        plt.legend()
                        plt.grid(c='0.2', linewidth=0.1)
                        plt.savefig(os.path.join(path + f'{station}_hist.{plot_format}'), bbox_inches='tight', dpi=1000)
                    
                    # clear the figure    
                    plt.clf()                    

                    # plot the biases as bars
                    if xGIMs:
                        plt.bar(xGIMs, yGIMs, width=6, color='purple', 
                                align='center', label = f'VTEC RMS of {station} w.r.t. GIMs')
                    if xMadr:
                        plt.bar(xMadr, yMadr, width=6, color='y', 
                                align='center', alpha = 0.8, label = f'VTEC RMS of {station} w.r.t. SMTMs')

                    # display the value of the bars that exceed the limits on the y-axis  
                    for i, v in enumerate(yGIMs):
                        if yMadr[i] > ylim_bias and yGIMs[i] > ylim_bias: 
                            ax.text(xGIMs[i] + datetime.timedelta(days=7), ylim_bias - 1.5, 
                                    f'{ylim_bias}.0+', color='k', ha='left', rotation='vertical')
                            break

                        elif yMadr[i] > ylim_bias: 
                            ax.text(xMadr[i] + datetime.timedelta(days=7), 3.5, 
                                    f'{ylim_bias}.0+', color='y', ha='right', rotation='vertical') 
                            break
                            
                        elif yGIMs[i] > ylim_bias: 
                            ax.text(xGIMs[i] + datetime.timedelta(days=7), ylim_bias - 3.5,
                                    f'{ylim_bias}.0+', color='purple', ha='left', rotation='vertical')
                            break
                            
                    # add some labels
                    # plt.xlabel('Session Date')
                    plt.ylabel('VTEC RMS (TECU)')
                    plt.xlim(sDate - datetime.timedelta(days=15), eDate + datetime.timedelta(days=15)) # adjust the dates dynamically
                    plt.ylim(0,ylim_bias)

                    plt.xlabel('Session Date')

                    # get the axises of the current figure 
                    ax = plt.gca()
                    # adjust the format of its x-axis labels
                    date_form = matplotlib.dates.DateFormatter("%Y-%m-%d")
                    ax.xaxis.set_major_formatter(date_form)
                    ax.xaxis.set_major_locator(matplotlib.dates.MonthLocator(interval=2))
                    # set the format of the y-axis labels
                    ax.yaxis.set_major_formatter(matplotlib.ticker.FormatStrFormatter('%.1f'))

                    # draw the median of the biases as a horizontal line and write the value on top of it
                    # draw a horizontal line at the medain value                    
                    xPos = sDate + datetime.timedelta(days=(eDate - sDate).days/12) 

                    if xGIMs:
                        ax.axhline(np.median(yGIMs), color='purple', linewidth=1, alpha = 0.6)
                        ax.text(xPos, np.median(yGIMs)+0.1, 'median RMS = ' + str(round(np.median(yGIMs),2)).rjust(3,'0').ljust(4,'0') +
                                ' $\pm$ '+ str(round(scipy.stats.median_abs_deviation(yGIMs),2)).rjust(3,'0').ljust(4,'0'), 
                                color="purple", va="bottom", fontsize=9)
                    if xMadr:
                        ax.axhline(np.median(yMadr), color='y', linewidth=1, alpha = 0.6)
                        ax.text(xPos, np.median(yMadr)-0.2, 'median RMS = ' + str(round(np.median(yMadr),2)).rjust(3,'0').ljust(4,'0') + 
                                ' $\pm$ '+ str(round(scipy.stats.median_abs_deviation(yMadr),2)).rjust(3,'0').ljust(4,'0'), 
                                color="y", va="top", fontsize=9)


                    # make a legend for both plots
                    if xGIMs or xMadr:
                        leg = plt.legend(loc='upper left', bbox_to_anchor=(0.02,1))

                    # get the current figure and automatically adjust the labels
                    fig = plt.gcf()
                    fig.autofmt_xdate()

                    # rotate the labels
                    plt.xticks(rotation=45)

                    # set the background colour
                    ax.set_facecolor('xkcd:white')
                    fig.patch.set_facecolor('xkcd:white')

                    # show the background grid
                    plt.grid(c='0.2', linewidth=0.1)

                    # create the output path if it doesn't exist
                    path = os.path.join(v_output_path + 'Inter-technique Biases/')
                    if not os.path.exists(path):
                        os.makedirs(path)

                    # save the figure
                    if xGIMs or xMadr:
                        plt.savefig(os.path.join(path + f'{station}_bar.{plot_format}'), bbox_inches='tight', dpi=1000)

                    # clear the figure
                    plt.clf()
            
                except Exception as e:
                    # close the figure
                    plt.close('all')
                    
                    logger.error(f'failed to plot the RMS differences of station {station}')
                    logger.debug(e)

        if plot_io:

            # clear the directory if exist. Otherwise, create it
            path = os.path.join(v_output_path + 'Instrumental Offsets/')
            if os.path.exists(path):
                shutil.rmtree(path)
                os.makedirs(path)
            else:
                os.makedirs(path)

            # plot instrumental offsets per station for all sessions
            for indx, station in enumerate(vgos_stations):
                try:

                    # get the dates to be plotted on the x-axis
                    x = [datetime.datetime.strptime(str(key[0])+ '/'+str(key[1])+'/'+str(key[2]),"%y/%m/%d").date() 
                         for i, key in enumerate(sorted(svgkey.keys())) if indx in vgos_sPs[svgkey[key]].keys()]

                    # get the offsets and their errors to be plotted on the y-axis
                    y =  [float(vgos_sPs[svgkey[key]][indx]['instr_offset'][0]) 
                          for i, key in enumerate(sorted(svgkey.keys())) if indx in vgos_sPs[svgkey[key]].keys()]

                    yerror =  [float(vgos_sPs[svgkey[key]][indx]['instr_offset'][1]) 
                               for i, key in enumerate(sorted(svgkey.keys())) if indx in vgos_sPs[svgkey[key]].keys()]

                    # plot the offsets as bars with errorbars
                    plt.bar(x, y, yerr=yerror, error_kw=dict(lw=0.8, capsize=1, capthick=0.7),
                            width=6, color='purple', align='center', label = f'instrumental offset of {station}')
                    
                    # display the value of the bar
                    for i, v in enumerate(y):
                        if v > ylim_instr:
                            ax.text(x[i] - datetime.timedelta(days=7), 3.5,
                                    f'{ylim_grad}.0+', color='k', ha='right', rotation='vertical')
                            break
                    
                    for i, v in enumerate(y):
                        if v < -ylim_instr:
                            ax.text(x[i] - datetime.timedelta(days=7), -9.5,
                                    f'{ylim_grad}.0+', color='k', ha='right', rotation='vertical')
                            break

                    # add some labels
                    plt.xlabel('Session Date')
                    plt.ylabel('Instr. Offsets (TECU)')
                    plt.xlim(sDate - datetime.timedelta(days=15), eDate + datetime.timedelta(days=15))
                    plt.ylim(-ylim_instr,ylim_instr)


                    # get the axises of the current figure 
                    ax = plt.gca()
                    # adjust the format of its x-axis labels
                    date_form = matplotlib.dates.DateFormatter("%Y-%m-%d")
                    ax.xaxis.set_major_formatter(date_form)
                    ax.xaxis.set_major_locator(matplotlib.dates.MonthLocator(interval=2))
                    # set the format of the y-axis labels
                    ax.yaxis.set_major_formatter(matplotlib.ticker.FormatStrFormatter('%.1f'))


                    # make a legend for both plots
                    leg = plt.legend(loc='upper left', bbox_to_anchor=(0.02,1))

                    # get the current figure and automatically adjust the labels
                    fig = plt.gcf()
                    fig.autofmt_xdate()

                    # rotate the labels
                    plt.xticks(rotation=45)

                    # set the background colour
                    ax.set_facecolor('xkcd:white')
                    fig.patch.set_facecolor('xkcd:white')

                    # show the background grid
                    plt.grid(c='0.2', linewidth=0.1)

                    # save the figure
                    plt.savefig(os.path.join(path + f'{station}.{plot_format}'), bbox_inches='tight', dpi=1000)

                    # clear the figure
                    plt.clf()
            
                except Exception as e:
                    # clear the figure
                    plt.clf()
                    
                    logger.error(f'failed to plot the instrumental offsets for station {station}')
                    logger.debug(e)
            


        if plot_g:

            # clear the directory if exist. Otherwise, create it.
            path = os.path.join(v_output_path + 'Gradients/')
            if os.path.exists(path):
                shutil.rmtree(path)
                os.makedirs(path)
            else:
                os.makedirs(path)

            # plot the gradients per station
            for indx, station in enumerate(vgos_stations):      
                
                try:

                    # get the dates to be plotted on the x-axis
                    x = [datetime.datetime.strptime(str(key[0])+ '/'+str(key[1])+'/'+str(key[2]),"%y/%m/%d").date() 
                     for i, key in enumerate(sorted(svgkey.keys())) if indx in vgos_sPs[svgkey[key]].keys()]
                    
                    if gradient:

                        # get the gradients to be plotted on the y-axis
                        Gn =  [float(vgos_sPs[svgkey[key]][indx]['iono_grad'][0])*np.pi/180
                               for i, key in enumerate(sorted(svgkey.keys())) if indx in vgos_sPs[svgkey[key]].keys()]

                        Gs =  [float(vgos_sPs[svgkey[key]][indx]['iono_grad'][2])*np.pi/180
                               for i, key in enumerate(sorted(svgkey.keys())) if indx in vgos_sPs[svgkey[key]].keys()]

                        # get the quality of the north and south gradients
                        qGn =  [float(vgos_sPs[svgkey[key]][indx]['iono_grad'][1])*np.pi/180
                                for i, key in enumerate(sorted(svgkey.keys())) if indx in vgos_sPs[svgkey[key]].keys()]

                        qGs =  [float(vgos_sPs[svgkey[key]][indx]['iono_grad'][3])*np.pi/180
                                for i, key in enumerate(sorted(svgkey.keys())) if indx in vgos_sPs[svgkey[key]].keys()]
                        
                        # plot the biases as bars
                        plt.bar(x, Gn, yerr=qGn, error_kw=dict(lw=0.8, capsize=1, capthick=0.7),
                                width=6, color='purple', align='center', label = f'north gradient of {station}')
                        plt.bar(x, Gs, yerr=qGs, error_kw=dict(lw=0.8, capsize=1, capthick=0.7),
                                width=6, color='y', align='center', alpha = 0.8, label = f'south gradient of {station}')
                        
                        # display the value of the bars that exceed the limits on the y-axis  
                        for i, v in enumerate(Gn):
                            if v > ylim_grad and not indx:           
                                ax.text(x[i] - datetime.timedelta(days=7), ylim_grad - 0.05,
                                        f'{ylim_grad}+', color='purple', ha='right', rotation='vertical')
                                break
                        
                        for i, v in enumerate(Gs):
                            if v < -ylim_grad and not indx:           
                                ax.text(x[i] - datetime.timedelta(days=7), ylim_grad - 0.05,
                                        f'{ylim_grad}+', color='purple', ha='right', rotation='vertical')
                                break
                                                        
                    else:
                        
                        # get the gradients to be plotted on the y-axis
                        Gns =  [float(vgos_sPs[svgkey[key]][indx]['iono_grad'][0])*np.pi/180
                                for i, key in enumerate(sorted(svgkey.keys())) if indx in vgos_sPs[svgkey[key]].keys()]

                        # get the quality of the north and south gradients
                        qGns =  [float(vgos_sPs[svgkey[key]][indx]['iono_grad'][1])*np.pi/180
                                 for i, key in enumerate(sorted(svgkey.keys())) if indx in vgos_sPs[svgkey[key]].keys()]                    

                        # plot the biases as bars
                        plt.bar(x, Gns, yerr=qGns, error_kw=dict(lw=0.8, capsize=1, capthick=0.7),
                                width=6, color='purple', align='center', label = f'north/south gradient of {station}')
                        
                        # display the value of the bars that exceed the limits on the y-axis  
                        for i, v in enumerate(Gns):
                            if abs(v) > ylim_grad and not indx:           
                                ax.text(x[i] - datetime.timedelta(days=7), ylim_grad - 0.05,
                                        f'{ylim_grad}+', color='purple', ha='right', rotation='vertical')
                                break

                    
                            
                    # add some labels
                    plt.xlabel('Session Date')
                    plt.ylabel('Gradient (TECU/deg)')
                    plt.xlim(sDate - datetime.timedelta(days=15), eDate + datetime.timedelta(days=15)) # adjust the dates dynamically
                    plt.ylim(-ylim_grad,ylim_grad)
                    
                    # get the axises of the current figure 
                    ax = plt.gca()
                    # adjust the format of its x-axis labels
                    date_form = matplotlib.dates.DateFormatter("%Y-%m-%d")
                    ax.xaxis.set_major_formatter(date_form)
                    ax.xaxis.set_major_locator(matplotlib.dates.MonthLocator(interval=2))
                    # set the format of the y-axis labels
                    ax.yaxis.set_major_formatter(matplotlib.ticker.FormatStrFormatter('%.3f'))


                    # make a legend for both plots
                    leg = plt.legend(loc='upper left', bbox_to_anchor=(0.02,1))

                    # get the current figure and automatically adjust the labels
                    fig = plt.gcf()
                    fig.autofmt_xdate()

                    # rotate the labels
                    plt.xticks(rotation=45)

                    # set the background colour
                    ax.set_facecolor('xkcd:white')
                    fig.patch.set_facecolor('xkcd:white')

                    # show the background grid
                    plt.grid(c='0.2', linewidth=0.1)

                    # save the figure
                    plt.savefig(os.path.join(path + f'{station}.{plot_format}'), bbox_inches='tight', dpi=1000)

                    # clear the figure
                    plt.clf()
            
                except Exception as e:
                    # clear the figure
                    plt.clf()
                    
                    logger.error(f'failed to plot the ionospheric gradients of station {station}')
                    logger.debug(e)


        if plot_unc:

            # clear the directory if exist. Otherwise, create it.
            path = os.path.join(v_output_path + 'VTECs_uncertainties/')
            if os.path.exists(path):
                shutil.rmtree(path)
                os.makedirs(path)
            else:
                os.makedirs(path)

            # plot vtec mean uncertainties per station
            for indx, station in enumerate(vgos_stations):
                
                try:

                    # get the dates to be plotted on the x-axis
                    x = [datetime.datetime.strptime(str(key[0])+'/'+str(key[1])+'/'+str(key[2]),"%y/%m/%d").date() 
                         for i, key in enumerate(sorted(svgkey.keys())) if indx in vgos_sPs[svgkey[key]].keys()]#[indx]]

                    # get the mean uncertainties to be plotted on the y-axis
                    y =  [round(np.median(vgos_sPs[svgkey[key]][indx]['vtec_std'].astype(float)),2)
                          for i, key in enumerate(sorted(svgkey.keys())) if indx in vgos_sPs[svgkey[key]].keys()]#[indx][indx][0]]
                    
                    
                    plt.hist(y, bins=np.arange(0,max(y),0.01), edgecolor='black', linewidth=0.5,
                             color='purple', label = f'VTEC uncertainty of {station}')
                    plt.xlabel('Sigma VTEC (TECU)')
                    plt.ylabel('Frequency')
                    plt.legend()
                    plt.grid(c='0.2', linewidth=0.1)
                    plt.savefig(os.path.join(path + f'{station}_hist.{plot_format}'), bbox_inches='tight', dpi=1000)
                    
                    # clear the figure
                    plt.clf()

                    # plot the biases as bars
                    plt.bar(x, y, width=6, color='purple', align='center', label = f'VTEC uncertainty of {station}')

                    # add some labels
                    # plt.xlabel('Session Date')
                    plt.ylabel(f'Sigma VTEC (TECU)')
                    plt.xlim(sDate - datetime.timedelta(days=15), eDate + datetime.timedelta(days=15)) # adjust the dates dynamically
                    plt.ylim(0,ylim_unc) 


                    # get the axises of the current figure 
                    ax = plt.gca()
                    # adjust the format of its x-axis labels
                    date_form = matplotlib.dates.DateFormatter("%Y-%m-%d")
                    ax.xaxis.set_major_formatter(date_form)
                    ax.xaxis.set_major_locator(matplotlib.dates.MonthLocator(interval=2))
                    # set the format of the y-axis labels
                    ax.yaxis.set_major_formatter(matplotlib.ticker.FormatStrFormatter('%.1f'))

                    # draw the mean of the biases as a horizontal line
                    ax.axhline(np.median(y), color='y', linewidth=1, alpha = 0.6)

                    # sDate + datetime.timedelta(days=(eDate - sDate).days/12) # datetime.date(2018,1,31) #
                    xPos =  sDate + datetime.timedelta(days=(eDate - sDate).days/12)
                    
                    ax.text(xPos, np.median(y)+0.02, 'median uncertainty = ' + str(round(np.median(y),2)).rjust(3,'0').ljust(4,'0') +
                            ' $\pm$ '+ str(round(scipy.stats.median_abs_deviation(y),2)).rjust(3,'0').ljust(4,'0'), 
                            color="y", va="bottom", fontsize=9)

                    # make a legend for both plots
                    leg = plt.legend(loc='upper left', bbox_to_anchor=(0.02,1))

                    # show the background grid
                    plt.grid(c='0.2', linewidth=0.1)

                    # get the current figure and automatically adjust the labels
                    fig = plt.gcf()
                    fig.autofmt_xdate()

                    # rotate the labels
                    plt.xticks(rotation=45)

                    # set the background colour
                    ax.set_facecolor('xkcd:white')
                    fig.patch.set_facecolor('xkcd:white')

                    # save the figure
                    plt.savefig(os.path.join(path + f'{station}_bar.{plot_format}'), bbox_inches='tight', dpi=1000)

                    # clear the figure
                    plt.clf()
            
                except Exception as e:
                    # clear the figure
                    plt.clf()
                    
                    logger.error(f'failed to plot the VTEC uncertainty of station {station}')
                    logger.debug(e)
                    