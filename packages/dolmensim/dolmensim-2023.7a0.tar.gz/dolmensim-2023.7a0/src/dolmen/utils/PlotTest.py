# -*- coding: utf-8 -*-
"""
Created on Wed Jun 21 14:41:36 2023

@author: vujic
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig, ax = plt.subplots()

scat = ax.scatter(1, 0)
x = np.linspace(0, 10)
y = np.linspace(0,10)


ax.set_xlim([0, 10])
ax.set_ylim([0,10])


    
    
    
    
###########################################################################
    def plotXY(self, Xsymbol,Ysymbol,Angle=None,FileName = 'PlotXY'):
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
        
        fig, ax = plt.subplots()
        
        ax.scatter(Xval,Yval)
        if Angle != None:
            
            # Récupérer les limites de l'axe x
            x_min, x_max = np.min(Xval), np.max(Xval)
            
            # Calculer l'étendue de l'axe x
            x_range = x_max - x_min
            
            # Calculer l'étendue de l'axe y en utilisant l'étendue de l'axe x
            y_range = x_range * (len(Yval) / len(Xval))
            
            # Obtenir la valeur moyenne de l'axe y
            y_mean = np.mean(Yval)
            
            # Calculer les limites de l'axe y en utilisant la valeur moyenne et l'étendue
            y_min, y_max = y_mean - y_range/2, y_mean + y_range/2
            
            # Définir les limites de l'axe y
            ax.set_ylim(y_min, y_max)
            
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
