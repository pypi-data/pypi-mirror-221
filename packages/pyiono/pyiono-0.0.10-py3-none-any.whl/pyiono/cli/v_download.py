
import datetime
import os
import random
import shutil
import string
import tarfile
import time
from ftplib import FTP_TLS
from typing import List

from unlzw3 import unlzw

import download_madrigal

import multiprocessing


class file_management:

    def __ini__(self):
        pass

    @classmethod
    def extract_vgos(cls, file, filepath):

        """This function unzips the session files."""

        # clear the folder corresponding to the file
        if os.path.exists(filepath + '/' + file.replace('.tgz', '')):
            shutil.rmtree(filepath + '/' + file.replace('.tgz', ''))

        # extract the '.Z' file
        tar = tarfile.open(filepath + file, 'r')
        tar.extractall(path=filepath)
        tar.close()

        # delete the '.Z' file, which are no longer needed
        os.remove(filepath + file)

    @classmethod
    def extract_ionex(cls, file, filepath):

        """This function decompresses the ionex file."""

        # extract the '.Z' file
        with open(filepath + file, 'rb') as f:
            decompr = unlzw(f.read())
        f.close()
        
        with open(filepath + file[0:-2], 'wb') as f:
            f.write(decompr)
        f.close()
        
        # delete the '.Z' file, which are no longer needed
        os.remove(filepath + file)

    @classmethod
    def rename_file(cls, sessions, download_path):

        """This function renames the geodetic VLBI/VGOS sessions for consistency purposes."""

        # get the path to VGOSDB
        vgosDB_path = download_path + 'Data/vgosDB/'
        years = os.listdir(vgosDB_path)
        for year in years:
            # rename the folder for consistency purposes, e.g. 19MAY21VG
            session_list = os.listdir(vgosDB_path + year + '/')
            for session in session_list:
                if len(session) > 9 and session[:9] in sessions:
                    os.rename(vgosDB_path + year + '/' + session, vgosDB_path + year + '/' + session[:9])

    @classmethod
    def get_file(cls, files):

        """This function finds the ionex file with the most recent and accurate solution to be downloaded."""

        # get the names of the centres that have available solution
        centers = [file[0:3] for file in files]

        # get the most recent solution, i.e. final, rapid, 1-day predict, or 2-day predict
        if 'igs' in centers:
            file = files[centers.index('igs')]
        elif 'esa' in centers:
            file = files[centers.index('esa')]
        elif 'cod' in centers:
            file = files[centers.index('cod')]
        elif 'jpl' in centers:
            file = files[centers.index('jpl')]
        elif 'upc' in centers:
            file = files[centers.index('upc')]
        elif 'cas' in centers:
            file = files[centers.index('cas')]
        elif 'whu' in centers:
            file = files[centers.index('whu')]
        elif 'igr' in centers:
            file = files[centers.index('igr')]
        elif 'esr' in centers:
            file = files[centers.index('esr')]
        elif 'cor' in centers:
            file = files[centers.index('cor')]
        elif 'upr' in centers:
            file = files[centers.index('upr')]
        elif 'uqr' in centers:
            file = files[centers.index('uqr')]
        elif 'uhr' in centers:
            file = files[centers.index('uhr')]
        elif 'ehr' in centers:
            file = files[centers.index('ehr')]
        elif 'car' in centers:
            file = files[centers.index('car')]
        elif 'whr' in centers:
            file = files[centers.index('whr')]
        elif 'i1p' in centers:
            file = files[centers.index('i1p')]
        elif 'c1p' in centers:
            file = files[centers.index('c1p')]
        elif 'e1p' in centers:
            file = files[centers.index('e1p')]
        elif 'i2p' in centers:
            file = files[centers.index('i2p')]
        elif 'c2p' in centers:
            file = files[centers.index('c2p')]
        elif 'e2p' in centers:
            file = files[centers.index('e2p')]
        elif 'u2p' in centers:
            file = files[centers.index('u2p')]

        return file

    @classmethod
    def doy(cls, folder, file):
        """This function calculates the day of year for a given date."""

        # build a dictionary to map the months to their names to their corresponding numbers
        months = {m: i + 1 for i, m in enumerate(['JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN',
                                                  'JUL', 'AUG', 'SEP', 'OCT', 'NOV', 'DEC'])}

        days: List[str] = []
        # find the day of year corresponding to the start of the session
        start_date = datetime.date(int(folder), 1, 1)
        ss_doy = datetime.date(int(folder), months[file[2:5]], int(file[5:7])).timetuple().tm_yday

        # append it to the list of days
        days.append(str(ss_doy).rjust(3, '0'))

        # get the last day of year
        ey_doy = datetime.date(int(folder), 12, 31).timetuple().tm_yday

        # get the next day of year if the day isn't the last day in the year
        if ss_doy != ey_doy:
            # get the next day of year
            es_doy = ss_doy + 1
            # append it to the list of days
            days.append(str(es_doy).rjust(3, '0'))
        # else, save the 1st day in the next year
        else:
            days.append(str(1).rjust(3, '0'))

        return days


