# **************************************************************************** #
# Air Hockey Table Project

# Author: Ricardo Valverde
# -------------------------

#This Code is Created for UCR's EE175 Senior Design Project

# This Code contains The Puck Object

#For Pygame Documentation please see:
#https://www.pygame.org/docs/index.html

# **************************************************************************** #

import numpy as np
import math
from pygame.math import Vector2
import pygame
from Constants import*
from Border import*

#from Line_detect import*


class Puck(object):
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.position = Vector2(x,y)
        self.lastposition = Vector2(x,y)
        self.velocity = Vector2(0,0)
        self.radius = PUCK_RADIUS
        self.trajectory =Vector2(0,0)
        self.test = np.array([x,y,x,y])

    def updateSpeed(self):
        self.velocity = Vector2(x,y)
        return self.velocity


    def updatePosition(self,x,y):
        self.position = Vector2(x,y)
        self.x = x
        self.y = y


    def ulastPosition(self):
        self.lastposition = self.position - self.velocity
        return self.lastposition

    def addSpeed(self,x,y):
        self.velocity += Vector2(x,y)

    def findAngle(self):
        pos = self.ulastPosition()
        sX = self.position[0]
        sY = self.position[1]
        try:
            angle = math.atan((sY - pos[1]) / (sX - pos[0]))
        except:
            angle = math.pi / 2



        if pos[1] < sY and pos[0] > sX:
            angle = abs(angle)
        elif pos[1] < sY and pos[0] < sX:
            angle = math.pi - angle
        elif pos[1] > sY and pos[0] < sX:
            angle = math.pi + abs(angle)
        elif pos[1] > sY and pos[0] > sX:
            angle = (math.pi * 2) - angle

        return angle

    def getTrajectory(self):

        #angle = self.findAngle()
        #if angle == None:
            #return Vector2(0,0)
        #vec = Vector2( ( math.cos(angle)) ,( math.sin(angle)))
        vec = self.velocity
        nvec = vec.normalize()
        self.trajectory = nvec *25
        return self.trajectory



    def bounceB(self,Border):

        pass

    def bounce1(self):
        traj = self.getTrajectory()
        sarray = np.sign(np.array([traj[0],traj[1]]))
        result = Vector2(sarray[0]*self.velocity[0],sarray[1]*self.velocity[1])



    # For Drawing Pygame simulation purposes
    def updatedrawpos(self):
        self.position += self.velocity
        self.x += self.velocity[0]
        self.y += self.velocity[1]


    def draw(self, win):

        pygame.draw.circle(win, PUCK_COLOR, (self.x,self.y), self.radius)
        pygame.draw.line(win, PUCK_TRAJECTORY_COLOR, self.position, self.position+ self.getTrajectory())

    def writetoscreen(self, win):
        font = pygame.font.SysFont(None,25)
        msg = str(self.findAngle())
        msg2 = str(self.getTrajectory())
        color = (255,255,255)
        screen_text = font.render(msg,True,color)
        screen_text1 = font.render(msg2,True,color)
        win.blit(screen_text,[100,100])
        win.blit(screen_text1,[200,200])
