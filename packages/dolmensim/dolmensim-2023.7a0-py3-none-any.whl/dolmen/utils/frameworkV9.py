# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
import time
import dolmen.control.LTIsystem as lti

class System:
    """
    A class used to define the physical model to be simulated.
    The physical quantities and the equations (Law of Behaviour) will be defined
    Model parameters and simulation conditions will be defined in seperate files,
    allowing to simulate several instances or test conditions in parallel

    The system dimensions (X, Y, ...) and Quantities (x, v, a) and outVal quantities
    and physical behaviour will be instanciated in "model" file

    The system can be studied alone or considered as a subsystem of an parent system

    Attributes
    ----------
    name: str
        name of the system under simulation

    description : str
        description of the system
        
    context : str
        description of the context of use of this simulation.
        could be used to document systems aggregation
        
    dimensions : dict of Dimension
        all the dimensions of the studied system as a dict
        only descriptions, no values

    inSignals : dict of listsprofile data signals
        all the profile data for input signals
        
    physics : function
        the behaviour law of the system
        
    values : panda dataframe
        all the values calculated by the simulation process


    """

    def __init__(self, name, description = '', context = ''):
        """
        constructor of object model, called by subclass model
        the concrete objects of the simulation will be instantiated
        after defining the inputs, by function setInput() unsing model.compose()
        """
        self.name = name
        self.description = description
        self.context = context
        self.dims = {}
        self.df_values = None
        self.inSignals = {}
        self.defineDimsQuant()
        self.output = ""
        
    def addDim(self, newDim):
        """
        add a dimension to the system
        
        Parameters
        ----------
        newDim : object Dimension
        defined in file model file, by the function Physics.defineDimsQuant()
        
        """
        self.dims.update({newDim.code : newDim})
    
    # def addoutVal(self, outVal):
    #     self.outVal = outVal
    
    def getNbDim(self):
        return len(self.dims)
    
    def getDimCode(self, id):
        key = list(self.dims.keys())[id] # get keys, make a list, get key of id
        # print(f"> System.getDimCode: dim['{key}'] = ")
        # print(self.dims[key])
        dimCode = self.dims[key].getCode()
        return dimCode

    def getDimCodes(self):
        codes = []
        for k,d in self.dims.items():
            codes.append(d.getCode())
        return codes

    def getDimName(self, id):
        key = list(self.dims.keys())[id] # get keys, make a list, get key of id
        dimName = self.dims[key].getName()
        return dimName

    def getDimNames(self):
        names = []
        for k,d in self.dims.items():
            names.append(d.getName())
        return names

    # what is the aim of this function ??
    def getQuantNames(self):
        firstKey = list(self.dims.keys())[0] # get keys, make a list, get nb 0
        return self.dims[firstKey].getQuantNames()

    def getOutValNames(self):
        return self.dims['b'].getQuantNames()

    def addInput(self, inSignal):
        """
        Add an input signal to the system
        
        Parameters
        ----------
        inSignal : list of list
            the profile data for one input signal

        """
        self.inSignals.update(inSignal)
        # print(">System.addInput: signals:\n", self.inSignals)
    
    def setFxyz(self, function):
        self.Fxyz = function
        
    def runSim(self, xyz, timeCond):
        """
        Executes the whole simulation.
        
        Parameters
        ----------
        xyz: 2D np.array of float
            actual values of mandatory quantities of modeled dimensions
            1st dim  is quantity [qtty,:] (eg. position, velovity, acceleration)
            2nd dim  is dimension [:,dim] (eg. X, psi, current)
    
        timeCond : list of floats
            start, stop and step values.
        
        dynamicBehaviour : boolean, optional
            The default is True.
            Does the model have a dynamic behaviour ?
            If no, it is a static system with only algebraic equations no diff eq

        Returns
        -------
        None.

        Border effects
        --------------
        Results dataframe (self.df_values) used by simufile to generate graphs
        logfile (simulog.csv)


        """
        # creation of the system, i.e. instatiate the objects
        print ("Simulation started at", time.strftime("%H:%M:%S"))
        self.compose()
        print ("Objects created")
        print ("Simulation running...", end='')
        
        # request SIMULATION from framework method
        arr_time,arr_values,arr_deriv,arr_outVal = simulate(xyz, self.Fxyz, timeCond)
        
        print ("Done.")
        # Simulation completed
        # prepare result values dataframe
        # prepare datas
        data = {'t': list(arr_time)} # first column is time

        # unpack arr_values normal quantities
        nbRows, nbQuant, nbDim = np.shape(arr_values)
        for dimId in range(nbDim):
            dimValues = arr_values[:,:, dimId]
            dimCode = self.getDimCode(dimId)
            titles = self.dims[dimCode].getQuantSymbols()#[dimId]
            for quantId in range(nbQuant):
                # normal qantities of this dim
                data.update({titles[quantId] : list(dimValues[:, quantId])})
            # unpack arr_deriv derivatives
            data.update({titles[quantId+1] : list(arr_deriv[:, dimId])}) # derivative quantitiy of this dim

        # unpack arr_outVal 
        nbRows, nbQuant= np.shape(arr_outVal)
        dimCode = 'b'
        titles = self.dims[dimCode].getQuantSymbols()#[dimId]
        for quantId in range(nbQuant):
            data.update({titles[quantId] : list(arr_outVal[:, quantId])})
        self.df_values = pd.DataFrame(data)
        print ("Dataframe ready")
        
        # output File write
        with open ('simuLog.csv', 'w') as destFile : # ouvre le fichier en lecture
            destFile.write(self.header+'\n')
            destFile.write(self.output)
            destFile.close()
            print ("Log saved.")
        print ("Simulation completed at", time.strftime("%H:%M:%S"))
        
    def plotQuantities(self, qttiesToPlot ='', FileName = 'Multi Plot', width=6.4, height=4.8):
        """
        generates a TIME plot 
    
        Parameters
        ----------
        qttiesToPlot : list of list of str
            contains the symbols of the quantities to be represented e.g. 'vel_z'
            grouped in a list for an axes
            all axes of the figure grouped in a list
        FileName : optional, str
            The default is 'Multi Plot'.
            Name you saved file.   
        width : optional, float
            The default is 6.4.
            Ajust the size of you graph
        height : optional, float
            The default is 4.8.
            Ajust the size of you graph
        Returns
        -------
        None.

        """
        import matplotlib.pyplot as plt

        if qttiesToPlot == '' : # nothing specified
            qttiesToPlot = []
            for q in list(self.df_values)[1:] :
                qttiesToPlot.append([q])  # create a list of all quantities ...
        graphNb  = len(qttiesToPlot)
        fig, axs = plt.subplots(graphNb, 1,figsize=(width,height))
        fig.subplots_adjust(hspace=0.7)
        if graphNb == 1 : axs = np.array([axs])# single axes not possible in matplotlib :-(
        axesIndex = 0
        for qttOneAx in qttiesToPlot :
            times =  np.array(self.df_values['t'])
            values = np.array(self.df_values[qttOneAx])
            # print("> System.plotQuantities: FINAL values=\n", values)
            axs[axesIndex].plot(times,values)
            axs[axesIndex].set_xlabel('time (s)', size='x-large')
            title = ""
            for qtty in qttOneAx : title += qtty + "\n"
            axs[axesIndex].set_ylabel(title, size='x-large')
            axs[axesIndex].legend(qttOneAx, loc='best', fontsize ='x-large')
            axs[axesIndex].grid(True)
            axesIndex +=1

        chart_img = FileName  # Nom du fichier d'image pour le graphique
        fig.savefig(chart_img)
        
        fig.show()

    def plotXY(self, Xsymbol,Ysymbol,Angle=None,FileName = 'PlotXY', scale = True):
        """
        generates an X-Y plot to represent relation between two quantities
    
        Parameters
        ----------
        X, Y : two 1D np.arrays 
            contains x, resp y values for the graph
        Angle : optional, str
            The default is None.
            If you want to see what is the Theta angle, to compare with the,
            you just have to write 'theta'
        FileName : optional str
            The default is 'PlotXY'.
            Name you saved file.
        scale : optional Booleen
            The default is True.
            If you want to scale or not your graph.

        Returns
        -------
        None.

        """
        import matplotlib.pyplot as plt
        
        Xval = self.df_values[Xsymbol]
        Yval = self.df_values[Ysymbol]
        
        fig, ax = plt.subplots()
        
        ax.scatter(Xval,Yval)
        if scale == True:
            x_min, x_max = np.min(Xval), np.max(Xval)
            x_range = x_max - x_min
        
            y_range = x_range * (len(Yval) / len(Xval))
            y_mean = np.mean(Yval)
            y_min, y_max = y_mean - y_range/2, y_mean + y_range/2
            ax.set_ylim(y_min, y_max)
            
        if Angle != None:
            
            angle = self.df_values[Angle]
            
            Angle_rad = np.deg2rad(angle)
            
            dx = np.cos(Angle_rad)
            dy = np.sin(Angle_rad)
            
            ax.quiver(Xval, Yval, dx, dy,color='red')  # Tracer les vecteurs d'angle

        # ax.plot(Xval,Yval)
        ax.set_title(f'{Ysymbol} = f({Xsymbol})')
        ax.set_xlabel(Xsymbol)
        ax.set_ylabel(Ysymbol)
        
        chart_img = FileName  # Nom du fichier d'image pour le graphique
        fig.savefig(chart_img)
        
        fig.show()    


    def plotXYAnimated(self, Xsymbol,Ysymbol, FileName='scatter.gif', ImageFile = 'dolmen\Su26M\Plane.png'):
        import matplotlib.animation as animation
        import matplotlib.pyplot as plt
        import os
        
        fig, ax = plt.subplots()
    
        Xval = self.df_values[Xsymbol]
        Yval = self.df_values[Ysymbol]
        
        x_min, x_max = np.min(Xval), np.max(Xval)
        x_range = x_max - x_min
        
        y_range = x_range * (len(Yval) / len(Xval))
        y_mean = np.mean(Yval)
        y_min, y_max = y_mean - y_range/2, y_mean + y_range/2
        
        ax.set_xlim(x_min, x_max)
        ax.set_ylim(y_min, y_max)
    
        ax.set_title(f'{Ysymbol} = f({Xsymbol})')
        ax.set_xlabel(Xsymbol)
        ax.set_ylabel(Ysymbol)
        
        # Load the image
        img = plt.imread(ImageFile)
        img_width = x_range / 10  # Adjust the image width as needed
        
        # Scale the image to match the data coordinates
        img_height = img_width * (img.shape[0] / img.shape[1])
        
        scat = ax.imshow(img, extent=(Xval[0]-img_width/2, Xval[0]+img_width/2,
                                      Yval[0]-img_height/2, Yval[0]+img_height/2))
        
        def animate(i):
            scat.set_extent((Xval[i]-img_width/2, Xval[i]+img_width/2,
                             Yval[i]-img_height/2, Yval[i]+img_height/2))
            return scat,
    
        ani = animation.FuncAnimation(fig, animate, repeat=True,
                                      frames=len(Xval) - 1, interval=500)
    
        plt.close()
        # To save the animation using Pillow as a gif
        writer = animation.PillowWriter(fps=15,
                                        metadata=dict(artist='Me'),
                                        bitrate=1800)
        ani.save(FileName, writer=writer)
    
        os.system('start ' + FileName)
        
    def plotXYZ(self, Xsymbol,Ysymbol,Zsymbol, FileName = 'PlotXYZ', scale = True):
        """
        generates an X-Y plot to represent relation between two quantities
    
        Parameters
        ----------
        X, Y : two 1D np.arrays 
            contains x, resp y values for the graph
        
        """
        import matplotlib.pyplot as plt
        
        Xval = self.df_values[Xsymbol]
        Yval = self.df_values[Ysymbol]
        Zval = self.df_values[Zsymbol]
        
        fig = plt.figure()
        ax = plt.axes(projection='3d')
        
        if scale == True:
            x_min, x_max = np.min(Xval), np.max(Xval)
            y_min, y_max = np.min(Yval), np.max(Yval)
            z_min, z_max = np.min(Zval), np.max(Zval)
        
            x_range = x_max - x_min
            y_range = y_max - y_min
            z_range = z_max - z_min
        
            max_range = max(x_range, y_range, z_range)
        
            # Calculate scaling factors based on the predominant range
            x_scale = max_range / x_range if x_range == max_range else 1.0
            y_scale = max_range / y_range if y_range == max_range else 1.0
            z_scale = max_range / z_range if z_range == max_range else 1.0
        
            # Apply scaling to each axis
            scaled_Xval = Xval * x_scale
            scaled_Yval = Yval * y_scale
            scaled_Zval = Zval * z_scale
        
            ax.scatter(scaled_Xval, scaled_Yval, scaled_Zval, color='blue')

        
            ax.scatter(scaled_Xval, scaled_Yval, scaled_Zval, color='blue')
        
        else :
            ax.scatter3D(Xval, Yval, Zval)
        ax.set_title(f'{Zsymbol} = f({Xsymbol}, {Ysymbol})')
        ax.set_xlabel(Xsymbol)
        ax.set_ylabel(Ysymbol)
        ax.set_zlabel(Zsymbol)
        
        chart_img = FileName  # Nom du fichier d'image pour le graphique
        fig.savefig(chart_img)
        
        plt.show()   
        
    # def plotXYZAnimated(self, Xsymbol, Ysymbol, Zsymbol, timeCond, FileName='scatter.gif'):
    #     import matplotlib.animation as animation
    #     import matplotlib.pyplot as plt
    #     import os

    #     fig = plt.figure()
    #     ax = fig.add_subplot(111, projection='3d')
    
    #     x = self.df_values[Xsymbol]
    #     y = self.df_values[Ysymbol]
    #     z = self.df_values[Zsymbol]
    #     t = np.arange(timeCond[0], timeCond[1]-1,timeCond[2])
        
    #     x_min, x_max = np.min(x), np.max(x)
    #     y_min, y_max = np.min(y), np.max(y)
    #     z_min, z_max = np.min(z), np.max(z)
    
    #     ax.set_xlim(x_min, x_max)
    #     ax.set_ylim(y_min, y_max)
    #     ax.set_zlim(z_min, z_max)
    
    #     ax.set_xlabel(Xsymbol)
    #     ax.set_ylabel(Ysymbol)
    #     ax.set_zlabel(Zsymbol)
        

    #     lines = []
        
    #     for i in range(1, len(t)):
    #         head = i - 1
    #         head_slice = (t > t[i - 1]) & (t <= t[i])
    #         line1 = ax.plot(x[:i], y[:i], z[:i], color='black')
    #         line1a = ax.plot(x[i-1:i+1], y[i-1:i+1], z[i-1:i+1], color='red', linewidth=2)
    #         line1e = ax.plot([x[head]], [y[head]], [z[head]], color='red', marker='o', markeredgecolor='r')
    #         lines.append([line1, line1a, line1e])
            
    #     ani = animation.ArtistAnimation(fig, lines, interval=50, blit=True)
    
    #     plt.close()
    
    #     # To save the animation using Pillow as a gif
    #     writer = animation.PillowWriter(fps=15,
    #                                     metadata=dict(artist='Me'),
    #                                     bitrate=1800)
    #     ani.save(FileName, writer=writer)
    
    #     os.system('start ' + FileName)
