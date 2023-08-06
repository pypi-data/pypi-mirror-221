# In[1]:

from ftplib import FTP_TLS
import subprocess
import sys
import datetime
import time
import tarfile
import os
import shutil

from unlzw3 import unlzw

import download_madrigal


# In[2]:


def extract_vgos(file, filepath):
    
    # clear the folder corresponding to the file
    if os.path.exists(filepath + '/' + file.replace('.tgz','')):
        shutil.rmtree(filepath + '/' + file.replace('.tgz',''))
           
    # extract the '.Z' file
    tar = tarfile.open(filepath + file, 'r')
    tar.extractall(path = filepath)
    tar.close()
    
    # delete the '.Z' file, which are no longer needed
    os.remove(filepath + file)
        

# In[3]:


def extract_ionex(file, filepath):
        
    # extract the '.Z' file
    compr = open(filepath + file, 'rb').read()
    decompr = unlzw(compr)
    f = open(filepath + file[0:-2], 'wb')
    f.write(decompr)
    f.close()
    
    # delete the '.Z' file, which are no longer needed
    os.remove(filepath + file)


# In[4]:


def get_file(files):
    
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


# In[5]:


def doy(folder, file):
    
    # build a dictionary to map the months to their names to their corresponding numbers
    months = {m:i+1 for i, m in enumerate(['JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN', 
                                           'JUL', 'AUG', 'SEP', 'OCT', 'NOV', 'DEC'])}
    
    days = []
    # find the day of year corresponding to this session
    startDate = datetime.date(int(folder), 1, 1)
    endDate = datetime.date(int(folder), months[file[2:5]], int(file[5:7]))
    delta = (endDate - startDate).days + 1
    thisD = delta
    # append it to the list of days
    days.append(str(thisD).rjust(3,'0'))   
    
    
    # get the last day of year
    endDate = datetime.date(int(folder), 12, 31)
    lastD = (endDate - startDate).days + 1       
    
    # get the next day of year if the day isn't the last day in the year
    if thisD != lastD:        
        # get the next day of year
        nxtD = delta + 1
        # append it to the list of days
        days.append(str(nxtD).rjust(3,'0'))
    # else, save the 1st day in the next year
    else:
        days.append(str(1).rjust(3,'0'))
            
    return days   


# In[6]:


