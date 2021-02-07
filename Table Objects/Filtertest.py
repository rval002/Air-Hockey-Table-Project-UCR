# **************************************************************************** #
# Air Hockey Table Project

# Author: Ricardo Valverde
# -------------------------

#This Code is Created for UCR's EE175 Senior Design Project

# This Code contains The KalmanFilter

#For filterpy Documentation please see:
#https://filterpy.readthedocs.io/en/latest/kalman/KalmanFilter.html

# **************************************************************************** #



# Import packages
import numpy as np
import filterpy
from filterpy.kalman import KalmanFilter
from filterpy.common import Q_discrete_white_noise


class Filter(KalmanFilter):
    def __init__(self,timestep=1/30,uncertainty=1000,noise=1):
        super().__init__(dim_x= 4 , dim_z = 1)

        self.x =  np.array([[0],
                         [0],
                         [0],
                         [0]])
        self.F = np.array([[1,0,timestep,0],
                         [0,1,0,timestep],
                         [0,0,1,0],
                         [0,0,0,1]])
        self.B = np.array([[((timestep**2)/2),0],
                         [0,((timestep**2)/2)],
                         [((timestep**2)/2),0],
                         [0,((timestep**2)/2)]])
        self.H = np.array([[1,0,0,0],
                         [0,1,0,0]])
        self.P *= uncertainty
        self.R = noise
        self.Q = 0.13 * np.array([[(.25*timestep**4),0,(.5*timestep**3),0],
                                [0,(.25*timestep**4),0,.5*timestep**3],
                                [.5*timestep**3,0,timestep**2,0],
                                [0,.5*timestep**3,0,timestep**2]])
        #self.Q = Q_discrete_white_noise(dim=4, dt = timestep ,var = 0.13, block_size = 1)




#while detecting:
    #predicts and updates
    #kf.predict()
    #kf.update(z)