#==============================================================================

class Quantity:
    """
    A class used to represent a physical quantity, eg. speed, current, etc
    
    Attributes
    ----------
    symbol : str
        the symbol of the physical quantity as used in equations
        must be variable name compatible, no space, underscores
        examples : T_motorIn, w_gearOut, a_glider_X
        
    name : str
        the name of the quantity as used in litterature and graphic scales
        Can include spaces
        'motor In torque', 'gear output speed', 'glider accel in x'

    unit : str
        the unit of the quantity
        prefer SI units
    
    val : float (or int)
        val of the quantity 

    mandatory : bool
        main quantity for resolution
        
    outVal : bool
        only generated for analysis or output
        
    inData : bool
        can be used as input on system.
        On static elements (no integral) a quantity can be used as an input or output

    outData : bool
        can be used as output on system
        On static elements (no integral) a quantity can be used as an input or output
    
    Methods
    -------

    """
    
    def __init__(self, symbol, name='', unit='', initialval=0):
        self.symbol = symbol
        self.name = name
        self.unit = unit
        self.val = 0
        self.initialval = initialval
        """
        Parameters
        ----------
        symbol : str
            the symbol of the physical quantity as used in equations
            must be variable name compatible, no space, underscores
            examples : T_motorIn, w_gearOut, a_glider_X
            
        name : str
            the name of the quantity as used in litterature and graphic scales
            Can include spaces
            'motor In torque', 'gear output speed', 'glider accel in x'
    
        unit : str
            the unit of the quantity
            prefer SI units

        mandatory : bool
            main quantity for resolution
            
        outVal : bool
            only generated for analysis or output
            
        inData : bool
            can be used as input on system.
            On static elements (no integral) a quantity can be used as an input or output
    
        outData : bool
            can be used as output on system
            On static elements (no integral) a quantity can be used as an input or output

        """
    
    def getSymbol(self):
        """
        returns Symbol of quantity
        """
        return self.symbol

    def getSymbolAndName(self):
        """
        returns [Symbol, Name] of quantity
        """
        return [self.symbol, self.name]

    def getName(self):
        """
        returns Name of all quantity
        """
        return self.name

