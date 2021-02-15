# **************************************************************************** #
# Air Hockey Table Project

# Author: Ricardo Valverde
# -------------------------

#This Code is Created for UCR's EE175 Senior Design Project

# This Code contains The Puck Object Striker

#For Pygame Documentation please see:
#https://www.pygame.org/docs/index.html

# **************************************************************************** #
from pygame.math import Vector2
import pygame
from Constants import*
#from Line_detect import*

class Striker(object):
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.postion = Vector2(x,y)
        self.velocity = Vector2(0,0)

        #these lines are the boundary lines
        self.centerxline = [(0,0),(0,0)]
        self.centeryline = [(0,0),(0,0)]

        self.xTline = [(0,0),(0,0)]
        self.xBlinet = [(0,0),(0,0)]
        self.yLline1 = [(0,0),(0,0)]
        self.yRline1 = [(0,0),(0,0)]


    def StrikerEyes(self):

        #get the differnce of
        radius_diff= STRIKER_RADIUS+PUCK_RADIUS

        self.centerxline = [(BORDER_POSITION[0],self.y),(BORDER_POSITION[0] + FACE_LENGTH,self.y)]
        self.centeryline = [(self.x,BORDER_POSITION[1]),(self.x,BORDER_POSITION[1] + FACE_WIDTH)]

        self.xTline = [(BORDER_POSITION[0],self.y-radius_diff),(BORDER_POSITION[0] + FACE_LENGTH,self.y-radius_diff)]
        self.xBlinet = [(BORDER_POSITION[0],self.y+radius_diff),(BORDER_POSITION[0] + FACE_LENGTH,self.y+radius_diff)]
        self.yLline1 = [(self.x-radius_diff,BORDER_POSITION[1]),(self.x-radius_diff,BORDER_POSITION[1] + FACE_WIDTH)]
        self.yRline1 = [(self.x+radius_diff,BORDER_POSITION[1]),(self.x+radius_diff,BORDER_POSITION[1] + FACE_WIDTH)]



    def calculateVelocity(self,desiredpos):
        self.velocity = (desiredpos - self.postion)


    def draw(self,win):

        #CENTER LINE FOR NOW
        pygame.draw.line(win,STRIKER_LINE_COLOR,self.centerxline[0],self.centerxline[1] , 1)
        pygame.draw.line(win,STRIKER_LINE_COLOR,self.centeryline[0],self.centeryline[1] , 1)
        #Stiker
        pygame.draw.circle(win, STRIKER_COLOR, self.postion, STRIKER_RADIUS)
