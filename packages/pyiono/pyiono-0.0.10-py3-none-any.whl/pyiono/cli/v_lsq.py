
import numpy as np
import statistics
import math
import random

import datetime
import time

import v_data
import GTMs

class v_lsq:
    
    def __ini__(self):
        pass
    
    
    @classmethod
    def nPara_time_window(cls, logger, t, gradient = 1, resolution = 60):

        '''This function calculates the number of parameters and generates the time windows of the piece-wise linear offsets.'''

        # get the start and end hours of the session
        startPoint = math.floor(min(t)) 
        endPoint = math.ceil(max(t))

        # or resolution == 30 or resolution == 60 or resolution == 120 or resolution == 180: 
        if 240 >= resolution >= 15:
            # eith Gn and Gs, or Gns
            if gradient:
                # two gradients: Gn and Gs
                # get the number of parameters per station
                # VTECs, Gn, Gs, and Instr
                nPara = (math.floor((endPoint - startPoint)*(60/resolution))+1)+1+1+1
            else:
                # one gradient: Gns
                # get the number of parameters per station
                # VTECs, Gns, and Instr
                nPara = (math.floor((endPoint - startPoint)*(60/resolution))+1)+1+1

            # generate the time windows
            indices = np.arange(int((endPoint - startPoint)*(60/resolution)+1))
            time_windows = indices*(resolution/60)

            return nPara, time_windows

        else:
            logger.critical('Please, enter a resolution between 15 and 240 in min')
            sys.exit()

            
    @classmethod
    def column_index(cls, logger, nSta, nPara, s1n, s2n, t, time_windows, rel_constraints, sum_instr_offsets, gradient):

        '''This function finds the indices of time windows with observations and
        the indices of the corresponding parameters per geodetic VLBI/VGOS station.'''

        # handle the gradient
        if gradient:
            # two gradients: Gn and Gs
            g = 2
        else:
            # one gradient: Gns
            g = 1

        # extract the number of observation per time interval per station
        c1 = np.zeros(shape = (nPara-1-g-1,nSta)) # 1st station in the baseline
        c2 = np.zeros(shape = (nPara-1-g-1,nSta)) # 2nd station in the baseline

        for i, item in enumerate(s1n):
            indx = [w for w in range(len(time_windows)-1) if time_windows[w] <= t[i] <time_windows[w+1] ]
            c1[indx[0], int(item-1)] +=1

        for i, item in enumerate(s2n):
            indx = [w for w in range(len(time_windows)-1) if time_windows[w] <= t[i] <time_windows[w+1] ]
            c2[indx[0], int(item-1)] +=1

        # conacate the lists of the stations
        c = c1+c2

        # define the (remaining) indices of the time windows with observations
        rcindx = np.ones(shape = (c.shape[0],c.shape[1]))

        # save the index of the parameters that don't have sufficient observations and are to be eliminated
        cindxe = []
        cindxr = [i for i in range(0,nSta*nPara)]
        for i in range(c.shape[1]):
            # if a station has no obs for the whole session, save the index of the instrumental delay and the gradients
            if (c[:,i] == 0).all():
                cindxe.append((i+1)*nPara-1)
                if gradient:
                    # two gradients: Gn and Gs
                    cindxe.append((i+1)*nPara-2)
                    cindxe.append((i+1)*nPara-3)
                else:
                    # one gradient: Gns
                    cindxe.append((i+1)*nPara-2)

            # if a station has no obs for certain hours, save the index of the VTEC parameters
            for j in range(c.shape[0]):
                if c[j,i] == 0: 
                    # stations, hours, parameter index in A matrix order
                    cindxe.append(i*nPara+j)               
                    # save the index of the station and the time window
                    rcindx[j,i] = 0
                    # deal with the last parameter in the series
                    if j == len(c[:,i])-1:
                        cindxe.append(i*nPara+j+1)

        # change cindxe from list to np.array
        cindxe = np.array(cindxe)

        # save the indices of the parameters with no observations to be used in VCE
        rel_cindxe = np.array(sorted(set(list(cindxe) + [nSta*nPara-1])))

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

        if not sum_instr_offsets:        
            # delete also the last column representing the instrumental offset of the last station as a constraint
            cindxe = np.array(sorted(set(list(cindxe) + [nSta*nPara-1])))

        # get the indices of the remaining parameters
        cindxr = np.delete(cindxr,cindxe.astype(int), 0)       

        return rel_cindxe, cindxe, cindxr, rcindx, c
            

    @classmethod
    def initial_values(cls, logger, nSta, nPara, rcindx, gradient):  

        '''This function generates the initial values for the piece-wise linear offsets, 
        ionospheric gradients and instrumental offsets.'''

        # create a variable for the estimates
        x0 = np.zeros(shape = (nSta * nPara))    

        # loop over the stations
        for j in range(nSta):        
            # set the initial values of the instrumental delay and ionospheric gradients
            x0[((j+1)*nPara-1)] = random.uniform(-5,5)

            if gradient:
                # two gradient: Gn and Gs
                x0[(j+1)*nPara-3:(j+1)*nPara-1] = [random.uniform(-1,1) for i in range((j+1)*nPara-3,(j+1)*nPara-1)]
            else:
                # one gradient: Gns
                x0[(j+1)*nPara-2] = random.uniform(-1,1)

            # get the initial values of the VTEC estimates from GIMs 
            for i in range(rcindx.shape[0]):
                if rcindx[i,j] != 0:
                    # vtec
                    x0[j*nPara+i] = random.uniform(2,20)

            if rcindx[i,j] != 0:
                # vtec
                x0[j*nPara+i+1] = random.uniform(2,20)

        # set the instrumental delay of the last station to zero as a constraint
        x0[((j+1)*nPara-1)] = 0

        return x0
    
    @classmethod
    def mapping_function(cls, logger, elev1, elev2, modified_mf = 1):

        '''This function maps the slant total electron content (STEC) to the vertical total electron content (VTEC).
        It has two options: the standard mapping function and the modified mapping function.'''

        # the mean radius of the Earth in km
        R = 6371.0

        if modified_mf:
            # the height of th ionospheric layer in km
            h = 506.7

            # alpha parameter
            alpha = 0.9782

            # get the mapping function
            mf1 = 1.0/((1.0-(((R*np.cos(alpha*elev1))/(R+h))**2))**0.5)
            mf2 = 1.0/((1.0-(((R*np.cos(alpha*elev2))/(R+h))**2))**0.5)

        else:
            # the mean radius of the Earth and the height of th ionospheric layer in km
            h = 450.0

            # get the mapping function
            mf1 = 1.0/((1.0-(((R*np.cos(elev1))/(R+h))**2))**0.5)
            mf2 = 1.0/((1.0-(((R*np.cos(elev2))/(R+h))**2))**0.5)

        return mf1, mf2
    
    
    @classmethod
    def design(cls, logger, x, freq, nSta, 
               nPara, s1n, s2n, Elev1, Elev2, 
               lonIPP1, lonIPP2, lonSta1, lonSta2, 
               latIPP1, latIPP2, latSta1, latSta2, 
               t, time_windows, modified_mf, gradient):

        '''This function forms the design matrix A row by row.'''

        # get the mapping functions
        mf1, mf2 = cls.mapping_function(logger, Elev1, Elev2, modified_mf)

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


        # vtec
        vtec11 = x[(s1n-1)*nPara + indx1]
        vtec12 = x[(s1n-1)*nPara + indx2]
        vtec21 = x[(s2n-1)*nPara + indx1]
        vtec22 = x[(s2n-1)*nPara + indx2] 

        # create a design matrix corresponding to the observation in question
        Ai = np.zeros(shape = (nSta*nPara))

        if gradient:
            # two gradient: Gn and Gs
            # ionospheric latitudinal gradient
            Gn1 = x[s1n*nPara - 3]    
            Gs1 = x[s1n*nPara - 2]
            Gn2 = x[s2n*nPara - 3]    
            Gs2 = x[s2n*nPara - 2]    


            # 1st station in the baseline
            if (latIPP1-latSta1) >= 0:
                # derivative w.r.t vtec11
                Ai[(s1n-1)*nPara + indx1] = \
                -mf1*(1+(latIPP1-latSta1)*Gn1)*(1-(t + np.rad2deg(lonIPP1 - lonSta1)/15.0 - t1)/(t2-t1))
                # derivative w.r.t vtec12
                Ai[(s1n-1)*nPara + indx2] = \
                -mf1*(1+(latIPP1-latSta1)*Gn1)*(t + np.rad2deg(lonIPP1 - lonSta1)/15.0 - t1)/(t2-t1)
                # derivative w.r.t Gn1
                Ai[s1n*nPara - 3] = \
                -mf1*(latIPP1-latSta1)*(vtec11+((t + np.rad2deg(lonIPP1 - lonSta1)/15.0 - t1)/(t2-t1))*(vtec12-vtec11))
            else:
                # derivative w.r.t vtec11
                Ai[(s1n-1)*nPara + indx1] = \
                -mf1*(1+(latIPP1-latSta1)*Gs1)*(1-(t + np.rad2deg(lonIPP1 - lonSta1)/15.0 - t1)/(t2-t1))
                # derivative w.r.t vtec12
                Ai[(s1n-1)*nPara + indx2] = \
                -mf1*(1+(latIPP1-latSta1)*Gs1)*(t + np.rad2deg(lonIPP1 - lonSta1)/15.0 - t1)/(t2-t1)
                # derivative w.r.t Gs1
                Ai[s1n*nPara - 2] = \
                -mf1*(latIPP1-latSta1)*(vtec11+((t + np.rad2deg(lonIPP1 - lonSta1)/15.0 - t1)/(t2-t1))*(vtec12-vtec11))
            # derivative w.r.t instr1
            Ai[s1n*nPara - 1] = -1

            # 2nd station in the baseline
            if (latIPP2-latSta2) >= 0:
                # derivative w.r.t vtec21
                Ai[(s2n-1)*nPara + indx1] = \
                mf2*(1+(latIPP2-latSta2)*Gn2)*(1-(t + np.rad2deg(lonIPP2 - lonSta2)/15.0 - t1)/(t2-t1))
                # derivative w.r.t vtec22
                Ai[(s2n-1)*nPara + indx2] = \
                mf2*(1+(latIPP2-latSta2)*Gn2)*(t + np.rad2deg(lonIPP2 - lonSta2)/15.0 - t1)/(t2-t1)
                # derivative w.r.t Gn2
                Ai[s2n*nPara - 3] = \
                mf2*(latIPP2-latSta2)*(vtec21+((t + np.rad2deg(lonIPP2 - lonSta2)/15.0 - t1)/(t2-t1))*(vtec22-vtec21))
            else:
                # derivative w.r.t vtec21
                Ai[(s2n-1)*nPara + indx1] = \
                mf2*(1+(latIPP2-latSta2)*Gs2)*(1-(t + np.rad2deg(lonIPP2 - lonSta2)/15.0 - t1)/(t2-t1))
                # derivative w.r.t vtec22
                Ai[(s2n-1)*nPara + indx2] = \
                mf2*(1+(latIPP2-latSta2)*Gs2)*(t + np.rad2deg(lonIPP2 - lonSta2)/15.0 - t1)/(t2-t1)
                # derivative w.r.t Gs2
                Ai[s2n*nPara - 2] = \
                mf2*(latIPP2-latSta2)*(vtec21+((t + np.rad2deg(lonIPP2 - lonSta2)/15.0 - t1)/(t2-t1))*(vtec22-vtec21))
            # derivative w.r.t instr2
            Ai[s2n*nPara - 1] = 1

        else:        
            # one gradient: Gns
            # ionospheric latitudinal gradient
            Gns1 = x[s1n*nPara - 2] 
            Gns2 = x[s2n*nPara - 2]    


            # 1st station in the baseline        
            # derivative w.r.t vtec11
            Ai[(s1n-1)*nPara + indx1] = \
            -mf1*(1+(latIPP1-latSta1)*Gns1)*(1-(t + np.rad2deg(lonIPP1 - lonSta1)/15.0 - t1)/(t2-t1))
            # derivative w.r.t vtec12
            Ai[(s1n-1)*nPara + indx2] = \
            -mf1*(1+(latIPP1-latSta1)*Gns1)*(t + np.rad2deg(lonIPP1 - lonSta1)/15.0 - t1)/(t2-t1)
            # derivative w.r.t Gn1
            Ai[s1n*nPara - 2] = \
            -mf1*(latIPP1-latSta1)*(vtec11+((t + np.rad2deg(lonIPP1 - lonSta1)/15.0 - t1)/(t2-t1))*(vtec12-vtec11))
            # derivative w.r.t instr1
            Ai[s1n*nPara - 1] = -1

            # 2nd station in the baseline
            # derivative w.r.t vtec21
            Ai[(s2n-1)*nPara + indx1] = \
            mf2*(1+(latIPP2-latSta2)*Gns2)*(1-(t + np.rad2deg(lonIPP2 - lonSta2)/15.0 - t1)/(t2-t1))
            # derivative w.r.t vtec22
            Ai[(s2n-1)*nPara + indx2] = \
            mf2*(1+(latIPP2-latSta2)*Gns2)*(t + np.rad2deg(lonIPP2 - lonSta2)/15.0 - t1)/(t2-t1)
            # derivative w.r.t Gn2
            Ai[s2n*nPara - 2] = \
            mf2*(latIPP2-latSta2)*(vtec21+((t + np.rad2deg(lonIPP2 - lonSta2)/15.0 - t1)/(t2-t1))*(vtec22-vtec21))
            # derivative w.r.t instr2
            Ai[s2n*nPara - 1] = 1

        return Ai

    
    @classmethod
    def observed_computed(cls, logger, x, freq, nSta, nPara, s1n, s2n, Elev1, Elev2, 
                          lonIPP1, lonIPP2, lonSta1, lonSta2, 
                          latIPP1, latIPP2, latSta1, latSta2, 
                          y, t, time_windows, modified_mf, gradient):

        '''This function forms the vector of reduced observations.'''

        # get the mapping functions
        mf1, mf2 = cls.mapping_function(logger, Elev1, Elev2, modified_mf)        

        # get the starting and ending of the time window and their corresponding indices
        if t  < time_windows[-1]:
            for i in range(time_windows.shape[0]):
                if time_windows[i] <= t < time_windows[i+1]:
                    indx1 = i 
                    indx2 = i+1 # index of 
                    t1 = time_windows[i] # starting of the time window
                    t2 = time_windows[i+1] # ending of the time window
                    break
        else:
            indx1 = time_windows.shape[0]-2
            indx2 = time_windows.shape[0]-1
            t1 = time_windows[-2]
            t2 = time_windows[-1]

        # instrumental delay constant
        instr1 = x[s1n*nPara - 1]    
        instr2 = x[s2n*nPara - 1]

        # vtec
        vtec11 = x[(s1n-1)*nPara + indx1]
        vtec12 = x[(s1n-1)*nPara + indx2]
        vtec21 = x[(s2n-1)*nPara + indx1]
        vtec22 = x[(s2n-1)*nPara + indx2]

        if gradient:
            # two gradient: Gn and Gs
            # ionospheric latitudinal gradient
            Gn1 = x[s1n*nPara - 3]    
            Gs1 = x[s1n*nPara - 2]
            Gn2 = x[s2n*nPara - 3]  
            Gs2 = x[s2n*nPara - 2]

            # 1st station    
            if (latIPP1-latSta1) >= 0:
                fun1 = mf1*(1+(latIPP1-latSta1)*Gn1)*(vtec11+((t + np.rad2deg(lonIPP1 - lonSta1)/15.0 - t1)/(t2-t1))*(vtec12-vtec11))
            else:
                fun1 = mf1*(1+(latIPP1-latSta1)*Gs1)*(vtec11+((t + np.rad2deg(lonIPP1 - lonSta1)/15.0 - t1)/(t2-t1))*(vtec12-vtec11))

            # 2nd station
            if (latIPP2-latSta2) >= 0:
                fun2 = mf2*(1+(latIPP2-latSta2)*Gn2)*(vtec21+((t + np.rad2deg(lonIPP2 - lonSta2)/15.0 - t1)/(t2-t1))*(vtec22-vtec21)) 
            else:
                fun2 = mf2*(1+(latIPP2-latSta2)*Gs2)*(vtec21+((t + np.rad2deg(lonIPP2 - lonSta2)/15.0 - t1)/(t2-t1))*(vtec22-vtec21)) 

        else:
            # one gradient: Gns
            # ionospheric latitudinal gradient
            Gns1 = x[s1n*nPara - 2]
            Gns2 = x[s2n*nPara - 2]

            # 1st station 
            fun1 = mf1*(1+(latIPP1-latSta1)*Gns1)*(vtec11+((t + np.rad2deg(lonIPP1 - lonSta1)/15.0 - t1)/(t2-t1))*(vtec12-vtec11))

            # 2nd station
            fun2 = mf2*(1+(latIPP2-latSta2)*Gns2)*(vtec21+((t + np.rad2deg(lonIPP2 - lonSta2)/15.0 - t1)/(t2-t1))*(vtec22-vtec21)) 



        return y - ((fun2 - fun1) + (instr2 - instr1))
    
    
    @classmethod
    def obs_weights(cls, logger, elev, dtecstd, cs, stationXYZ, eindx = [], W = []):

        '''This function calculates the weigts for geodetic VLBI/VGOS observations.
        It also excludes the weights of observations flagged as outliers.'''

        if eindx:
            # delete the row and column of the observations flagged as an outlier
            W = np.delete(W,eindx, 0)
            W = np.delete(W,eindx, 1)

        else:
            # calculate the weight matrix from scratch if no observations flagged as an outliers

            # calculate the elevation-dependent weights of the observations
            # weight is proportional to elevation angle
            ew1 = np.sin(elev[:,0])
            ew2 = np.sin(elev[:,1])
            ew = ew1*ew2

            # calculate the weights based on the standard deviations of the dtec
            tw = 1/dtecstd**2
            sw = tw/max(tw)

            # calculate the final weights
            W = np.diag(sw*ew)

        return W
    
    
    @classmethod
    def helmertlsq(cls, logger, rel_cindxe, cindxe, cindxr, x0, freq, nSta, nPara, s1n, s2n, Elev1, Elev2, lonIPP1, 
                   lonIPP2, lonSta1, lonSta2, latIPP1, latIPP2, latSta1, latSta2, dtec, dtecstd, t, 
                   time_windows, modified_mf, W, rel_constraints, sum_instr_offsets, gradient):

        '''This function performs the LSQ adjustment to estimate VTEC time series from geodetic VLBI/VGOS observations.'''
        
        # initialize some variables
        A = np.zeros(shape = (len(t),nSta*nPara))
        b = np.zeros(shape = (len(t)))

        for i in range(len(t)):

            # form the A matrix
            A[i,:] = cls.design(logger, x0, freq[i], nSta, nPara, 
                                int(s1n[i]), int(s2n[i]), Elev1[i], Elev2[i], 
                                lonIPP1[i], lonIPP2[i], lonSta1[i], lonSta2[i], 
                                latIPP1[i], latIPP2[i], latSta1[i], latSta2[i],
                                t[i], time_windows, modified_mf, gradient)

            # form the residual vector
            b[i] = cls.observed_computed(logger, x0, freq[i], nSta, nPara, 
                                         int(s1n[i]), int(s2n[i]), Elev1[i], Elev2[i], 
                                         lonIPP1[i], lonIPP2[i], lonSta1[i], lonSta2[i], 
                                         latIPP1[i], latIPP2[i], latSta1[i], latSta2[i], 
                                         dtec[i], t[i], time_windows, modified_mf, gradient)       
        
        
        if rel_constraints:        
            # get the parameters of the pseudo-observations
            H, h, Wc = cls.pseudo_obs(logger, cindxe, nPara, nSta,x0, gradient)         

            # delete the last column representing the instrumental offset of the last station as a constraint
            # delete the columns of the parameters with no observations from the A matrix 
            a = np.delete(A, cindxe.astype(int), 1)

            # form the matric of the lsq
            neqA = np.transpose(a).dot(W).dot(a)         
            neqH = np.transpose(H).dot(Wc).dot(H)
            neqT = neqA + neqH 
            
            f = np.transpose(a).dot(W).dot(b) + np.transpose(H).dot(Wc).dot(h)

            if sum_instr_offsets:
                # enforce the condition that the sum of instr offsets equal zero
                constr_eq = np.zeros(nSta*nPara)
                for i in range(nSta):
                    constr_eq[(i+1)*nPara-1] = 1.0
                constr_eq = np.delete(constr_eq, cindxe.astype(int), 0)
                constr_eq.shape

                # concatenate the matrices
                neqT = np.concatenate((neqT, np.expand_dims(np.transpose(constr_eq), axis=1)), axis=1)
                neqT = np.concatenate((neqT, np.expand_dims(np.concatenate((constr_eq,[0]), axis = 0), axis = 0)), axis=0)
                f = np.concatenate((f, [-sum([x0[(i+1)*nPara-1] for i in range(nSta)])]), axis = 0)

                # calculate the corrections for the estimates
                dx = np.linalg.inv(neqT).dot(f)  

                # get the residuals
                r = a.dot(dx[:-1]) - b
                rh = H.dot(dx[:-1]) - h

            else:
                # calculate the corrections for the estimates
                dx = np.linalg.inv(neqT).dot(f)  

                # get the residuals
                r = a.dot(dx) - b
                rh = H.dot(dx) - h   

            # calculate the degree of freedom, # of obs - # of unknown + # of constrained parameters without obs
            if sum_instr_offsets: 
                dof = len(r)-len(cindxr)+(len(rel_cindxe)-len(cindxe)) + 1
            else:
                dof = len(r)-len(cindxr)+(len(rel_cindxe)-len(cindxe))

            # calculate the reduced-chi squared (reference variance)
            rchisqr = (np.transpose(r).dot(W).dot(r) + np.transpose(rh).dot(Wc).dot(rh))/dof

            # calculate sigma
            s0 = np.sqrt(rchisqr)

            # calculate the co-variance matrix of the estimates
            Qxx = np.linalg.inv(neqT)

            # get the formal errors of the estimates
            sx = s0*np.sqrt(abs(np.diag(Qxx)))

        else: 
            # delete the last column representing the instrumental offset of the last station as a constraint
            # delete the columns of the parameters with no observations from the A matrix 
            a = np.delete(A, cindxe.astype(int), 1)

            # form the matric of the lsq
            neqA = np.transpose(a).dot(W).dot(a)   
            f = np.transpose(a).dot(W).dot(b)

            if sum_instr_offsets:
                # enforce the condition that the sum of instr offsets equals zero
                constr_eq = np.zeros(nSta*nPara)
                for i in range(nSta):
                    constr_eq[(i+1)*nPara-1] = 1.0
                constr_eq = np.delete(constr_eq, cindxe.astype(int), 0)

                # concatenate the matrices
                neqA = np.concatenate((neqA, np.expand_dims(np.transpose(constr_eq), axis=1)), axis=1)
                neqA = np.concatenate((neqA, np.expand_dims(np.concatenate((constr_eq,[0]), axis = 0), axis = 0)), axis=0)
                f = np.concatenate((f, [-sum([x0[(i+1)*nPara-1] for i in range(nSta)])]), axis = 0)

                # calculate the corrections for the estimates
                dx = np.linalg.inv(neqA).dot(f)

                # get the residuals
                r = a.dot(dx[:-1]) - b

            else:
                # calculate the corrections for the estimates
                dx = np.linalg.inv(neqA).dot(f)

                # get the residuals
                r = a.dot(dx) - b

            if sum_instr_offsets:
                # calculate the degree of freedom
                dof = len(r)-len(cindxr) + 1
            else:
                # calculate the degree of freedom
                dof = len(r)-len(cindxr)

            # calculate the reduced-chi squared (reference variance)
            rchisqr = np.transpose(r).dot(W).dot(r)/dof

            # calculate sigma
            s0 = np.sqrt(rchisqr)

            # calculate the co-variance matrix of the estimates
            Qxx = np.linalg.inv(neqA)

            # get the formal errors of the estimates
            sx = s0*np.sqrt(abs(np.diag(Qxx)))

        # add the corrections to the estimates and map the formal errors to the estimates
        indx = [i for i in range(cindxr.shape[0])]
        x0 = x0[cindxr] + dx[indx]
        
        sxx = np.zeros(nPara*nSta)
        sxx[cindxr] = sx[indx]

        return x0, sxx, dx, A, rchisqr, r

    
    @classmethod
    def variance_component_estimation(cls, logger, rel_cindxe, cindxr, Obs2Source, sta, W,
                                      r, A, source_based = 1, baseline_based = 1):

        '''This function estimates the variance components per radio source and per baseline, generating a new weighting matrix.'''

        # apply VCE only once the data is free from outliers

        # delete the column of the parameters with no observation but are relatively constraints
        a = np.delete(A,rel_cindxe,1)

        # get the normal equations
        neqA = np.transpose(a).dot(W).dot(a)

        # calculate the co-variance matrix of the estimates    
        QxxA = np.linalg.inv(neqA)

        # calculate the co-variance matrix of the residuals
        QvvA = np.linalg.inv(W) - a.dot(QxxA).dot(np.transpose(a))

        # calculate the redundancy matrix
        RA = QvvA.dot(W)
        #logger.debug(sum(np.diag(RA)))

        # get the baselines
        baseline = [str(int(sta[i,0])) + ' - ' + str(int(sta[i,1])) for i in range(len(sta[:,0]))] 

        # get the stations
        stations = sorted(set(list(set(sta[:,0])) + list(set(sta[:,1]))))

        # save the input weighting matrix to be used in the estimation of the variance components
        W0 = W

        # apply source-based VCE
        if source_based:

            indx = {} # indices of residuals per source
            vPs = {} # variance component per source 

            for i in set(Obs2Source):            

                # get the indices of residuals per source
                indx[i] = [j for j in range(len(r))  if Obs2Source[j] == i]

                # get the variance component of unit weight per source group
                vPs[i] = np.transpose(r[indx[i]]).dot(np.diag(W0[indx[i],indx[i]])).dot(r[indx[i]])/sum(RA[indx[i],indx[i]])
                #logger.debug(vPs[i],len(indx[i]))

                # scale the weight of each group by its variance component
                W[indx[i],indx[i]] = W[indx[i],indx[i]]/vPs[i]


        # apply baseline_based VCE
        if baseline_based:

            indx = {} # indices of residuals per baseline
            vPb = {} # variance component per baseline

            for i in sorted(set(baseline)):

                # get the indices of residuals per baseline
                indx[i] = [j for j in range(len(baseline))  if i in baseline[j]]

                # get the variance component of unit weight per source group
                vPb[i] = np.transpose(r[indx[i]]).dot(np.diag(W0[indx[i],indx[i]])).dot(r[indx[i]])/sum(RA[indx[i],indx[i]]) 
                #logger.debug(vPb[i],len(indx[i]))

                # scale the weight of each group by its variance component
                W[indx[i],indx[i]] = W[indx[i],indx[i]]/vPb[i]

        return W
    

    @classmethod
    def pseudo_obs(cls, logger, cindxe, nPara, nSta, x0, gradient):

        '''This function applies relative constraints between the piece-wise linear offsets using pseudo observations.'''

        if gradient:
            # two gradients: Gn and Gs
            g = 2
        else:
            # one gradient: Gns
            g = 1

        # initialize some variables for the design matrix of the pseudo-observations  
        H = np.zeros(shape=(nSta*(nPara-1-g-1),nSta*nPara))    
        # sub-constrain matrix of H
        Hi = np.zeros(shape=(nPara-1-g-1,nPara-g-1)) 
        # sub-constrain matrix of W
        Wc = np.zeros(shape=(nSta*(nPara-1-g-1),nSta*(nPara-1-g-1)))
        # vector of residuals
        h = np.zeros(shape=(nSta*(nPara-1-g-1)))

        # sigma of delta VTEC
        std_deltaV = 30    

        # get those matrices
        for n in range(nSta):
            for i in range(Hi.shape[0]):
                Hi[i,i] = 1
                Hi[i, i+1] = -1            

            # VTECs
            H[n*(nPara-1-g-1):(n+1)*(nPara-1-g-1),n*nPara:(n+1)*nPara-g-1] = Hi
            Wc[n*(nPara-1-g-1):(n+1)*(nPara-1-g-1),n*(nPara-1-g-1):(n+1)*(nPara-1-g-1)] = np.diag([1/std_deltaV**2 
                                                                                                   for j in range(nPara-1-g-1)])
            h[n*(nPara-1-g-1):(n+1)*(nPara-1-g-1)] = -(x0[n*nPara:(n+1)*nPara-1-g-1] - x0[n*nPara+1:(n+1)*nPara-g-1])


        # delete the last column representing the instrumental offset of the last station as a constraint
        # delete the columns of the parameters / time windows with no observations
        H = np.delete(H, cindxe.astype(int), 1)

        # find the rows corresponding to the missing parameters
        sub_rows = [((i+1)//nPara)*(nPara-1-g-1)+(i+1)%nPara-1 for i in cindxe 
                    if (i+1)%nPara != nPara-g-1 and (i+1)%nPara != nPara-2 and (i+1)%nPara != nPara-1 and (i+1)%nPara != 0] 
        rows = [i for i in sorted(set(sub_rows + list(np.array(sub_rows)-1))) if i != -1]

        # delete those rows 
        H = np.delete(H, rows, 0)
        h = np.delete(h, rows, 0)
        Wc = np.delete(Wc, rows, 0)
        Wc = np.delete(Wc, rows, 1)

        return H, h, Wc
    
        
    @classmethod
    def data_snooping(cls, logger, h0, freq, nSta, nPara, s2nr, meta_data, stationLLA, stationXYZ, dtec, 
                      dtecstd, t, time_windows, modified_mf, v_doy, sum_instr_offsets, gradient):

        '''This function detects and eliminates any significant outliers in geodetic VLBI/VGOS observations.'''
        
        # don't apply VCE because it's too sensitive to outliers
        # don't apply relative constraint
        rel_constraints = 0

        # extract the observations
        freq, meta_data, sta, elev, latIPP, lonIPP, latSta, lonSta, dtec, dtecstd, t, s2nr = \
        v_data.v_data.extract_observations(logger, freq, s2nr, meta_data, dtec, dtecstd, t)

        # get an update on the time windows w/o observations
        rel_cindxe, cindxe, cindxr, rcindx, c = cls.column_index(logger, nSta, nPara, sta[:,0], sta[:,1], t, time_windows, 
                                                                 rel_constraints, sum_instr_offsets, gradient)

        # get the initial values
        x0 = cls.initial_values(logger, nSta, nPara, rcindx, gradient)

        # get the weights
        W = cls.obs_weights(logger, elev, dtecstd, meta_data, stationXYZ)


        #
        niter_0 = 1
        nObs = len(t)
        # logger.info(f'nObs: {nObs}')
        oindxr = []
        while True:

            # get the estimates
            niter_1 = 0
            rchisqr_before = 1
            while True:

                # calculate the corrections for the estimates
                x0, sxx, dx, A, rchisqr, r = cls.helmertlsq(logger, rel_cindxe, cindxe, cindxr, x0, freq, nSta,
                                                            nPara, sta[:,0], sta[:,1], elev[:,0], elev[:,1],
                                                            lonIPP[:,0], lonIPP[:,1], lonSta[:,0], lonSta[:,1],
                                                            latIPP[:,0], latIPP[:,1], latSta[:,0], latSta[:,1], 
                                                            dtec, dtecstd, t, time_windows, modified_mf, W,
                                                            rel_constraints, sum_instr_offsets, gradient)    

                niter_1 += 1         
                #logger.debug('rchisqr_1', rchisqr, abs(rchisqr-rchisqr_before))
                # iterate for at least the min. # of iteration, i.e. 3 times
                # break if the change in the reference variance is below the threshold
                # or the number of iterations reaches the max. # of iterations 
                if  abs(rchisqr-rchisqr_before) < 1e-2 and niter_1 > 3 or niter_1 > 1e1:    
                    break
                rchisqr_before = rchisqr

            # delete the last column representing the instrumental offset of the last station if it was set to zero as a constraint
            # delete the columns of the parameters with no observations from the A matrix 
            a = np.delete(A, cindxe.astype(int), 1)

            # form the matric of the lsq
            neqA = np.transpose(a).dot(W).dot(a)

            # calculate the co-variance matrix of the estimates    
            QxxA = np.linalg.inv(neqA)

            # calculate the co-variance matrix of the residuals
            QvvA = np.linalg.inv(W) - a.dot(QxxA).dot(np.transpose(a))

            # calculate the standardized residuals
            r_ = abs(r)/np.sqrt(abs(np.diag(QvvA)))

            # get the index of the observation with the maximum normalized residual
            indx = [list(r_).index(max(r_))]

            # calculate sigma
            s0 = np.sqrt(rchisqr)

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
                freq, meta_data, sta, elev, latIPP, lonIPP, latSta, lonSta, dtec, dtecstd, t, s2nr = \
                v_data.v_data.extract_observations(logger, freq, s2nr, meta_data, dtec, dtecstd, t, eindx = indx)

                # get the weights
                W = cls.obs_weights(logger, elev, dtecstd, meta_data, stationXYZ, eindx = indx, W = W)


                oindxr.append(indx[0])

                # get an update on the time windows w/o observations
                rel_cindxe, cindxe, cindxr, rcindx, c = cls.column_index(logger, nSta, nPara, sta[:,0], sta[:,1], t, time_windows,
                                                                         rel_constraints, sum_instr_offsets, gradient)

            else:
                break    


            # break if the number of iterations (outliers) reaches 5% of the data
            #niter_0 += 1
            #if niter_0 > int(nObs*5e-1):
                #break

        logger.info(f'no of outliers: {len(oindxr)}')        
        return freq, meta_data, sta, elev, latIPP, lonIPP, latSta, lonSta, dtec, dtecstd, t, s2nr, x0, oindxr
    
    
    @classmethod
    def refine_parameters(cls, logger, freq, s2nr, nSta, nPara, x0, meta_data, stationXYZ, dtec, dtecstd, t, 
                          time_windows, modified_mf, rel_constraints, vce, sum_instr_offsets, gradient):

        '''This function refines the estimated parameters from geodetic VLBI/VGOS observations.'''

        # extract the observations
        freq, meta_data, sta, elev, latIPP, lonIPP, latSta, lonSta, dtec, dtecstd, t, s2nr = \
        v_data.v_data.extract_observations(logger, freq, s2nr, meta_data, dtec, dtecstd, t)

        # get an update on the time windows w/o observations
        rel_cindxe, cindxe, cindxr, rcindx, c = cls.column_index(logger, nSta, nPara, sta[:,0], sta[:,1], t, time_windows, 
                                                                 rel_constraints, sum_instr_offsets, gradient)
                                

        # get the weights
        W = cls.obs_weights(logger, elev, dtecstd, meta_data, stationXYZ)

        # get the estimates    
        niter_0 = 0
        rchisqr_before = 1
        while True:

            # calculate the corrections for the estimates
            x0, sxx, dx, A, rchisqr, r = cls.helmertlsq(logger, rel_cindxe, cindxe, cindxr, x0, freq, nSta, 
                                                        nPara, sta[:,0], sta[:,1], elev[:,0], elev[:,1],
                                                        lonIPP[:,0], lonIPP[:,1], lonSta[:,0], lonSta[:,1],
                                                        latIPP[:,0], latIPP[:,1], latSta[:,0], latSta[:,1], 
                                                        dtec, dtecstd, t, time_windows, modified_mf, W, 
                                                        rel_constraints, sum_instr_offsets, gradient)                

            niter_0 += 1
            # logger.debug('rchisqr_0', rchisqr, abs(rchisqr_before-rchisqr))
            # iterate for at least the min. # of iteration, i.e. 3 times
            # break if the change in the reference variance is below the threshold
            # or the number of iterations reaches the max. # of iterations 
            if abs(rchisqr-rchisqr_before) < 1e-2 and niter_0 > 3 or niter_0 > 1e1:    
                break
            rchisqr_before = rchisqr


        # refine the stochastic model and re-do the adjustment
        # get the observations per source  
        Obs2Source = meta_data[:,0,7]  
        if vce:
            niter_1 = 0    
            while True:

                # finesse the stochastic model and redo the adjustment
                W = cls.variance_component_estimation(logger, rel_cindxe, cindxr, Obs2Source, sta, W, r, A)

                niter_2 = 0
                rchisqr_before = 1
                while True:

                    # calculate the corrections for the estimates
                    x0, sxx, dx, A, rchisqr, r = cls.helmertlsq(logger, rel_cindxe, cindxe, cindxr, x0, freq, nSta, 
                                                                nPara, sta[:,0], sta[:,1], elev[:,0], elev[:,1],
                                                                lonIPP[:,0], lonIPP[:,1], lonSta[:,0], lonSta[:,1],
                                                                latIPP[:,0], latIPP[:,1], latSta[:,0], latSta[:,1],
                                                                dtec, dtecstd, t, time_windows, modified_mf, W, 
                                                                rel_constraints, sum_instr_offsets, gradient)

                    niter_2 += 1         
                    # logger.debug('rchisqr_1', rchisqr, abs(rchisqr-rchisqr_before))
                    # iterate for at least the min. # of iteration, i.e. 3 times
                    # break if the change in the reference variance is below the threshold
                    # or the number of iterations reaches the max. # of iterations 
                    if  abs(rchisqr-rchisqr_before) < 1e-2 and niter_2 > 3 or niter_2 > 1e1:    
                        break
                    rchisqr_before = rchisqr


                niter_1 += 1
                # logger.debug('rchisqr_2', rchisqr, 1-rchisqr)
                # iterate for at least the min. # of iteration, i.e. 5 times
                # break if the change in the reference variance is below the threshold
                # or the number of iterations reaches the max. # of iterations 
                if abs(1-rchisqr) < 5e-4 and niter_1 >= 3 or niter_1 > 1e1: 
                    break   

        return x0, sxx, r, Obs2Source
    
    
    @classmethod
    def mapping_parameters(cls, logger, nSta, nPara, resolution, stations, stationLLA, rcindx, exSta, x, sx, h0,
                           time_windows, session, gradient, gims, madrigal, v_doy, ionex_path, madrigal_path):

        '''This function maps the estimated parameters to their stations.'''

        # initialize some variables
        param = {station: {'vtec':[],'iono_grad':[],'instr_offset':[]}
                 for i, station in enumerate(stations) if station not in exSta}    

        # get the time tag
        time_tag = []
        date_tag = []
        for i in int(h0) + time_windows: 
            # append the time tag to the list
            time_tag.append(str(datetime.timedelta(hours = i-24*math.floor(i/24))).rjust(2,'0'))
            # get the date of the next day
            nxtdate = datetime.date(2000+int(session[:2]),datetime.datetime.strptime(session[2:5], "%b").month,
                                    int(session[5:7])) + datetime.timedelta(days=math.floor(i/24))
            # append the date tag to the list
            date_tag.append(nxtdate.strftime("%Y")+'/'+nxtdate.strftime("%m").rjust(2,'0')+'/'+nxtdate.strftime("%d").rjust(2,'0'))

        # get the vtec values from GIMs
        if gims:
            gims, gims_vtec = GTMs.Global_TEC_Maps.VTEC_GIMs(logger, h0, resolution, time_windows,
                                                             stationLLA, v_doy, gims, ionex_path)
        # get the VTECs from madrigal
        if madrigal:
            epochs = int(h0) + time_windows
            madrigal, madr = GTMs.Global_TEC_Maps.VTEC_MTMs(logger, session, stations, exSta, stationLLA,
                                                            epochs[0], epochs[-1], madrigal, madrigal_path) 

        # loop over the stations
        for i, station in enumerate(stations):            
            if station not in exSta:

                if gradient:
                    # two gradients: Gn and Gs
                    # initialize some variables
                    vtec = np.empty(shape = (nPara-3,6)).astype(str)                    
                    iono_grad = np.empty(shape = (5)).astype(str)
                    instr_offset = np.empty(shape = (3)).astype(str)
                    vtec[:,:], iono_grad[:], instr_offset[:] = '_', '_', '_'

                    # get the date
                    vtec[:,0] = date_tag
                    iono_grad[0] = date_tag[0]
                    instr_offset[0] = date_tag[0]

                    # get the time tags
                    vtec[:,1] = time_tag                 

                    # get the VLBI/VGOS parameters
                    vtec[:,2] = [str(np.round(item,3)) for item in x[i*nPara:(i+1)*nPara-3]]
                    iono_grad[1] = str(np.round(x[(i+1)*nPara-3],3))
                    iono_grad[3] = str(np.round(x[(i+1)*nPara-2],3))
                    instr_offset[1] = str(np.round(x[(i+1)*nPara-1],3))

                    # get their formal errors
                    vtec[:,3] = [str(np.round(item,3)) for item in sx[i*nPara:(i+1)*nPara-3]]   
                    iono_grad[2] = str(np.round(sx[(i+1)*nPara-3],3))
                    iono_grad[4] = str(np.round(sx[(i+1)*nPara-2],3))
                    instr_offset[2] = str(np.round(sx[(i+1)*nPara-1],3))

                    # get VTECs from GIMs
                    if gims:
                        vtec[:,4] = [str(np.round(item,3)) for item in gims_vtec[:,i]] 
                    
                    # get VTECs from Madrigal
                    if madrigal:
                        if madr[station].any():
                            vtec[:,5] = [str(np.round(item,3)) for item in np.interp(epochs, madr[station][:,0], madr[station][:,2])] 

                else:
                    # one gradient: Gns
                    # initialize some variables
                    vtec = np.empty(shape = (nPara-2,6)).astype(str)
                    iono_grad = np.empty(shape = (3)).astype(str)
                    instr_offset = np.empty(shape = (3)).astype(str)
                    vtec[:,:], iono_grad[:], instr_offset[:] = '_', '_', '_'

                    # get the date
                    vtec[:,0] = date_tag
                    iono_grad[0] = date_tag[0]
                    instr_offset[0] = date_tag[0]

                    # get the time tags
                    vtec[:,1] = time_tag                 

                    # get the VLBI/VGOS parameters
                    vtec[:,2] = [str(np.round(item,3)) for item in x[i*nPara:(i+1)*nPara-2]]
                    iono_grad[1] = str(np.round(x[(i+1)*nPara-2],3))
                    instr_offset[1] = str(np.round(x[(i+1)*nPara-1],3))

                    # get their formal errors
                    vtec[:,3] = [str(np.round(item,3)) for item in sx[i*nPara:(i+1)*nPara-2]]   
                    iono_grad[2] = str(np.round(sx[(i+1)*nPara-2],3))
                    instr_offset[2] = str(np.round(sx[(i+1)*nPara-1],3))

                    # get VTECs from GIMs     
                    if gims:
                        vtec[:,4] = [str(np.round(item,3)) for item in gims_vtec[:,i]] 

                    # get VTECs from Madrigal
                    if madrigal:
                        if madr[station].any():
                            vtec[:,5] = [str(np.round(item,3)) for item in np.interp(epochs, madr[station][:,0], madr[station][:,2])] 

                # get the indices of the time windows with observations
                indx = [j for j in range(rcindx.shape[0]) if rcindx[j,i] != 0]
                if rcindx[-1,i] != 0:
                    indx = indx + [int(indx[-1])+1]

                # save the parameters in the dictionary
                param[station]['vtec'] = vtec[indx,:]
                param[station]['iono_grad'] = iono_grad
                param[station]['instr_offset'] = instr_offset                
        
        return param
    