if __name__ == '__main__':
    print("> Quantity: class test")
    pos_x = Quantity('pos_x', 'glider position X', 'm', 0)
    pos_y = Quantity('pos_y', 'glider position Y', 'm', 0)
    vel_x = Quantity('vel_x', 'glider speed X', 'm/s', 0)
    vel_y = Quantity('vel_y', 'glider speed Y', 'm/s', 0)

#==============================================================================
class Dimension:
    """
    A class used to group the quantities of a behaviour law.
    For example position - speed - acceleration
    
    Attributes
    ----------
    code : str
        abbreviated dimension name eg. 'x'
        
    name : str
        name of the dimension 'forward', 'head rotation', 'pitch'
    
    quantities : dict of obj Quantity
        all the quantities in increasing order (x, x', x'')
    
    
    Methods
    -------


    """
    # dimNb = 0 # static !
    
    def __init__(self, code, name):
        self.code = code
        self.name = name
        self.quantities = {} 
        self.boundQuantNb = 0
        

    def bindQuant(self, quantity):
        """
        aggregate a created quantity into a dimension, as a dict
        example:
            X.bind(position)
            X.bind(velocity)
        """
        self.quantities.update({quantity.symbol: quantity})
        self.boundQuantNb += 1
    
    def getCode(self):
        """
        returns the code of this dim
        """
        return self.code

    def getName(self):
        """
        returns the name of this dim
        """
        return self.name

    def getNbQuant(self):
        """
        returns the number of quantities bound to dim
        """
        return self.boundQuantNb 
    
    def getQuantSymbols(self):
        """
        returns Symbol of all quantities of a dim, as a list
        """
        symbols = []
        for k,q in self.quantities.items():
            symbols.append(q.getSymbol())
        # print("Dimension.getQuantSymbols: symbols =", symbols)
        return symbols

    def getQuantSymbolsAndNames(self):
        """
        returns [Symbol, Name] of all quantities of a dim, as a list (eg. list of list!)
        """
        names = []
        for k,q in self.quantities.items():
            names.append([q.getSymbol(), q.getName()])
        return names

    def getQuantNames(self):
        """
        returns Names of all quantities of a dim, as a list
        """
        names = []
        for k,q in self.quantities.items():
            names.append(q.getName())
        return names
    
    # def quantValues(self, symbol):
        """
        Parameters
        ----------
        symbol : str
            symbol of the quantity, for example 'vel_x'
        """
        



    def __repr__(self):
        dimRepr = 'Dimension : '
        dimRepr += f"{self.code} : "        
        dimRepr += f"{self.name}"
        dimRepr += f"\n\tQuantities ({self.getNbQuant()}):"

        for dim in self.getQuantSymbolsAndNames():
            dimRepr += f"\n\t\t{dim[0]} : {dim[1]}"
        return dimRepr
        
        
        
