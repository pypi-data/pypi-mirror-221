import datetime
import sys

import netCDF4 as nc
import numpy as np
import pyproj
import os

import IPP


class v_data:

    def __ini__(self):
        pass

    @classmethod
    def BsElAzIPPLLA(cls, logger, session, geomagnetic, modip, modip_grid, path):

        """This function reads and prepares the meta data of VLBI/VGOS sessions."""

        #######
        ########

        # read the station file
        try:
            Station = nc.Dataset(os.path.join(path + '/Apriori/Station.nc'))
        except Exception as e:
            logger.error('failed to find/process the Station.nc file')
            logger.debug(e)

        # extract the station cartesian coordinates (XYZ)
        stationXYZ = Station['AprioriStationXYZ'][:]
        
            
        #######
        ########

        # convert the coordinates of the station from XYZ to longitudate, latitude, and altitude
        # create a tranformation object
        transformer = pyproj.Transformer.from_crs({"proj": 'geocent', "ellps": 'WGS84', "datum": 'WGS84'},
                                                  {"proj": 'latlong', "ellps": 'WGS84', "datum": 'WGS84'})

        # latitude, longitude, and altitude order
        stationLLA = np.zeros(shape=(len(stationXYZ[:]), len(stationXYZ[0, :])))

        # cartesian(XYZ) to georgraphic(LLA) coordinates
        for n, item in enumerate(stationXYZ[:]):
            # longitude, latitude, and altitude order
            stationLLA[n, 1], stationLLA[n, 0], stationLLA[n, 2] = transformer.transform(item[0], item[1], item[2])

        #######
        ########

        # read the station cross reference file
        try:
            StaCrRef = nc.Dataset(os.path.join(path + '/CrossReference/StationCrossRef.nc'))
        except Exception as e:
            logger.error('failed to find/process the StationCrossRef.nc file')
            logger.debug(e)

        # extract the station list
        StationList = StaCrRef['CrossRefStationList'][:]
        nStation = len(StationList)
        

        stations = []
        # decode the string back into ASCII
        for i in range(len(StationList[:])):
            x = []
            for j in range(len(StationList[i, :])):
                x.append(StationList[i, j].decode('UTF-8'))
            # concatenate the letters
            stations.append(''.join(x).replace(' ', ''))

        # extract the elevation angle and azimuth for each scan and station    
        Scan2Station = StaCrRef['Scan2Station'][:].data
        AzEl2Station = np.zeros(shape=(len(Scan2Station[:, 0]), len(stations), 2))
        for i in range(len(stations)):
            try:
                AzEl = nc.Dataset(os.path.join(path + stations[i] + '/' + 'AzEl.nc'))
            except Exception as e:
                logger.error('failed to find/process the AzEl.nc file')
                logger.debug(e)
            El = AzEl['ElTheo'][:, 0].data
            Az = AzEl['AzTheo'][:, 0].data
            for n, item in enumerate(Scan2Station[:, i]):
                if item != 0:
                    AzEl2Station[n, i, 0] = El[item - 1]
                    AzEl2Station[n, i, 1] = Az[item - 1]
                    

        #######
        ########

        # read the observation cross reference file
        try:
            ObsCrRef = nc.Dataset(os.path.join(path + '/CrossReference/ObsCrossRef.nc'))
        except Exception as e:
            logger.error('failed to find/process the ObsCrossRef.nc file')
            logger.debug(e)

        # extract the elevation angle for each observation and station
        Obs2Scan = ObsCrRef['Obs2Scan'][:].data
        AzEl2Obs = AzEl2Station[Obs2Scan - 1]

        # get the observations per baseline (station #)
        Obs2Baseline = ObsCrRef['Obs2Baseline'][:].data

        # get the elevation angle and the azimuth per station
        El2Station = np.zeros(shape=(len(Obs2Baseline[:, 0]), len(Obs2Baseline[0, :])))
        Az2Station = np.zeros(shape=(len(Obs2Baseline[:, 0]), len(Obs2Baseline[0, :])))
        for n, i in enumerate(Obs2Baseline[:, :]):
            El2Station[n, :] = AzEl2Obs[n, i[:] - 1, 0]
            Az2Station[n, :] = AzEl2Obs[n, i[:] - 1, 1]
                     
            
        #######
        ########

        # read the source cross reference file
        try:
            SourceCrRef = nc.Dataset(os.path.join(path + '/CrossReference/SourceCrossRef.nc'))
        except Exception as e:
            logger.error('failed to find/process the SourceCrossRef.nc file')
            logger.debug(e)

        # get the list of sources
        SourceList = SourceCrRef['CrossRefSourceList'][:].data

        Sources = []
        # decode the string back into ASCII
        for i in range(len(SourceList[:])):
            x = []
            for j in range(len(SourceList[i, :])):
                x.append(SourceList[i, j].decode('UTF-8'))
            # concatenate the letters
            Sources.append(''.join(x).replace(' ', ''))

        # extract the number of the radio source for each observation and station
        Scan2Source = SourceCrRef['Scan2Source'][:].data
        Obs2Source = Scan2Source[Obs2Scan - 1]
        
        #######
        ########
        # organize the meta_data
        meta_data = np.zeros(shape=(Obs2Baseline.shape[0], Obs2Baseline.shape[1], 8))
        meta_data[:, :, 0] = Obs2Baseline
        meta_data[:, :, 1] = El2Station
        meta_data[:, :, 2] = Az2Station
        meta_data[:, 0, 7] = Obs2Source
        meta_data[:, 1, 7] = Obs2Scan

        #######
        ########
        # 
        if geomagnetic and modip:
            logger.critical('You can choose either geomagnetic latitude or modip latitude; please, specify.')
            sys.exit()

        # get IPPs
        meta_data = IPP.IPP.IPP_LLA(logger, session, stationLLA, meta_data, geomagnetic, modip, modip_grid)
        
        ########
        # close the datasets
        Station.close()
        StaCrRef.close()
        AzEl.close()
        ObsCrRef.close()
        SourceCrRef.close()

        return nStation, meta_data, stations, stationLLA, stationXYZ.data, Sources

    @classmethod
    def vgos_dTEC(cls, logger, path):

        '''This function reads the ionospheric delays (dTEC) of VGOS observations.'''

        ###
        # read the DiffTec.nc file
        try:
            ds = nc.Dataset(os.path.join(path + '/Observables/DiffTec.nc'))
        except Exception as e:
            logger.error('failed to find/process the DiffTec.nc file')
            logger.debug(e)

        dtec = ds['diffTec'][:].data
        dtecstd = ds['diffTecStdDev'][:].data
        
        # close the dataset
        ds.close()
        
        return dtec, dtecstd

    @classmethod
    def vlbi_dTEC(cls, logger, path):

        '''This function reads the ionospheric delays (dTEC) of geodetic VLBI observations.'''

        ###
        # read the file
        try:
            # using Hobiger's method with X-band
            dsx = nc.Dataset(os.path.join(path + '/ObsDerived/Cal-SlantPathIonoGroup_bX.nc'))
        except Exception as e:
            logger.error('failed to find/process the DiffTec.nc file')
            logger.debug(e)

        dtec = dsx['Cal-SlantPathIonoGroup'][:, 0].data
        dtecstd = dsx['Cal-SlantPathIonoGroupSigma'][:, 0].data
        
        # close the dataset
        dsx.close()
        
        return dtec, dtecstd

    
    @classmethod
    def obs_epochs(cls, logger, path):

        '''This function reads the epochs of geodetic VLBI/VGOS observations.'''

        ###
        # read the TimeUTC.nc file
        try:
            t = nc.Dataset(os.path.join(path + '/Observables/TimeUTC.nc'))
        except Exception as e:
            logger.error('failed to find/process the TimeUTC.nc file')
            logger.debug(e)

        # 
        YMD = t['YMDHM'][0, 0:3].data

        # extract the starting time of the session
        h0 = t['YMDHM'][0, 3].data

        # extract the epoch of the observation
        h = t['YMDHM'][:, 3].data + t['YMDHM'][:, 4].data / 60 + t['Second'][:].data / (60 ** 2)

        # get the starting date
        date0 = datetime.date(2000 + t['YMDHM'][0, 0].data, t['YMDHM'][0, 1].data, t['YMDHM'][0, 2].data)
        for i in range(len(h)):
            # calcuate the ending date       
            date1 = datetime.date(2000 + t['YMDHM'][i, 0].data, t['YMDHM'][i, 1].data, t['YMDHM'][i, 2].data)
            # calculate the difference in days between the starting and ending dates
            did = (date1 - date0).days
            # calculate the hours since the start of the session 
            h[i] = h[i] + (24 * did - h0)
        
        # close the dataset
        t.close()
        
        # return the starting time and the epoch
        return h0, h, YMD

    @classmethod
    def doy(cls, logger, YMD):

        '''This function finds the day of year for a given date.'''

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
        days.append(str(thisD).rjust(3, '0'))

        # get the last day of year
        endDate = datetime.date(year, 12, 31)
        lastD = (endDate - startDate).days + 1

        # get the next day of year if the day isn't the last day in the year
        if thisD != lastD:
            # get the next day of year
            nxtD = delta + 1
            # append it to the list of days
            days.append(str(nxtD).rjust(3, '0'))
        # else, save the 1st day in the next year
        else:
            days.append(str(1).rjust(3, '0'))

        return days

    @classmethod
    def v_data(cls, logger, session, exSta=[], snr=15, cutoffangle=5, minObs=5,
               vgosDB_path='Data/vgosDB/', geomagnetic=0, modip=1, modip_grid=1):

        '''This function reads, prepares, and preprocesses geodetic VLBI/VGOS observations for further processing.'''

        if 'VG' in session:

            ### get the data   
            # get the path
            year = 2000 + int(session[0:2])
            session_path = os.path.join(vgosDB_path + str(year) + '/' + session + '/')

            # read the observations         
            nSta, meta_data, stations, stationLLA, stationXYZ, sources = cls.BsElAzIPPLLA(logger, session,
                                                                                          geomagnetic, modip,
                                                                                          modip_grid, path=session_path)

            # get the signal to noise ratio of the observations
            ds = nc.Dataset(os.path.join(session_path + 'Observables/SNR_bX.nc'))
            s2nr = ds['SNR'][:].data
            ds.close()
            
            # get the ionospheric delays  in TECU
            dtec, dtecstd = cls.vgos_dTEC(logger, path=session_path)
            
            # get the epoch of the observations
            h0, hrs, YMD = cls.obs_epochs(logger, path=session_path)

            # get the freq in MHz and convert it to Hz
            ds = nc.Dataset(os.path.join(session_path + 'Observables/RefFreq_bX.nc'))
            freq = ds['RefFreq'][:].data
            freq = np.array([float(freq * 1e6) for i in range(len(hrs[:]))])
            ds.close()
            
            # convert the delay from TECU to meters
            # dtec, dtecstd = dtec * (40.31/freq**2), dtecstd * (40.31/freq**2)
            
            # to convert the unit of the instr. offsets from TECU to nanosecond, you need to multiple it with
            # print(np.average(40.31*(10**16)*(10**9)/(299792458 * freq**2)))

            ### preprocess the data        
            # get the indices of the observations from sources that were scanned more than the minObs 
            sindx = []
            Obs2Source = meta_data[:, 0, 7]
            for i in set(Obs2Source):
                xindx = [j for j in range(len(Obs2Source)) if Obs2Source[j] == i]
                if len(xindx) > minObs:
                    sindx = sindx + xindx

                    # get the observations with signal to noise ratio more than snr
            snrindx = [list(s2nr).index(s2nr[i]) for i in range(len(s2nr)) if s2nr[i] > snr]

            # get the indices of the observations with an elevation angle more than the cut off angle   
            caindx = [i for i in range(len(meta_data[:, 0, 1]))
                      if np.rad2deg(meta_data[i, 0, 1]) > cutoffangle and np.rad2deg(meta_data[i, 1, 1]) > cutoffangle]

            # get the indices of observations with non-zero standard deviation
            # obs. w. zero sta. dev. are basically made with the twin telescopes, i.e., Onsala13SW and Onsala13NE, as a baseline
            nzindx = [i for i in range(len(dtecstd)) if dtecstd[i] != 0]

            # get the indices of the observations corresponding to the stations that are to be exiled
            inindx = cls.include_stations(logger, stations, meta_data, exSta)

            # find the common indices
            indx = np.intersect1d(sindx,
                                  np.intersect1d(np.intersect1d(snrindx, nzindx), np.intersect1d(caindx, inindx)))

            # extract the corresponding observations  
            meta_data, hrs = meta_data[indx, :, :], hrs[indx]
            dtec, dtecstd = dtec[indx], dtecstd[indx]
            freq = freq[indx]
            s2nr = s2nr[indx]

            # extract the time tag and the integer hours
            t = hrs[:]

            # find the day of year (DOY) of VGOS/VLBI session to be used in GIMs  
            days = cls.doy(logger, YMD)
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
            if vgosDB_path:
                session_path = vgosDB_path + str(year) + '/' + session + '/'
            else:
                vgosDB_path = 'Data/vgosDB/'
                session_path = os.path.join(vgosDB_path + str(year) + '/' + session + '/')
            nSta, meta_data, stations, stationLLA, stationXYZ, sources = cls.BsElAzIPPLLA(logger, session,
                                                                                          geomagnetic, modip,
                                                                                          modip_grid, path=session_path)

            # get the signal to noise ratio of the observations
            dsx = nc.Dataset(os.path.join(session_path + 'Observables/SNR_bX.nc'))
            s2nrX = dsx['SNR'][:].data
            dsx.close()
            
            dss = nc.Dataset(os.path.join(session_path + 'Observables/SNR_bS.nc'))
            s2nrS = dss['SNR'][:].data            
            dss.close()

            # get the ionospheric delays in seconds
            dtec, dtecstd = cls.vlbi_dTEC(logger, path=session_path)

            # get the epoch of the observations
            h0, hrs, YMD = cls.obs_epochs(logger, path=session_path)
            
            # get the effective freq in MHz and then converted to Hz
            ds = nc.Dataset(os.path.join(session_path + 'ObsDerived/EffFreq_bX.nc'))
            freq = ds['FreqGroupIono'][:].data * 1e6
            ds.close()

            # get the reference freq of X-band and S-band in MHz and converted to Hz
            dss = nc.Dataset(os.path.join(session_path + 'ObsDerived/EffFreq_bS.nc'))
            fs = dss['FreqGroupIono'][:].data * 1e6
            dss.close()
            dsx = nc.Dataset(os.path.join(session_path + 'ObsDerived/EffFreq_bX.nc'))
            fx = dsx['FreqGroupIono'][:].data * 1e6
            dsx.close()


            if len(fs) == 1:
                fs = np.array([float(fs) for i in range(len(hrs[:]))])

            if len(fx) == 1:
                fx = np.array([float(fx) for i in range(len(hrs[:]))])

            ### preprocess the data
            # get the indices of the observations from sources that were scanned more than the minObs 
            sindx = []
            Obs2Source = meta_data[:, 0, 7]
            for i in set(Obs2Source):
                xindx = [j for j in range(len(Obs2Source)) if Obs2Source[j] == i]
                if len(xindx) > minObs:
                    sindx = sindx + xindx

            # get the indices of the observatins with a signal to noise ration more than snr
            snrindxX = [list(s2nrX).index(s2nrX[i]) for i in range(len(s2nrX)) if s2nrX[i] > snr]
            snrindxS = [list(s2nrS).index(s2nrS[i]) for i in range(len(s2nrS)) if s2nrS[i] > snr]
            snrindx = list(set(snrindxX + snrindxS))

            # get the indices of the observations with an elevation angle more than the cut off angle   
            caindx = [i for i in range(len(meta_data[:, 0, 1]))
                      if np.rad2deg(meta_data[i, 0, 1]) > cutoffangle and np.rad2deg(meta_data[i, 1, 1]) > cutoffangle]

            # find the indices of non-zero frequences
            indxf = [i for i in range(len(fs)) if fs[i] != 0 and fx[i] != 0]

            # get the indices of observations with non-zero standard deviation
            # obs. w. zero sta. dev. are basically made with the twin telescopes, i.e., Onsala13SW and Onsala13NE, as a baseline
            nzindx = [i for i in range(len(dtecstd)) if dtecstd[i] != 0]

            # get the indices of the observations corresponding to the stations that are to be exiled
            inindx = cls.include_stations(logger, stations, meta_data, exSta)

            # find the common indices
            indx = np.intersect1d(np.intersect1d(sindx, snrindx),
                                  np.intersect1d(np.intersect1d(nzindx, caindx), np.intersect1d(indxf, inindx)))

            # extract the corresponding observations  
            meta_data, hrs = meta_data[indx, :, :], hrs[indx]
            dtec, dtecstd = dtec[indx], dtecstd[indx]
            freq = freq[indx]
            fs, fx = fs[indx], fx[indx]
            s2nr = np.column_stack((s2nrS, s2nrX))[indx, :]
                    
                      
            # using Hobiger's equation for S/X-band
            dtec, dtecstd = dtec * 299792458 * freq**2 * (10**-16)/ 40.31 , dtecstd * 299792458 * freq**2 * (10**-16)/ 40.31 

            # to convert the unit of the instr. offsets from TECU to nanosecond, you need to multiple it with
            # print(np.average(40.31 * f * (10**16)*(10**9))/299792458)

            # extract the time tag and the integer hours
            t = hrs[:]

            # find the day of year (DOY) of VGOS/VLBI session to be used in GIMs  
            days = cls.doy(logger, YMD)
            v_doy = {}
            # save the days to their corresponding years
            if int(days[1]) > int(days[0]):
                v_doy[str(year)] = days
            else:
                v_doy[str(year + 1)] = days[1]

            return h0, freq, nSta, stations, stationLLA, stationXYZ, meta_data, dtec, dtecstd, t, v_doy, sources, s2nr

        else:
            logger.critical(
                session + ' does not end with XA, XB or VG. Please, provide the correct name of the session')
            sys.exit()

    @classmethod
    def include_stations(cls, logger, stations, cs, exSta=[]):

        '''This function finds the indices of the stations to be included in the LSQ adjustment.'''

        # find the indices of the stations to be excluded  
        exStaIndx = [stations.index(i) for i in exSta]

        # find the indices of the observations of the remaining stations; 
        # the corresponding column of the stations will later be deleted automatically
        inindx = [i for i in range(len(cs[:, 0, 0])) if
                  cs[i, 0, 0] - 1 not in exStaIndx or cs[i, 1, 0] - 1 not in exStaIndx]

        return inindx

    @classmethod
    def exclude_problematic_stations(cls, logger, sessions, v_input_path=''):

        '''This function reads the file of problematic stations in geodetic VLBI/VGOS sessions.'''
        
        psl = {session: [] for session in sessions}
        with open(os.path.join(v_input_path + 'Data/Others/Problematic_Stations.txt'), 'r') as file:                    
            for line in file.read().split('\n'):
                if line:
                    if line.split()[0] in psl.keys():
                        psl[line.split()[0]] = line.split()[1:]
                        
        file.close()
        
        return psl

    @classmethod
    def extract_observations(cls, logger, freq, s2nr, meta_data, dtec, dtecstd, t, eindx=[]):

        '''This function extracts the different types of observations such as lat and lon of IPP. It also eliminates any observations flagged as outlier.'''

        ## delete any observations flagged as an outliers
        if eindx:
            # the time tag and the integer hours
            t = np.delete(t, eindx, 0)

            # the dtec and their standard deviations
            dtec = np.delete(dtec, eindx, 0)
            dtecstd = np.delete(dtecstd, eindx, 0)

            # the frequency
            freq = np.delete(freq, eindx, 0)

            # the signal to noise ratio
            s2nr = np.delete(s2nr, eindx, 0)

            # the meta data
            meta_data = np.delete(meta_data, eindx, 0)

        ## extract observations
        # extract the number of the station
        sta = np.zeros(shape=(len(meta_data[:, 0, 0]), 2))
        sta[:, 0] = [int(meta_data[i, 0, 0]) for i in range(len(meta_data[:, 0, 0]))]
        sta[:, 1] = [int(meta_data[i, 1, 0]) for i in range(len(meta_data[:, 1, 0]))]

        # extract the elevation angle of the iono piercing points
        elev = meta_data[:, :, 1]

        # extract the latitude and longitude of the iono piercing points
        latIPP = meta_data[:, :, 3]
        lonIPP = meta_data[:, :, 4]

        # extract the latitude and longitude of the VGOS/VLBI stations
        latSta = meta_data[:, :, 5]
        lonSta = meta_data[:, :, 6]

        return freq, meta_data, sta, elev, latIPP, lonIPP, latSta, lonSta, dtec, dtecstd, t, s2nr