class file_download:

    def __ini__(self):
        pass

    @classmethod
    def download_vgos(cls, startDate, endDate, extension, download_path):

        '''This function downloads geodetic VLBI/VGOS sessions from the CDDIS server.'''

        # try to connect to the ftp server
        ftp = FTP_TLS(host='gdc.cddis.eosdis.nasa.gov')
        ftp.login(user='anonymous', passwd=''.join(random.choices(string.ascii_letters + string.digits, k=8)))
        ftp.prot_p()

        try:
            # try to change the ftp directory
            ftp.cwd('/vlbi/ivsdata/vgosdb/')
        except:
            # pause the code for 10 sec
            time.sleep(1)
            # try again to connect to the server 
            ftp = FTP_TLS(host='gdc.cddis.eosdis.nasa.gov')
            ftp.login(user='anonymous', passwd=''.join(random.choices(string.ascii_letters + string.digits, k=8)))
            ftp.prot_p()
            # try again to change the folder
            ftp.cwd('/vlbi/ivsdata/vgosdb/')

        # get the local working directory ready
        if download_path:
            dir = download_path
        else:
            dir = os.getcwd()
        if not os.path.exists(dir + '/Data/vgosDB/'):
            os.makedirs(dir + '/Data/vgosDB/')
        path = dir + '/Data/vgosDB'

        # get the starting date and ending date, i.e. sDate and eDate
        sDate = startDate.split('/')
        sDate = datetime.date(int(sDate[0]), int(sDate[1]), int(sDate[2]))
        if endDate:
            eDate = endDate.split('/')
            eDate = datetime.date(int(eDate[0]), int(eDate[1]), int(eDate[2]))
        else:
            eDate = sDate  # datetime.date.today()

        # get the list of years
        years = list(map(str, range(int(sDate.strftime('%Y')), int(eDate.strftime('%Y')) + 1)))

        # loop over the corresponding folders 
        doy_vgos = {}
        sessions = []
        for year in years:

            doy_vgos[year] = []
            doy_vgos[str(int(year) + 1)] = []

            try:
                # try to change the ftp directory to the year folder
                ftp.cwd('/vlbi/ivsdata/vgosdb/' + year)
                # get the list of the files in the ftp directory
                files = ftp.nlst()
            except:
                # pause the code for 10 sec
                time.sleep(1)
                # try again to connect to the server 
                ftp = FTP_TLS(host='gdc.cddis.eosdis.nasa.gov')
                ftp.login(user='anonymous', passwd=''.join(random.choices(string.ascii_letters + string.digits, k=8)))
                ftp.prot_p()
                # try again to change the directory
                # get the list of the files in the ftp directory
                files = ftp.nlst()

            # create a local directory for the day folder
            if not os.path.exists(path + '/' + year):
                os.makedirs(path + '/' + year)

            # loop over the files in the ftp directory
            for file in files:

                # proceed if the file ends with the given characters
                if file.endswith(tuple(extension)):  # , 'VE.tgz', 'VB.tgz', 'VI.tgz')):
                    # get the corresponding date to VGOS session
                    vgosDate = datetime.date(int(year), datetime.datetime.strptime(file[2:5], "%b").month, int(file[5:7]))

                    # download the file if the corresponding date falls in between the starting and ending dates
                    if sDate <= vgosDate <= eDate:

                        try:
                            with open(path + '/' + year + '/' + file, 'wb') as f:
                                ftp.retrbinary("RETR " + file, f.write)
                            f.close()

                            # append the file name to the list of sessions
                            sessions.append(file.replace('.tgz', ''))

                            # extract the file
                            filepath = path + '/' + year + '/'
                            file_management.extract_vgos(file, filepath)

                            # save the day of year corresponding to vgos session
                            # get the days
                            days = file_management.doy(year, file)
                            # save the days to their corresponding years
                            if int(days[1]) > int(days[0]):
                                doy_vgos[year] = doy_vgos[year] + days
                            else:
                                doy_vgos[str(int(year) + 1)] = doy_vgos[str(int(year) + 1)] + days[1]

                        except:
                            # pause the code for 10 sec
                            time.sleep(1)

                            # try again to connect to the server and download the file                    
                            ftp = FTP_TLS(host='gdc.cddis.eosdis.nasa.gov')
                            ftp.login(user='anonymous', passwd=''.join(random.choices(string.ascii_letters + string.digits, k=8)))
                            ftp.prot_p()
                            ftp.cwd('/vlbi/ivsdata/vgosdb/' + year)
                            with open(path + '/' + year + '/' + file, 'wb') as f:
                                ftp.retrbinary("RETR " + file, f.write)
                            f.close()

                            # append the file name to the list of sessions
                            sessions.append(file.replace('.tgz', ''))

                            # extract the file
                            filepath = path + '/' + year + '/'
                            file_management.extract_vgos(file, filepath)

                            # save the two day of year corresponding to vgos session
                            # get the days
                            days = file_management.doy(year, file)
                            # save the days to their corresponding years
                            if int(days[1]) > int(days[0]):
                                doy_vgos[year] = doy_vgos[year] + days
                            else:
                                doy_vgos[str(int(year) + 1)] = doy_vgos[str(int(year) + 1)] + days[1]

        ftp.quit()

        return doy_vgos, sessions
    

    @classmethod
    def download_ionex(cls, doy_ionex, download_path):

        '''This function downloads the ionex files containing global ionosphere maps (GIMs) from the CDDIS server.'''

        # try to connect to the ftp server 
        ftp = FTP_TLS(host='gdc.cddis.eosdis.nasa.gov')
        ftp.login(user='anonymous', passwd=''.join(random.choices(string.ascii_letters + string.digits, k=8)))
        ftp.prot_p()

        try:
            # try to change the ftp directory
            ftp.cwd('/gnss/products/ionex/')
        except:
            # pause the code for 10 sec
            time.sleep(1)
            # try again to connect to the server 
            ftp = FTP_TLS(host='gdc.cddis.eosdis.nasa.gov')
            ftp.login(user='anonymous', passwd=''.join(random.choices(string.ascii_letters + string.digits, k=8)))
            ftp.prot_p()
            # try again to change the folder
            ftp.cwd('/gnss/products/ionex/')

        # get the local working directory ready 
        if download_path:
            dir = download_path
        else:
            dir = os.getcwd()
        if not os.path.exists(dir + '/Data/Ionex/'):
            os.makedirs(dir + '/Data/Ionex/')
        path = dir + '/Data/Ionex'

        # loop over the folders 
        years = [str(year) for year in doy_ionex.keys() if doy_ionex[year]]
        for year in years:

            try:
                # try to change the ftp directory to the year folder
                ftp.cwd('/gnss/products/ionex/' + year)
                # get the list of the files in the ftp directory
                days = ftp.nlst()
            except:
                # pause the code for 10 sec
                time.sleep(1)
                # try again to connect to the server 
                ftp = FTP_TLS(host='gdc.cddis.eosdis.nasa.gov')
                ftp.login(user='anonymous', passwd=''.join(random.choices(string.ascii_letters + string.digits, k=8)))
                ftp.prot_p()
                # try again to change the directory
                ftp.cwd('/gnss/products/ionex/' + year)
                # get the list of the files in the ftp directory
                days = ftp.nlst()

            ftp.quit()
            
            
            # Download 100 ionex files per connection
            for i in range(0, len(days), 100):
                
                # try again to connect to the server  
                ftp = FTP_TLS(host='gdc.cddis.eosdis.nasa.gov')
                ftp.login(user='anonymous', passwd=''.join(random.choices(string.ascii_letters + string.digits, k=8)))
                ftp.prot_p()
                                
                for day in days[i:i+100]:
                    
                    # download the ionex files corresponding to vgos sessions
                    if str(day) in doy_ionex[year]:
                        try:
                            # change the ftp directory to the day folder
                            ftp.cwd('/gnss/products/ionex/' + year + '/' + day)
                            # get the list of the files in the ftp directory
                            files = ftp.nlst()
                        except:
                            # pause the code for 10 sec
                            time.sleep(1)
                            # try again to connect to the server  
                            ftp = FTP_TLS(host='gdc.cddis.eosdis.nasa.gov')
                            ftp.login(user='anonymous', passwd=''.join(random.choices(string.ascii_letters + string.digits, k=8)))
                            ftp.prot_p()
                            ftp.cwd('/gnss/products/ionex/' + year + '/' + day)
                            # get the list of the files in the ftp directory
                            files = ftp.nlst()

                        # create a local directory for the day folder
                        if not os.path.exists(path + '/' + year + '/' + day):
                            os.makedirs(path + '/' + year + '/' + day)
                        else:
                            # clear it
                            for f in os.listdir(path + '/' + year + '/' + day):
                                os.remove(os.path.join(path + '/' + year + '/' + day + '/', f))

                        # get the most recent solution, i.e. final, rapid, 1-day predict, or 2-day predict
                        file = file_management.get_file(files)

                        # download the most recent solution
                        try:
                            with open(path + '/' + year + '/' + day + '/' + file, 'wb') as f:
                                ftp.retrbinary("RETR " + file, f.write)
                            f.close()

                            # extract the file
                            filepath = path + '/' + year + '/' + day + '/'
                            file_management.extract_ionex(file, filepath)

                        except:
                            # pause the code for 10 sec
                            time.sleep(1)

                            # try again to connect to the server and download the file                    
                            ftp = FTP_TLS(host='gdc.cddis.eosdis.nasa.gov')
                            ftp.login(user='anonymous', passwd=''.join(random.choices(string.ascii_letters + string.digits, k=8)))
                            ftp.prot_p()
                            ftp.cwd('/gnss/products/ionex/' + year + '/' + day)
                            with open(path + '/' + year + '/' + day + '/' + file, 'wb') as f:
                                ftp.retrbinary("RETR " + file, f.write)
                            f.close()

                            # extract the file
                            filepath = path + '/' + year + '/' + day + '/'
                            file_management.extract_ionex(file, filepath)

                ftp.quit()
                
    @classmethod
    def download_MTM(cls, sessions, download_path):
        
        data = [(session, download_path) for session in sessions]
        with multiprocessing.Pool() as pool:    
            _ = pool.starmap(download_madrigal.download_madrigal, data) 
        
        
    @classmethod
    def v_download(cls, logger, startDate, endDate, ionex, madrigal, extension, download_path):

        '''This function downloads geodetic VLBI/VGOS sessions, Ionex files, Madrigal TEC maps (MTMs).'''

        # download vgos sessions
        logger.info('Downloading VLBI/VGOS sessions is in progress ..')
        doy_vgos, sessions = cls.download_vgos(startDate, endDate, extension, download_path)
        file_management.rename_file(sessions, download_path)
        logger.info('Downloading VGOS sessions is complete.')
        

        if ionex:
            logger.info('Downloading GIMs sessions is in progress ..')
            
            # download GIMs corresponding to vgos sessions
            cls.download_ionex(doy_vgos, download_path)
            
            logger.info('Downloading GIMs is complete.')

        if madrigal:
            logger.info('Downloading MTMs is in progress ..')
            
            # download madrigal TEC maps corresponding to vgos sessions
            cls.download_MTM(sessions, download_path)                        
            
            logger.info('Downloading MTMs is complete.')

        return sessions