if __name__ == '__main__':
    print("> Dimension: class test")
    dimX = Dimension('r','horiz-right')
    dimX.bindQuant(pos_x)
    dimX.bindQuant(vel_x)
    
    print(dimX)
    
#==============================================================================



def RK4(x, F, t, h):
    """
    Created on Thu Mar 10 09:50:23 2022
    
    @author: Vincent Bourquin
    """
    """
    Cette méthode permet la résolution numérique des équations différentielles 
    en général et celles dérivant de l'équation de Newton en particulier'
    cf: https://femto-physique.fr/analyse-numerique/runge-kutta.php
    "On lui donne les dérivées et elle nous calcule les intégrales"

    Méthode de Runge-Kutta du 4ème ordre pour résoudre le
    problème aux valeurs initiales {x}' = {F(t,{x})}, où
    {x} = {x[0],x[1],...x[n-1]}.
    t,x = conditions initiales
    tStop = valeur finale de t (marquant la fin de l'intégration)
    h = incrément de t utilisé pour l'intégration'
    F = fonction à intégrer décrite par l'utilisateur et retournant
    le array F(t,x) = {x'[0],x'[1],...,x'[n-1]}.
    """
    
    k1 = h*F(t,         x          )[0] # index to get 1st array : new values
    k2 = h*F(t + h/2.0, x + k1/2.0 )[0] # "
    k3 = h*F(t + h/2.0, x + k2/2.0 )[0] # "
    k4 = h*F(t + h,     x + k3     )[0] # "
    increase = (k1 + 2.0*k2 + 2.0*k3 + k4)/6.0

    result = x + increase
    # print (':', end='')
    return result

