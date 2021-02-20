# **************************************************************************** #
# Air Hockey Table Project

# Author: Ricardo Valverde
# -------------------------

#This Code is Created for UCR's EE175 Senior Design Project

# This Code contains The Object Border

#For Pygame Documentation please see:
#https://www.pygame.org/docs/index.html

# **************************************************************************** #
from pygame.math import Vector2
import pygame
from Constants import*
from Line_detect import*

class Border(object):
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.postion = Vector2(x,y)
        self.length = FACE_LENGTH
        self.width = FACE_WIDTH


        #might not be used in some form
        # [startx , starty , endx, endy]          # start pont (0 , 0)
        self.leftborder = [x,y, x,y+self.width]  #end point ( 0,width)
        self.topborder = [x,y,x+self.length,y]    #end point ( length,0)
        self.rightborder = [x+self.length,y,x+self.length,y+self.width]
        self.bottomborder = [x,y+self.width,x+self.length,y+self.width] # (length ,width)

        self.points = [(x,y),(x+self.length,y),(x+self.length,y+self.width),(x,y+self.width)]


    # For Drawing Pygame simulation purposes
    def draw(self, win):
        pygame.draw.lines(win, BORDER_COLOR, True, self.points)