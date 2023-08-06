
import netCDF4 as nc
import numpy as np
import os
import math
import matplotlib.pylab as plt
import random
import datetime
import time
import matplotlib
import statistics
import pyproj
matplotlib.use('Agg')



class g_gnss:

       
    @classmethod
    def g_data(cls, logger, session, geomagnetic, modip, modip_grid, cutoffangle, input_path):

        '''This function reads, prepares, and preprocesses GNSS data for further processing.'''

        # read the coordinates of the stations from the coord file
        try:
            with open(input_path + str(2000 + int(session[0:2])) + '/' + 'coord.txt', 'r') as file:
                file_content = file.read().split('\n')[3:]
            file.close()
        except Exception as e:
            logger.error(e)
            
        sxyz = {line.split()[0]: list(np.array(line.split()[1:]).astype(float)) for line in file_content if line}

        # convert the coordinates from XYZ to latitude and longitude
        # create a tranformation object
        transformer = pyproj.Transformer.from_crs({"proj":'geocent', "ellps":'WGS84', "datum":'WGS84'},
                                                  {"proj":'latlong', "ellps":'WGS84', "datum":'WGS84'})
        # get it
        slla = {key: list(transformer.transform(value[0], value[1], value[2])[:2])[::-1] for key, value in sxyz.items()}

        # read the file
        with open(input_path + str(2000 + int(session[0:2])) + '/' +  session + '.TEC', 'r') as file:
            file_content = file.read().split('\n')[3:]
        file.close()        
        
        # clean the data from nan and inf
        file_content = [line for line in file_content if line if 'nan' not in line]
        file_content = [line for line in file_content if line if 'inf' not in line]
        file_content = [line for line in file_content if line if float(line.split()[6]) > 0] # remove negative stec
    
        # clean the data from observations with elevation angle below, e.g., 5 deg
        file_content = [line for line in file_content if line if float(line.split()[5]) > cutoffangle]

        # extract the data
        sta = [line.split()[0] for line in file_content if line]
        satellite_name = [line.split()[1] for line in file_content if line]
        d = [line.split()[2] for line in file_content if line]
        hms = [line.split()[3] for line in file_content if line]
        Az = np.deg2rad([float(line.split()[4]) for line in file_content if line])
        El = np.deg2rad([float(line.split()[5]) for line in file_content if line])
        st = [float(line.split()[6]) for line in file_content if line]
        
        # get the time and some other parameters
        epoch =  {i:[] for i in sorted(set(sta))}
        elevation = {i:[] for i in sorted(set(sta))}
        stec = {i:[] for i in sorted(set(sta))}
        satellite = {i:[] for i in sorted(set(sta))}
        for i in range(len(hms)):
            tt = [float(j) for j in hms[i].split(':')]
            epoch[sta[i]].append(tt[0]+tt[1]/60+tt[2]/60/60)
            elevation[sta[i]].append(El[i])
            stec[sta[i]].append(st[i])
            satellite[sta[i]].append(satellite_name[i])

        # get IPP
        phiIPP, lamIPP, slla = cls.getIPP(logger, session, sta, El, Az, slla, geomagnetic, modip, modip_grid)

        return sta, satellite, epoch, elevation, stec, phiIPP, lamIPP, slla
        
    
    @classmethod
    def column_index(cls, logger, nPara, t, time_windows, rel_constraints):

        '''This function finds the indices of time windows with observations and
        the indices of the corresponding parameters for the station.'''

        # four gradients: Gn and Gs
        g = 2

        # extract the number of observation per time interval per station
        c = np.zeros(shape = (nPara-1-g, 1))
        
        for i, item in enumerate(t):
            indx = [w for w in range(len(time_windows)-1) if time_windows[w] <= item <time_windows[w+1]]            
            c[indx[0], 0] +=1
        
        
        # define the (remaining) indices of the time windows with observations
        rcindx = np.ones(shape = (c.shape[0],c.shape[1]))
        
        # save the index of the parameters that don't have sufficient observations and are to be eliminated
        cindxe = []
        cindxr = [i for i in range(0, nPara)]
        for i in range(c.shape[1]):
            # if a station has no obs for the whole session, save the index of the instrumental delay and the gradients
            if (c[:,i] == 0).all():
                # two gradients: Gn and Gs
                cindxe.append((i+1)*nPara-2)
                cindxe.append((i+1)*nPara-1)

            # if a station has no obs for certain hours, save the index of the VTEC parameters
            for j in range(c.shape[0]):
                if c[j,i] == 0:
                    # stations, hours, parameter index in A matrix order
                    cindxe.append(i*nPara+j)               
                    # save the index of the station and the time window
                    rcindx[j,i] = 0

        # change cindxe from list to np.array
        cindxe = np.array(cindxe)

        # save the indices of the parameters with no observations to be used in VCE
        rel_cindxe = np.array(sorted(set(list(cindxe) + [nPara-1])))

        # if relative constraints are applied,
        if rel_constraints:         
            indx = []
            # re-fill the gaps
            for i in range(rcindx.shape[1]):
                for j in range(rcindx.shape[0]):
                    if rcindx[j,i] == 0:
                        # check whether the missing obs is bounded with obs
                        if (rcindx[0:j,i] == 1).any():
                            if (rcindx[j:rcindx.shape[0],i] == 1).any():
                                # if yes, change its value to 1
                                rcindx[j,i] = 1

                                # save the index of the corresponding parameter                            
                                indx.append(list(cindxe).index(i*nPara+j))

            # don't delete those parameters
            cindxe = np.delete(cindxe,indx, 0)
            

        # get the indices of the remaining parameters
        cindxr = np.delete(cindxr,cindxe.astype(int), 0)       

        return rel_cindxe, cindxe, cindxr, rcindx, c    
    
    
    @classmethod
    def nPara_time_window(cls, logger, t, resolution = 60):

        '''This function calculates the number of parameters and generates the time windows of the piece-wise linear offsets.'''

        startPoint = math.floor(min(t)) 
        endPoint = math.ceil(max(t))

        if 240 >= resolution >= 15: 

            # get the number of parameters per station
            # VTECs, Gn and Gs
            nPara = (math.floor((endPoint - startPoint)*(60/resolution))+1)+1+1

            # generate the time windows
            indices = np.arange(int((endPoint - startPoint)*(60/resolution)+1))
            time_windows = indices*(resolution/60)

            return nPara, time_windows
        
        else:
            logger.critical('Please, enter a resolution between 15 and 240 in min')
            sys.exit()
            
            
    @classmethod
    def get_geomagnetic_lats(cls, logger, lats, lons):

        '''This function calculates the geomagnetic latitude.'''

        # convert the latitude and longitude from radian to degrees    
        lats, lons = np.rad2deg(lats), np.rad2deg(lons)

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
    def getIPP(cls, logger, session, sta, El, Az, slla, geomagnetic, modip, modip_grid):

        '''This function calculates the latitude and longitude of ionospheric pierce point.'''

        # get the lat and lon of IPP
        phiIPP = {i:[] for i in sorted(set(sta))}
        lamIPP = {i:[] for i in sorted(set(sta))}
        for i in range(len(Az)):
            # Bull. Geod. Sci, Articles Section, Curitiba, v. 23, no4, p.669 - 683, Oct - Dec, 2017.
            # calculate the Earth-centred angle
            R = 6371.0
            h = 450 # 506.7 #

            Psi = np.pi/2 - El[i] - np.arcsin(6371.0/(6371.0+h)*np.cos(El[i]))

            # compute the latitude of the IPP
            lat = np.deg2rad(slla[sta[i]][0])   
            Phi = np.arcsin(np.sin(lat)*np.cos(Psi) + np.cos(lat)*np.sin(Psi)*np.cos(Az[i]))

            # compute the longitude of the IPP
            lon = np.deg2rad(slla[sta[i]][1])
            Lambda = lon + np.arcsin(np.sin(Psi)*np.sin(Az[i])/np.cos(Phi))

            phiIPP[sta[i]].append(Phi)
            lamIPP[sta[i]].append(Lambda)

        # convert the lats to geomagnetic lats or modified dip lats
        if geomagnetic:                
            # get the geomagnetic latitude for IPPs

            for key in sorted(set(sta)):
                phiIPP[key] = cls.get_geomagnetic_lats(logger, phiIPP[key], lamIPP[key])

            # get the geomagnetic latitude for all the stations
            for key, value in slla.items():
                slla[key][0] = np.rad2deg(cls.get_geomagnetic_lats(logger, np.deg2rad(value[0]), np.deg2rad(value[1])))


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

                # get the modifed dip latitude for IPPs and all the stations
                for key in sorted(set(sta)):
                    phiIPP[key] = [cls.interpolate_dips(logger, dips, lat, lamIPP[key][j])
                                                 for j, lat in enumerate(phiIPP[key])]
                for key, value in slla.items():
                    slla[key][0] = np.rad2deg(cls.interpolate_dips(logger, dips, np.deg2rad(value[0]), np.deg2rad(value[1])))


            else:
                # calculate for all points for accurate solution
                # get the modifed latitude for IPPs and all the stations
                for key in sorted(set(sta)):
                    phiIPP[key] = [cls.get_modips(logger, session, lat, lamIPP[key][j])
                                                 for j, lat in enumerate(phiIPP[key])]
                for key, value in slla.items():
                    slla[key][0] = np.rad2deg(cls.get_modips(logger, session, np.deg2rad(value[0]), np.deg2rad(value[1])))

        return phiIPP, lamIPP, slla


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
    def mapping_function(cls, logger, Elev0, modified_mf):    
        
        '''This function calculates the mapping function.'''

        R = 6371.0 

        if modified_mf:
            h = 506.7
            alpha = 0.9782
        else:
            h = 450
            alpha = 1 
            
        mf = 1/((1.0-(((R*np.cos(alpha*Elev0))/(R+h))**2))**0.5)
        
        return mf
    
        
    @classmethod
    def initial_values(cls, logger, nPara):  

        '''This function generates the initial values for the piece-wise linear offsets, and the ionospheric gradients.'''
        
        # generate some inital values for the VTECs and the gradients
        x0 = np.array([20 for i in range(nPara)])
        
        return x0
    
        
    @classmethod
    def design(cls, logger, nPara, x0, Elev0, lonIPP, lonSta, latIPP, latSta, t, time_windows, modified_mf):

        '''This function forms the design matrix A row by row.'''

        #### CONVERT station coords to rad
        lonSta = np.deg2rad(lonSta) 
        latSta = np.deg2rad(latSta) 

        #####

        # get the starting and ending of the time window and their corresponding indices
        if t  < time_windows[-1]:
            for i in range(time_windows.shape[0]):
                if time_windows[i] <= t < time_windows[i+1]:
                    indx1 = i
                    indx2 = i+1 # index of 
                    t1 = time_windows[i] # starting time of the window
                    t2 = time_windows[i+1] # ending time of the window
                    break
        else:        
            indx1 = time_windows.shape[0]-2
            indx2 = time_windows.shape[0]-1
            t1 = time_windows[-2]
            t2 = time_windows[-1]
            
        # get the initial values for the VTECs and the Gradients
        vtec1 = x0[indx1]
        vtec2 = x0[indx2]
        Gn = x0[nPara - 2]
        Gs = x0[nPara - 1]
        
        
        # get the mapping functions
        mf = cls.mapping_function(logger, Elev0, modified_mf)

        # create a design matrix corresponding to the observation in question
        Ai = np.zeros(shape = (nPara))
                
        # for north
        if (latIPP - latSta) >= 0:
            # derivative w.r.t vtec1
            Ai[indx1] = mf*(1+(latIPP-latSta)*Gn)*(1-(t + np.rad2deg(lonIPP - lonSta)/15.0 - t1)/(t2-t1))
            # derivative w.r.t vtec2
            Ai[indx2] = mf*(1+(latIPP-latSta)*Gn)*((t + np.rad2deg(lonIPP - lonSta)/15.0 - t1)/(t2-t1))
            # derivative w.r.t Gn
            Ai[nPara - 2] = mf*(latIPP - latSta)*(vtec1+((t + np.rad2deg(lonIPP - lonSta)/15.0 - t1)/(t2-t1))*(vtec2-vtec1))
        
        # for south
        else:
            # derivative w.r.t vtec1
            Ai[indx1] = mf*(1+(latIPP-latSta)*Gs)*(1-(t + np.rad2deg(lonIPP - lonSta)/15.0 - t1)/(t2-t1))
            # derivative w.r.t vtec2
            Ai[indx2] = mf*(1+(latIPP-latSta)*Gs)*((t + np.rad2deg(lonIPP - lonSta)/15.0 - t1)/(t2-t1))
            # derivative w.r.t Gs
            Ai[nPara - 1] = mf*(latIPP - latSta)*(vtec1+((t + np.rad2deg(lonIPP - lonSta)/15.0 - t1)/(t2-t1))*(vtec2-vtec1))


        return Ai
    
    
    @classmethod
    def observed_computed(cls, logger, nPara, x0, stec, Elev0, lonIPP, lonSta, latIPP, latSta, t, time_windows, modified_mf):

        '''This function forms the vector of reduced observations.'''

        #### CONVERT station coords to rad
        lonSta = np.deg2rad(lonSta) 
        latSta = np.deg2rad(latSta) 

        #####

        # get the starting and ending of the time window and their corresponding indices
        if t  < time_windows[-1]:
            for i in range(time_windows.shape[0]):
                if time_windows[i] <= t < time_windows[i+1]:
                    indx1 = i
                    indx2 = i+1 # index of 
                    t1 = time_windows[i] # starting time of the window
                    t2 = time_windows[i+1] # ending time of the window
                    break
        else:        
            indx1 = time_windows.shape[0]-2
            indx2 = time_windows.shape[0]-1
            t1 = time_windows[-2]
            t2 = time_windows[-1]
            
        # get the initial values for the VTECs and the Gradients
        vtec1 = x0[indx1]
        vtec2 = x0[indx2]
        Gn = x0[nPara - 2]
        Gs = x0[nPara - 1]
        
        
        # get the mapping functions
        mf = cls.mapping_function(logger, Elev0, modified_mf)
        
                
        # for north
        if (latIPP - latSta) >= 0:
            func_x = mf*(1+(latIPP-latSta)*Gn)*(vtec1+((t + np.rad2deg(lonIPP - lonSta)/15.0 - t1)/(t2-t1))*(vtec2-vtec1))
                    
        # for south
        else:
            func_x = mf*(1+(latIPP-latSta)*Gs)*(vtec1+((t + np.rad2deg(lonIPP - lonSta)/15.0 - t1)/(t2-t1))*(vtec2-vtec1))
        
        return stec - func_x
    

    @classmethod
    def obs_weights(cls, logger, elev_angle):

        '''This function calculates the weigts for GNSS observations.'''

        # calculate the weight matrix from scratch if no observations flagged as an outliers

        # calculate the elevation-dependent weights of the observations
        # weight is proportional to elevation angle
        ew = np.sin(elev_angle)

        # calculate the final weights
        W = np.diag(ew) # np.identity(np.diag(ew).shape[0])

        return W
    

    @classmethod
    def variance_component_estimation(cls, logger, sat, W, r, A, rel_cindxe, satellite_based = 1):

        '''This function estimates the variance components per radio satellite, generating a new weighting matrix.'''

        # apply VCE only once the data is free from outliers
        
        # delete the column of the parameters with no observation but are relatively constraints
        a = np.delete(A, rel_cindxe, 1)

        # get the normal equations
        neqA = np.transpose(a).dot(W).dot(a)

        # calculate the co-variance matrix of the estimates    
        QxxA = np.linalg.inv(neqA)

        # calculate the co-variance matrix of the residuals
        QvvA = np.linalg.inv(W) - a.dot(QxxA).dot(np.transpose(a))

        # calculate the redundancy matrix
        RA = QvvA.dot(W)

        # save the input weighting matrix to be used in the estimation of the variance components
        W0 = W

        # apply satellite-based VCE
        if satellite_based:

            indx = {} # indices of residuals per satellite
            vPs = {} # variance component per satellite 

            for i in set(sat):            

                # get the indices of residuals per satellite
                indx[i] = [j for j in range(len(r))  if sat[j] == i]

                # get the variance component of unit weight per satellite group
                vPs[i] = np.transpose(r[indx[i]]).dot(np.diag(W0[indx[i],indx[i]])).dot(r[indx[i]])/sum(RA[indx[i],indx[i]])
                #logger.debug(vPs[i],len(indx[i]))

                # scale the weight of each group by its variance component
                W[indx[i],indx[i]] = W[indx[i],indx[i]]/vPs[i]

        return W
    
    
    @classmethod
    def pseudo_obs(cls, logger, nPara, cindxe):

        '''This function applies relative constraints between the piece-wise linear offsets using pseudo observations.'''

        # number of gradients: Gn and Gs
        g = 2

        # initialize some variables for the design matrix of the pseudo-observations  
        H = np.zeros(shape=(nPara-1-g, nPara))    
        # sub-constrain matrix of H
        # Hi = np.zeros(shape=(nPara-1-g, nPara-g)) 
        # sub-constrain matrix of W
        Wc = np.zeros(shape=(nPara-1-g, (nPara-1-g)))
        # vector of residuals
        h = np.zeros(shape=(nPara-1-g))

        # sigma of delta VTEC
        std_deltaV = 30    

        # get those matrices        
        for i in range(nPara-1-g):
            H[i,i] = 1
            H[i, i+1] = -1          

        # weight matrix
        Wc = np.diag([1/std_deltaV**2 for j in range(nPara-1-g)])
        # h[n*(nPara-1-g-1):(n+1)*(nPara-1-g-1)] = -(x0[n*nPara:(n+1)*nPara-1-g-1] - x0[n*nPara+1:(n+1)*nPara-g-1])


        # delete the last column representing the instrumental offset of the last station as a constraint
        # delete the columns of the parameters / time windows with no observations
        H = np.delete(H, cindxe.astype(int), 1)

        # find the rows corresponding to the missing parameters
        sub_rows = [((i+1)//nPara)*(nPara-1-g)+(i+1)%nPara-1 for i in cindxe 
                    if (i+1)%nPara != nPara-g and (i+1)%nPara != nPara-2 and (i+1)%nPara != nPara-1 and (i+1)%nPara != 0] 
        rows = [i for i in sorted(set(sub_rows + list(np.array(sub_rows)-1))) if i != -1]

        # delete those rows 
        H = np.delete(H, rows, 0)
        h = np.delete(h, rows, 0)
        Wc = np.delete(Wc, rows, 0)
        Wc = np.delete(Wc, rows, 1)

        return H, h, Wc


    @classmethod
    def g_lsq(cls, logger, x0, rel_cindxe, cindxe, cindxr, elev_angle, lonIPPs, lonSta, latIPPs, latSta,
              stec, epochs, sat, W, resolution, modified_mf, rel_constraints):

        '''This function performs the LSQ adjustment to estimate VTEC time series from GNSS observations.'''

        # get the # of parameters and the time windows
        nPara, time_windows = cls.nPara_time_window(logger, epochs, resolution)
        
        # initialize some variable
        A = np.zeros(shape = (len(epochs),int(nPara)))
        b = np.zeros(shape = (len(epochs)))
        
                
        # get the estimates
        niter_0 = 0
        rchisqr_before = 1
        while True:            

            # form the A matrix
            for i in range(len(epochs)):
                A[i,:] = cls.design(logger, int(nPara), x0, elev_angle[i], lonIPPs[i], lonSta, latIPPs[i], latSta, epochs[i], 
                                    time_windows, modified_mf)
                b[i] = cls.observed_computed(logger, int(nPara), x0, stec[i], elev_angle[i], lonIPPs[i], lonSta, latIPPs[i], latSta,
                                             epochs[i], time_windows, modified_mf)

            if rel_constraints:     
                
                # get the parameters of the pseudo-observations
                H, h, Wc = cls.pseudo_obs(logger, nPara, cindxe)  

                # delete the columns of the parameters with no observations from the A matrix 
                a = np.delete(A, cindxe.astype(int), 1)  


                # form the matric of the lsq
                neqA = np.transpose(a).dot(W).dot(a)  
                neqH = np.transpose(H).dot(Wc).dot(H)            
                neqT = neqA + neqH 

                f = np.transpose(a).dot(W).dot(b) + np.transpose(H).dot(Wc).dot(h)            

                # calculate the corrections for the estimates
                dx = np.linalg.inv(neqT).dot(f)  


                # get the residuals
                r = a.dot(dx) - b   
                rh = H.dot(dx) - h


                # calculate the degree of freedom
                dof = len(r)-len(cindxr)+(len(rel_cindxe)-len(cindxe))#-nPara + H.shape[0]

                # calculate the reduced-chi squared (reference variance)
                rchisqr = (np.transpose(r).dot(W).dot(r) + np.transpose(rh).dot(Wc).dot(rh))/dof

            else:

                # delete the columns of the parameters with no observations from the A matrix 
                a = np.delete(A, cindxe.astype(int), 1)


                # form the matric of the lsq
                neq = np.transpose(a).dot(W).dot(a)

                # get the estimates
                dx = np.linalg.inv(neq).dot(np.transpose(a).dot(W).dot(b))

                # logger.debug(np.transpose(a).dot(W).dot(b)) # np.argwhere(np.isnan(np.transpose(a).dot(W).dot(b)))

                # get the residuals
                r = a.dot(dx) - b

                # calculate the degree of freedom
                dof = len(r)-nPara

                # calculate the reduced-chi squared (reference variance)
                rchisqr = np.transpose(r).dot(W).dot(r)/dof
                # logger.debug(rchisqr)   

            # add the corrections to the estimates
            indx = [i for i in range(cindxr.shape[0])]
            x0 = x0[cindxr] + dx[indx]

            
            niter_0 += 1
            # logger.debug('rchisqr_0', rchisqr, abs(rchisqr_before-rchisqr))
            # iterate for at least the min. # of iteration, i.e. 3 times
            # break if the change in the reference variance is below the threshold
            # or the number of iterations reaches the max. # of iterations 
            if abs(rchisqr-rchisqr_before) < 1e-2 and niter_0 > 5 or niter_0 > 1e1:    
                break
            rchisqr_before = rchisqr
                                   
                
        sxx = np.zeros(nPara)
        # generate statistics
        if rel_constraints: 
            # calculate sigma
            s0 = np.sqrt(rchisqr)

            # calculate the co-variance matrix of the estimates
            Qxx = np.linalg.inv(neqT)

            # get the formal errors of the estimates
            _sxx = s0*np.sqrt(abs(np.diag(Qxx)))
                        
            # map the formal errors to the estimates
            sxx[cindxr] = _sxx[indx]
            
            
        else:
            
            # calculate sigma
            s0 = np.sqrt(rchisqr)

            # calculate the co-variance matrix of the estimates
            Qxx = np.linalg.inv(neq)

            # get the formal errors of the estimates
            _sxx = s0*np.sqrt(abs(np.diag(Qxx)))
            
            # map the formal errors to the estimates
            sxx[cindxr] = _sxx[indx]
            
            
        return x0, sxx, A, Qxx, rchisqr, r
    
    
    
    @classmethod
    def data_snooping(cls, logger, x, rel_cindxe, cindxe, cindxr,
                      elev, lamIPP, lonSta, phiIPP, latSta,
                      stec, epoch, satellite, resolution, 
                      modified_mf, W, rel_constraints, station):
        
        logger.info(f'outlier detection is running for station {station} ..')
        
        while True:            

            # get the estimates without relative constraints for the sake of simplicity
            x, sxx, A, Qxx, rchisqr, r = cls.g_lsq(logger, x, rel_cindxe, cindxe, cindxr,
                                                   elev, lamIPP, lonSta, phiIPP, latSta,
                                                   stec, epoch, satellite, W, resolution, 
                                                   modified_mf, rel_constraints = 0)

            # delete the columns of the parameters with no observations from the A matrix 
            a = np.delete(A, cindxe.astype(int), 1)


            # calculate the co-variance matrix of the residuals
            Qvv = np.linalg.inv(W) - a.dot(Qxx).dot(np.transpose(a))

            # calculate the standardized residuals
            r_ = abs(r)/np.sqrt(abs(np.diag(Qvv)))

            # get the index of the observation with the maximum normalized residual
            indx = list(r_).index(max(r_))

            # calculate sigma
            s0 = np.sqrt(rchisqr)

            # logger.debug(f'{station}: {r_[indx]}, {3.29*s0}')

            # using the student test, check whether the corresponding observation is an outlier
            # 1- aplha the significance level of the test, and 1 - beta the power of the test.
            # 6.6 corrosponds to alpha = 0.001 and beta = 0.999 >>> confidence level 99.9%
            # 3.29 as a rejection criteria corrosponds to alpha = 0.001  and beta =  >>> confidence level 99.9%
            if r_[indx] > 3.29*s0: # 3.29, 6.6
                #logger.debug('indxr', list(abs(r)).index(max(abs(r))), 'maxr', round(max(abs(r)),3), 'cr_', 
                #      round(float(r_[list(abs(r)).index(max(abs(r)))]),3), 'indxr_', indx, 'maxr_', 
                #      round(float(r_[indx]),3), 'cr', round(float(r[indx]),3), 'rej', round(3.29*s0,3))

                # if yes, remove it
                # extract the observations
                del elev[indx], lamIPP[indx], phiIPP[indx]
                del stec[indx], epoch[indx], satellite[indx]

                # delete the row and column of the observations flagged as an outlier
                W = np.delete(W, indx, 0)
                W = np.delete(W, indx, 1)

            else:
                # get the estimates with relative constraint if applied
                x, sxx, A, Qxx, rchisqr, r = cls.g_lsq(logger, x, rel_cindxe, cindxe, cindxr,
                                                       elev, lamIPP, lonSta, phiIPP, latSta,
                                                       stec, epoch, satellite, W, resolution, 
                                                       modified_mf, rel_constraints)

                logger.info(f'for station {station}, all possible outliers were eliminated.')

                break   

        return x, sxx, A, Qxx, rchisqr, r, W, elev, lamIPP, phiIPP, stec, epoch, satellite
    
    
    
    @classmethod
    def g_plot(cls, logger, cindxr, time_windows, t, session, resolution, station, x, sxx, path = 'Results/GNSS/', plot_format = 'jpg'):

        '''This function plots the VTEC time series for GNSS stations.'''

        # get the figure ready
        # get_ipython().run_line_magic('matplotlib', 'notebook')
        # %matplotlib notebook
        plt.rcParams["figure.figsize"] = (10,4)
        # adjust the linewidth
        plt.rcParams['lines.linewidth'] = 2
        plt.rcParams['axes.linewidth'] = 1.5
        # adjust the font
        plt.rcParams.update({'font.size': 10})
        
        startPoint = math.floor(min(t))
        
        # get the indices and epochs
        indx = []
        epochs = []
        
        g = 2
                
        for i, item in enumerate(cindxr[:-g]):
            
            epoch = startPoint+time_windows[item]*resolution/60
            
            
            if i:
                if epoch - epoch0 != resolution/60 or i == cindxr[:-g].shape[0]-1:
                    # append the index to the list of indices & the epoch to the list of epochs if it's the last epoch
                    if  i == cindxr[:-g].shape[0]-1:
                        indx.append(i)
                        epochs.append(epoch)
                          
                    plt.errorbar(epochs, x[indx], yerr=sxx[indx], c='k', label = f'{station} GNSS')# if unique_label == 0 else "")

                    # reset the epochs and indices
                    indx = []
                    epochs = []
                            
            # append the index to the list of indices and the epoch to the list of epochs
            indx.append(i)
            epochs.append(epoch) 
            
            # save the epoch
            epoch0 = epoch  

        # create a legend with unique labels
        handles, labels = plt.gca().get_legend_handles_labels()
        by_label = dict(zip(labels, handles))
        plt.legend(by_label.values(), by_label.keys())
    
        plt.title(station + '_VTECs on ' + session)
        #plt.show()


        if not os.path.exists(path):
            # create the directory to save the plots
            os.makedirs(path)

        plt.savefig(os.path.join(path + f'{station}.{plot_format}'), dpi = 1000, bbox_inches='tight')
        plt.close('all')


    @classmethod
    def save_results(cls, logger, cindxr, x, sxx, session, epoch, resolution, path = 'Results/GNSS/'):

        '''This function saves the estimated parameters in a text file.'''
        
        # set the number of gradients
        g = 2

        # extract the year 
        year = 2000 + int(session[0:2])

        # create the path if missing
        if not os.path.exists(path):
            os.makedirs(path)

        # open a text file   
        with open(path + session +'.txt','w') as file: # 'n' for new

            # write the header
            file.write('{0:^9}'.format('station') + '{0:^9}'.format('date') +
                              '{0:^9}'.format('time') + '{0:^9}'.format('vtec') + '{0:^9}'.format('vtec_sigma') + '\n')

            for station in x.keys():
                nPara, time_windows = cls.nPara_time_window(logger, epoch[station], resolution)
                indx = 0
                for i, item in enumerate(x[station][:-g]):                      
                    file.write('{0:^9}'.format(station) + '{0:^9}'.format(session) + 
                                      '{0:^9}'.format(str(time_windows[cindxr[indx]])) + '{0:^9}'.format(str(np.round(item,3))) + 
                                      '{0:^9}'.format(str(np.round(sxx[station][i],3))) +'\n')
                    indx +=1
            file.write('\n')

            # four gradients: Gn and Gs
            # append the ionospheric gradients to the file
            file.write('{0:^9}'.format('station') + '{0:^9}'.format('date') +
                              '{0:^9}'.format('Gn') +
                              '{0:^11}'.format('Gn_sigma') + 
                              '{0:^9}'.format('Gs') +
                              '{0:^11}'.format('Gs_sigma') + '\n')

            for station in x.keys():
                file.write('{0:^9}'.format(station) + '{0:^9}'.format(session) +
                                  '{0:^9}'.format(str(np.round(x[station][-2],3))) +
                                  '{0:^11}'.format(str(np.round(sxx[station][-2],3))) +
                                  '{0:^9}'.format(str(np.round(x[station][-1],3))) +
                                  '{0:^11}'.format(str(np.round(sxx[station][-1],3))) +'\n')
            file.write('\n')

        file.close()
        

        
    @classmethod
    def g_processing(cls, logger, session, resolution = 60, cutoffangle = 5, vce = 1, modified_mf = 1,
                     geomagnetic = 0, modip = 1, modip_grid = 1, outlier_detection = 1, rel_constraints = 1,
                     g_input_path = '', g_output_path = '', plot_format = 'png'):

        '''This function derives VTEC time series from GNSS observations.'''

        # get the path
        if g_input_path: 
            g_input_path = g_input_path + 'Data/GNSS/'
        else:
            g_input_path = 'Data/GNSS/'

        if g_output_path:
            g_output_path = g_output_path + 'Results/GNSS/'
        else:
            g_output_path = 'Results/GNSS/'

        # get GNSS data
        sta, satellite, epoch, elev, stec, phiIPP, lamIPP, slla = cls.g_data(logger, session, geomagnetic, modip, modip_grid, 
                                                                             cutoffangle, g_input_path)

        x, sxx = {}, {}
        for station in sorted(set(sta)):
            try:
                        
                # get the # of parameters and the time windows
                nPara, time_windows = cls.nPara_time_window(logger, epoch[station], resolution)

                # 
                rel_cindxe, cindxe, cindxr, rcindx, c = cls.column_index(logger, nPara, epoch[station], time_windows, rel_constraints)
                # print(cindxr)
                

                ####
                
                # get the initial values
                x0 = cls.initial_values(logger, nPara)

                
                if outlier_detection:
                    
                    # get the elevation-dependent weight matrix
                    W = cls.obs_weights(logger, elev[station])
                    
                    # detect and eliminate the outliers in GNSS observations without applying relative constraints
                    x[station], sxx[station], A, Qxx, rchisqr, r, W, \
                    elev[station], lamIPP[station], phiIPP[station], stec[station], epoch[station], satellite[station] = \
                    cls.data_snooping(logger, x0, rel_cindxe, cindxe, cindxr, elev[station],
                                      lamIPP[station], slla[station][1], phiIPP[station],
                                      slla[station][0], stec[station], epoch[station],
                                      satellite[station], resolution, modified_mf, W,
                                      rel_constraints = 0, station = station)
                    
                else:

                    # get the elevation-dependent weight matrix
                    W = cls.obs_weights(logger, elev[station])

                    # get the estimates
                    x[station], sxx[station], A, Qxx, rchisqr, r = cls.g_lsq(logger, x0, rel_cindxe, cindxe, cindxr,
                                                                             elev[station], lamIPP[station], slla[station][1], 
                                                                             phiIPP[station], slla[station][0], stec[station], 
                                                                             epoch[station], satellite[station], W, resolution,
                                                                             modified_mf, rel_constraints)

                # logger.debug(f'{station}: {rchisqr}')

                #####

                # estimate variance component per satellite
                if vce:
                    
                    niter_1 = 0    
                    while True:

                        # finesse the stochastic model and redo the adjustment
                        W = cls.variance_component_estimation(logger, satellite[station], W, r, A, rel_cindxe)
                        
                        # get the initial values
                        x0 = np.array(x[station])

                        # get the estimates
                        x[station], sxx[station], A, Qxx, rchisqr, r = cls.g_lsq(logger, x0, rel_cindxe, cindxe, cindxr,
                                                                                 elev[station], lamIPP[station], 
                                                                                 slla[station][1], phiIPP[station], slla[station][0],
                                                                                 stec[station], epoch[station], satellite[station], W,
                                                                                 resolution, modified_mf, rel_constraints)

                        # logger.debug(f'{station}: {rchisqr}')

                        niter_1 += 1
                        # iterate for at least the min. # of iteration, e.g. 2 times
                        # break if the change in the reference variance is below the threshold
                        # or the number of iterations reaches the max. # of iterations 
                        if abs(1-rchisqr) < 1e-2 and niter_1 >= 5 or niter_1 > 1e1: 
                            break


                # plot the estimates
                cls.g_plot(logger, cindxr, time_windows, epoch[station], session, resolution, station, x[station], sxx[station], 
                           g_output_path + session + '/', plot_format)

                logger.info(f'Successfully processed station {station} in campaign {session}')

            except Exception as e:
                logger.error(f'failed to process station {station} in campaign {session}')
                logger.debug(e)
                continue
        
        # save the results in a text file and plot the time series
        cls.save_results(logger, cindxr, x, sxx, session, epoch, resolution, path = g_output_path + session + '/')

        return x, sxx
    
