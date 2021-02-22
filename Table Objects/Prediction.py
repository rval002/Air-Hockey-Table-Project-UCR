# **************************************************************************** #
# Air Hockey Table Project

# Author: Ricardo Valverde
# -------------------------

#This Code is Created for UCR's EE175 Senior Design Project

# This Code contains The Prediction file

#For Pygame Documentation please see:
#https://www.pygame.org/docs/index.html

# **************************************************************************** #
import time , sys
from pygame.math import Vector2
import pygame
from Constants import*
from linex import*
from Puck import*
from Border import*
from Striker import*
#from Filtertest import*


class Prediction(object):
    def __init__(self,Stikerpos,BorderPos):
        self.border = Border(BorderPos[0],BorderPos[1])
        self.puck = Puck(0,0)
        self.striker = Striker(Stikerpos[0],Stikerpos[1])
       


    def getPredictionLine(self,currentpos,strikerpos,velocity):
        self.striker = strikerpos
        # self.striker.StrikerEyes()
        self.puck.updatePosition(currentpos[0],currentpos[1])
        self.puck.declareVelocity =Vector2(velocity)
        coordinate = self.puck.coordinate(self.border)
        return coordinate
    

    def getNewStrikerPos(self):
        newstriker = puck.strikercorr(self.striker)
        self.strker.updatePosition(newstriker)
        return newstriker
