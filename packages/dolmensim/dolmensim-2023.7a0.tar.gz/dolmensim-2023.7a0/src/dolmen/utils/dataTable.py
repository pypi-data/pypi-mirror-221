        # -*- coding: utf-8 -*-
"""
Created on Thu Mar 10 11:20:57 2022

@author: nicolas.rouve
"""
import sys
import numpy as np
import pandas as pd

class profile :
    """
    A class used to define a profile of values to provide input to systems
    
    Attributes
    ----------
    profiledata: 2d np.array
        raws with [time, value, nature]
            time: time of event
            value: value to be attained at 'time'
            nature: how to get to THIS value
                - step : step to this value (mandatory for first line)
                - ramp : ramp from previous value/time to this value/time
        example:
            test = profile ([
                [0, 500, 'step'],
                [2, 1200, 'ramp'],
                [5, 2000, 'step'],
                [7, 700, 'ramp']
                ])

    
    """
    def __init__(self, profileData = [[0, 1, 'step']]) :
        self.profileData = profileData
        
    def setProfile(self, profileData) :
        self.profileData = profileData
    
    def getParam(self, trigger):
        """
        gets the profile value for actual time
        
        Parameters
        ----------
        trigger : float
            time at which to get the value
            
        Returns
        -------
        the claculated value
        """
        param = 0
        i=0
        profileLen = len(self.profileData)
        while i < profileLen :
            inVal,outVal, form = self.profileData[i]
            # print ('i=', i, 'profileLen=',profileLen)
            # print ('trig=',trigger, 'inVal=', inVal,'outVal=', outVal,'form=', form )
            if i+1 >= profileLen : # no next point ... 
                if form == 'ramp':
                    form = 'step'      # ...changed to 'step'
                    print('utils::profile > warning: last profile point (',inVal,';', outVal,') cannot be ramp. Changed to step', sep = '')
                return outVal
            inValNext,outValNext, formNext = self.profileData[i+1]
            if inValNext > trigger : # use this values (not next)
                if form == 'step':
                    return outVal
                elif form == 'ramp':
                    # print ('trig=',trigger, 'inValNext=', inValNext,'outValNext=', outValNext,'formNext=', formNext, end='')
                    outSpan = outValNext - outVal
                    inSpan  = inValNext  - inVal
                    valueScaled = (trigger-inVal)/inSpan
                    param = outVal + valueScaled*outSpan
                    # print(' param=',param)
                    return param
            i+=1 #try with next coordinates !
"""
TODO:
    - impulse
    - quadratic
    - sine
    - slope (value reached in delta t)
    - text (for control mode SPEED, ALTITUDE, FORCE)
    
"""

# if __name__ == "__main__":
#     test = profile ([
#             [0, 500, 'step'],
#             [2, 1200, 'ramp'],
#             [5, 2000, 'step'],
#             [7, 700, 'ramp']
#             ])


#     for x in range (0, 9, 1):
#         print ('=>', x, test.getParam(x))

class dataFile:
    """
    A class used to access to a parameter defined in a table (csv file)
    first column must be an x axis for one or more curves
    first line must be the name of the parameter to read
    
    Attributes
    ----------
    inName: str
        the name of the entry value (verified by constructor)
        
    df_datas: panda dataframe
        table imported from csv
    
    dict_datas: dictionnary of np.arrays
        each column of parameter is put in 1 np.array, then updated to the dict with columname as index
    
    """
    
    def __init__(self, fileName, inName):
        self.fileName = fileName
        self.df_datas = pd.read_csv(fileName) # panda dataframe
        if inName in self.df_datas:
            self.inName = inName
        else:
            sys.exit(f"dataTables::dataFile : error : input name '{inName}' does not exist in datafile {fileName} !")

        self.dict_datas = {}
        for index, series in self.df_datas.iteritems() :
            self.dict_datas.update({index : np.array(series)})

    
    def getParam(self, refVal, paramName):
        """
        get the value of a parameter
        
        Parameters
        ----------
        refVal : float
            value of the entry parameter for which we want the parameter value
        
        paramName: str
            name of the parameter (column in the file) in which to read the value
        
        """
        if not paramName in self.df_datas:
            sys.exit("dataTables::dataFile : error : param name does not exist in datafile!")

        xp = self.dict_datas[self.inName]
        fp = self.dict_datas[paramName]
        interpolatedValue = np.interp(refVal, xp, fp, ) # native interpol of numpy
        # if not min(xp) < refVal < max(xp) :
        #     print(f">>>dolmen.utils.dataTable.dataFile.getParam ({self.fileName}): value out of range: {min(xp)} < {refVal} < {max(xp)}")
            # sys.exit()
        
        return interpolatedValue

    def aeroCoef(Re,alpha,foilFile):
        
        """
        this function is used to find the aerodynamic coefficients with a very
        specific method which is explained in this file :
            'dolmen\_howTo\Coefficient aérodynamique.pptx"'
    
        Parameters
        ----------
        Re : TYPE float
            DESCRIPTION. Reynold number [-]
        alpha : TYPE float
            DESCRIPTION. attack angle [°]
        foilFile : TYPE text
            DESCRIPTION. file with all coefficient depending of Re and alpha with
            this form : C:\direction\dolmen\direction\FileName.xlsx
    
        Returns
        -------
        Cl : TYPE float
            DESCRIPTION. Lift coefficient
        Cd : TYPE float
            DESCRIPTION. Drag Coefficient
        Cm : TYPE float
            DESCRIPTION. Moment Coefficient
    
        """    
      
        alpha = round_to_quarter(alpha)
        polar = pd.read_excel(foilFile)
        # Sélection de la colonne en fonction de Re
        if Re < 75000:
            Re_p = polar['50000']
        elif 75000 <= Re < 150000:
            Re_p = polar['100000']
        elif 150000 <= Re < 350000:
            Re_p = polar['200000']
        elif 350000 <= Re < 750000:
            Re_p = polar['500000']
        elif 750000 <= Re:
            Re_p = polar['1000000']
        
        alpha_e = None
        last_val = None
        vals_array = []
        
        for val in Re_p:
            if pd.notnull(val):   # Vérifier si la valeur n'est pas NaN
                sep = val.split(',')
                alpha_excel = float(sep[0])
                vals_array.append(val)
                if alpha <= alpha_excel:
                    alpha_e = alpha_excel
                    Cl = float(sep[1])
                    Cd = float(sep[2])
                    Cm = float(sep[4])
                    break
            else:
                last_val = vals_array[-1]
                break
        if Re > 750000:
            last_val = vals_array[-1]
        if alpha_e is None and last_val is not None:
            sep = last_val.split(',')
            alpha_e = float(sep[0])
            Cl = float(sep[1])
            Cd = float(sep[2])
            Cm = float(sep[4])
        return Cl, Cd, Cm

def round_to_quarter(num):
    """
    Round a number to X.0 , X.25, X.5, X.75

    Parameters
    ----------
    num : TYPE float
        DESCRIPTION. Number to you want to round

    Returns
    -------
    TYPE float
        DESCRIPTION. The number rounded

    """
    return np.round(num / 0.25) * 0.25

# if __name__ == "__main__":
#     path = "C:/Users/nicolas.rouve/Documents/20_PROJETS/2122/GliderWinch/DolmenSim"
#     file = "Ask21Wing.csv"
#     datas = dataFile(path+'/'+ file, 'alpha')
#     inval = 15
#     outval = datas.getParam(inval, 'CL')
#     print (f'Value at {inval} is {outval}')
    