# Numerical integration scheme using the Runge Kutta method
def simulate(xyz, Fxyz, timeCond):
    """
    Executes the calculation loops: iterates for each time step
    
    Parameters
    ----------
    xyz: 2D np.array of float
        actual values of mandatory quantities of modeled dimensions
        1st dim  is quantity [qtty,:] (eg. position, velovity, acceleration)
        2nd dim  is dimension [:,dim] (eg. X, psi, current)

    Fxyz : Function
        Physical relationships constituting the model: Behavior law
        
    timeCond : list of floats
        start, stop and step values.

    Returns
    -------
    All the results are returned as a series of np.array
    
    np.array of floats
        the TIME of each line.
    np.array of floats
        the INTEGRALS calculated by the model function (integrals updated)
    np.array of floats
        the highest order DERIVATIVE (as they are lost in the integral array)
    np.array of floats
        OUTPUT (bonus) values produced by model function not part of the derivative-integral loop
    """

    t,tStop,h = timeCond
    
    # Initialization of solution vectors
    arr_time   = [] # temps
    arr_values = [] # results 
    arr_deriv  = [] # highest order derivatives
    arr_outVal = [] # outVal quantities
    # We write the initial solution as the first element of the vector
    arr_time.append(t) # time
    arr_values.append(xyz) # initial physical quantities
    # print ('>> Framework.simulate: init derivatives')
    arr_deriv.append(Fxyz(t, xyz)[1]) # derivatives
    # print ('>> Framework.simulate: init ouVals')
    arr_outVal.append(Fxyz(t, xyz)[2]) # outVal
    
    # Numerical integration loop
    nextalive = alive = 10/100  # percent to monitor on console
    while t < tStop: # ends at time tStop
        # print ('>> Framework.simulate: -----------loop')
        h = min(h,tStop - t) # correction of h to manage that the last iteration doesn't overshoot
        lti.LTI.h = h # as we are not on a physical controller but in a simulation (MATRIX ;-) step is predefined for LTI
        # Calculation of the new values of x and t
        # print ('>> Framework.simulate: deriv actuals')
        deriv=Fxyz(t, xyz)[1] # calculates derivatives (causes) with old values!
        # print('>> Framework.simulate: Runge Kutta')
        xyz = RK4(xyz, Fxyz, t, h) # new values calculated with Runge-Kutta "integration"
        # print ('>> Framework.simulate: out actuals')
        out=Fxyz(t, xyz, True)[2] # calculates outVal with new values. Request increment of totalizers !
        
        t = t + h
        arr_time.append(t)
        arr_values.append(xyz)
        arr_deriv.append(deriv)# derivative quantities
        arr_outVal.append(out)# outVal quantities
        
        if t/tStop >= nextalive : 
            print(f"{int(t/tStop*100)}%... ", end = '')
            nextalive += alive

    return np.array(arr_time),np.array(arr_values), np.array(arr_deriv), np.array(arr_outVal) # returns arr_values[time, quantity, dimension]
