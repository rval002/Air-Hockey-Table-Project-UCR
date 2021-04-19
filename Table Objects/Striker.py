# **************************************************************************** #
# Air Hockey Table Project

# Author: Ricardo Valverde
# -------------------------

#This Code is Created for UCR's EE175 Senior Design Project

# This Code contains The Puck Object Striker

#For Pygame Documentation please see:
#https://www.pygame.org/docs/index.html

# **************************************************************************** #
import math
from pygame.math import Vector2
import pygame
from Constants import*
from linex import*

class Striker(object):
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.startpos = Vector2(x,y)
        self.position = Vector2(x,y)
        self.velocity = Vector2(0,0)
        initl = (x-STRIKER_RADIUS,y+STRIKER_RADIUS)
        wl = (2*STRIKER_RADIUS,2*STRIKER_RADIUS)
        self.startRect = pygame.Rect(initl,(1,1))
        self.Rect = pygame.Rect(initl,wl)

        #these lines are the boundary lines
        self.centerxline = [(0,0),(0,0)]
        self.centeryline = [(0,0),(0,0)]

        self.xTline = [(0,0),(0,0)]
        self.xBlinet = [(0,0),(0,0)]
        self.yLline1 = [(0,0),(0,0)]
        self.yRline1 = [(0,0),(0,0)]

    def updatePosition(self,position):
        self.position = Vector2(position)

    def updateVelocity(self,vel):
        self.position += Vector2(vel)

    def getposition(self):
        return self.position


    def StrikerEyes(self):

        #get the differnce of
        radius_diff= STRIKER_RADIUS+PUCK_RADIUS

        self.centerxline = [(BORDER_POSITION[0],self.y),(BORDER_POSITION[0] + FACE_LENGTH,self.y)]
        self.centeryline = [(self.x,BORDER_POSITION[1]),(self.x+1,BORDER_POSITION[1] + FACE_WIDTH)]

        self.xTline = [(BORDER_POSITION[0],self.y-radius_diff),(BORDER_POSITION[0] + FACE_LENGTH,self.y-radius_diff)]
        self.xBlinet = [(BORDER_POSITION[0],self.y+radius_diff),(BORDER_POSITION[0] + FACE_LENGTH,self.y+radius_diff)]
        self.yLline1 = [(self.x-radius_diff,BORDER_POSITION[1]),(self.x-radius_diff,BORDER_POSITION[1] + FACE_WIDTH)]
        self.yRline1 = [(self.x+radius_diff,BORDER_POSITION[1]),(self.x+radius_diff,BORDER_POSITION[1] + FACE_WIDTH)]



    def calculateVelocity(self,dis,time):
        try:
            xvel = round(dis[0]/time[0])
        except:
            xvel = 0
        try:
            yvel = round(dis[1]/time[1])
        except:
            yvel = 0

        return Vector2(xvel,yvel)

    def movetovel(self,desiredpos,dis,time):
        x1 = self.position[0]
        x2 = desiredpos[0]
        y1 = self.position[1]
        y2 = desiredpos[1]

        velneeded = self.calculateVelocity(dis,time)


        xval = math.copysign(velneeded[0],(x2-x1))
        yval = math.copysign(velneeded[1],(y2-y1))
        yval = round(yval*5)
        self.updateVelocity((xval,yval))
        print("updatedvel")
        print(self.velocity)



    def checkcol(self,puck):
        if(self.Rect.colliderect(puck.Rect)):
            val = self.velocity * -1
            valx = val[0]
            valy = val[1]
            self.updateVelocity(xval,yval)


    def checkstart(self):
        if(self.Rect.colliderect(puck.startRect)):
            self.updateVelocity(0,0)

    def updatedrawpos(self):
        self.position += self.velocity
        self.x += self.velocity[0]
        self.y += self.velocity[1]
        self.Rect.move(self.position[0],self.position[1])

    def draw(self,win):

        #CENTER LINE FOR NOW
        pygame.draw.line(win,STRIKER_LINE_COLOR,self.centerxline[0],self.centerxline[1] , 1)
        pygame.draw.line(win,STRIKER_LINE_COLOR,self.centeryline[0],self.centeryline[1] , 1)
        #Stiker
        pygame.draw.circle(win, STRIKER_COLOR, self.position, STRIKER_RADIUS)
