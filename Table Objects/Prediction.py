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
from Filtertest import*


class Prediction(object):
    def __init__(self,x,y,bx,by):
        self.border = Border(bx,by)
        self.puck=Puck(0,0)
        self.striker = Striker(x,y)
        self.StrikerEyes()

    def getPuckVelocity(self,prePos,pos)
        pos = Vector2(Pos)
        prepos = Vecotr2(prePos)
        return(pos-prePos)

    def getPredictionLine(self,prePos,Pos):
        puck.declareVelocity = getPuckVelocity(prePos,pos)
        puck.coordinate(self.border)
        pass