### VGOS
def download_vgos(startDate, endDate = ''):
    # try to connect to the ftp server 
    ftp = FTP_TLS(host = 'gdc.cddis.eosdis.nasa.gov')
    ftp.login(user = 'anonymous', passwd = 'ETHZURICH')
    ftp.prot_p()

    try:
        # try to change the ftp directory
        ftp.cwd('/vlbi/ivsdata/vgosdb/')
    except:
        # pause the code for 10 sec
        time.sleep(10)
        # try again to connect to the server 
        ftp = FTP_TLS(host = 'gdc.cddis.eosdis.nasa.gov')
        ftp.login(user = 'anonymous', passwd = 'ETHZURICH')
        ftp.prot_p()
        # try again to change the folder
        ftp.cwd('/vlbi/ivsdata/vgosdb/')

    # get the local working directory ready
    dir = os.getcwd()    
    if not os.path.exists(dir + '/Data/vgosDB/'):
        os.makedirs(dir + '/Data/vgosDB/')
    path = dir + '/Data/vgosDB/'
    
    # get the starting date and ending date, i.e. sDate and eDate
    sDate = startDate.split('/')
    sDate = datetime.date(int(sDate[0]),int(sDate[1]),int(sDate[2]))
    if endDate:
        eDate = endDate.split('/')
        eDate = datetime.date(int(eDate[0]),int(eDate[1]),int(eDate[2]))
    else:
        eDate = sDate # datetime.date.today()
    
    # get the list of years
    years = list(map(str, range(int(sDate.strftime('%Y')), int(eDate.strftime('%Y')) + 1)))
    
    # loop over the corresponding folders 
    doy_vgos = {}
    sessions = []
    for y in years:
    
        doy_vgos[y] = []
        doy_vgos[str(int(y)+1)] = []
    
        try:        
            # try to change the ftp directory to the year folder
            ftp.cwd('/vlbi/ivsdata/vgosdb/' + y)
            # get the list of the files in the ftp directory
            files = ftp.nlst()
        except:
            # pause the code for 10 sec
            time.sleep(10)
            # try again to connect to the server 
            ftp = FTP_TLS(host = 'gdc.cddis.eosdis.nasa.gov')
            ftp.login(user = 'anonymous', passwd = 'ETHZURICH')
            ftp.prot_p()
            # try again to change the directory
            # get the list of the files in the ftp directory
            files = ftp.nlst()
    
        # create a local directory for the day folder
        if not os.path.exists(path + '/' + y):
            os.makedirs(path + '/' + y)   
        
        # loop over the files in the ftp directory
        for file in files:
            
            # proceed if the file ends with the given characters
            if file.endswith(('VG.tgz')):#, 'VE.tgz', 'VB.tgz', 'VI.tgz')):
                # get the corresponding date to VGOS session
                vgosDate = datetime.date(int(y),datetime.datetime.strptime(file[2:5], "%b").month,int(file[5:7]))
            
                # download the file if the corresponding date falls in between the starting and ending dates
                if sDate <= vgosDate <= eDate: 
                    
                    try:
                        f = open(path + '/' + y + '/' + file, 'wb')
                        ftp.retrbinary("RETR " + file, f.write)
                        f.close()
                        
                        # append the file name to the list of sessions
                        sessions.append(file.replace('.tgz',''))
                
                        # extract the file
                        filepath = path + '/' + y + '/'
                        extract_vgos(file, filepath)
                
                        # save the day of year corresponding to vgos session
                        # get the days
                        days = doy(y, file)
                        # save the days to their corresponding years
                        if int(days[1]) > int(days[0]):
                            doy_vgos[y] = doy_vgos[y] + days
                        else:
                            doy_vgos[str(int(y)+1)] = doy_vgos[str(int(y)+1)] + days[1]
                
                    except:                    
                        # pause the code for 10 sec
                        time.sleep(10)
                    
                        # try again to connect to the server and download the file                    
                        ftp = FTP_TLS(host = 'gdc.cddis.eosdis.nasa.gov')
                        ftp.login(user = 'anonymous', passwd = 'ETHZURICH')
                        ftp.prot_p()
                        ftp.cwd('/vlbi/ivsdata/vgosdb/' + y)
                        f = open(path + '/' + y + '/' + file, 'wb')
                        ftp.retrbinary("RETR " + file, f.write)
                        f.close()
                        
                        # append the file name to the list of sessions
                        sessions.append(file.replace('.tgz',''))
                        
                        # extract the file
                        filepath = path + '/' + y + '/'
                        extract_vgos(file, filepath)
                
                        # save the two day of year corresponding to vgos session
                        # get the days
                        days = doy(y, file)
                        # save the days to their corresponding years
                        if int(days[1]) > int(days[0]):
                            doy_vgos[y] = doy_vgos[y] + days
                        else:
                            doy_vgos[str(int(y)+1)] = doy_vgos[str(int(y)+1)] + days[1]
        
    ftp.quit()  
    
    return doy_vgos, sessions


# In[7]:


