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
        self.border = Border(BorderPos)
        self.puck = Puck(0,0)
        self.striker = Striker(x,y)
        self.striker.StrikerEyes()


    def getPredictionLine(self,currentpos,strikerpos,velocity):
        self.striker = self.getStrikerPosition()
        self.striker.StrikerEyes()
        self.puck.updatePosition(currentpos[0],currentpos[1])
        self.puck.declareVelocity = velocity
        coordinate = puck.coordinate(self.border)
        return self.puck.PathLine1


    def getNewStrikerPos(self):
        newstriker = puck.strikercorr(self.striker)
        self.strker.updatePosition(newstriker)
        return newstriker
