# **************************************************************************** #
# Air Hockey Table Project

# Author: Ricardo Valverde
# -------------------------

#This Code is Created for UCR's EE175 Senior Design Project

# This Code contains The Objects of the game pertaining to path prediction


# **************************************************************************** #
#import packages
import numpy as np







class TableObject():
    def __init__(self,startpos = [0,0], shape = 'round', size=[0,0]):
        if shape == 'round':
            self.center = startpos
            self.radius = size[0]
            self.shape = shape
        else:
            self.startpos = startpos
            self.length = size[0]
            self.width = size[1]
            self.shape = shape

    def get_location(self):
        if self.shape == 'round':
            print(self.center)
        else:
            print(self.startpos[0] ,self.startpos[0] + self.length, self.startpos[1],
            self.startpos[1]+self.width)



faceborder = TableObject([100,200], shape = 'box', size = [1000,1000])
#puck = TableObject([0,0],size = 25)

faceborder.get_location()







#class PathPredict():
    #def __init__(self):