### IONEX
def download_ionex(doy_vgos):
    # try to connect to the ftp server 
    ftp = FTP_TLS(host = 'gdc.cddis.eosdis.nasa.gov')
    ftp.login(user = 'anonymous', passwd = 'ETHZURICH')
    ftp.prot_p()

    try:
        # try to change the ftp directory
        ftp.cwd('/gnss/products/ionex/')
    except:
        # pause the code for 10 sec
        time.sleep(10)
        # try again to connect to the server 
        ftp = FTP_TLS(host = 'gdc.cddis.eosdis.nasa.gov')
        ftp.login(user = 'anonymous', passwd = 'ETHZURICH')
        ftp.prot_p()
        # try again to change the folder
        ftp.cwd('/gnss/products/ionex/')

    # get the local working directory ready 
    dir = os.getcwd()
    if not os.path.exists(dir + '/Data/Ionex/'):
        os.makedirs(dir + '/Data/Ionex/')
    path = dir + '/Data/Ionex/'
    
    # loop over the folders 
    years = [str(year) for year in doy_vgos.keys() if doy_vgos[year]]
    for y in years:
    
        try:        
            # try to change the ftp directory to the year folder
            ftp.cwd('/gnss/products/ionex/' + y)
            # get the list of the files in the ftp directory
            days = ftp.nlst()
        except:
            # pause the code for 10 sec
            time.sleep(10)
            # try again to connect to the server 
            ftp = FTP_TLS(host = 'gdc.cddis.eosdis.nasa.gov')
            ftp.login(user = 'anonymous', passwd = 'ETHZURICH')
            ftp.prot_p()
            # try again to change the directory
            ftp.cwd('/gnss/products/ionex/' + y)
            # get the list of the files in the ftp directory
            days = ftp.nlst()
    
        for d in days:
            # download the ionex files corresponding to vgos sessions
            if str(d) in doy_vgos[y]: 
                try:
                    # change the ftp directory to the day folder
                    ftp.cwd('/gnss/products/ionex/' + y + '/' + d)
                    # get the list of the files in the ftp directory
                    files = ftp.nlst()
                except:
                    # pause the code for 10 sec
                    time.sleep(10)
                    # try again to connect to the server  
                    ftp = FTP_TLS(host = 'gdc.cddis.eosdis.nasa.gov')
                    ftp.login(user = 'anonymous', passwd = 'ETHZURICH')
                    ftp.prot_p()
                    ftp.cwd('/gnss/products/ionex/' + y + '/' + d)
                    # get the list of the files in the ftp directory
                    files = ftp.nlst()
        
                # create a local directory for the day folder
                if not os.path.exists(path + '/' + y + '/' + d):
                    os.makedirs(path + '/' + y + '/' + d)
                else:
                    # clear it
                    for f in os.listdir(path + '/' + y + '/' + d):                        
                        try:
                            shutil.rmtree(os.path.join(path + '/' + y + '/' + d + '/', f))
                        except OSError:
                            os.remove(os.path.join(path + '/' + y + '/' + d + '/', f))                    
            
                # get the most recent solution, i.e. final, rapid, 1-day predict, or 2-day predict
                file = get_file(files)
            
                # download the most recent solution
                try:
                    f = open(path + '/' + y + '/' + d + '/' + file, 'wb')
                    ftp.retrbinary("RETR " + file, f.write)
                    f.close()
                    # extract the file
                    filepath = path + '/' + y + '/' + d + '/'
                    extract_ionex(file, filepath)
                
                except:                    
                    # pause the code for 10 sec
                    time.sleep(10)
                    
                    # try again to connect to the server and download the file                    
                    ftp = FTP_TLS(host = 'gdc.cddis.eosdis.nasa.gov')
                    ftp.login(user = 'anonymous', passwd = 'ETHZURICH')
                    ftp.prot_p()
                    ftp.cwd('/gnss/products/ionex/' + y + '/' + d)
                    f = open(path + '/' + y + '/' + d + '/' + file, 'wb')
                    ftp.retrbinary("RETR " + file, f.write)
                    f.close()
                
                    # extract the file
                    filepath = path + '/' + y + '/' + d + '/'
                    extract_ionex(file, filepath)
        
    ftp.quit()


# In[8]:


def v_download(startDate, endDate, ionex = 1, madrigal = 1):
    
    # downlaod vgos sessions
    doy_vgos, sessions = download_vgos(startDate, endDate)
    
    if ionex:
        # download GIMs corresponding to vgos sessions
        download_ionex(doy_vgos)
        
    if madrigal:
        # download madrigal TEC maps corresponding to vgos sessions
        download_madrigal.download_madrigal(sessions)
    
    return sessions




