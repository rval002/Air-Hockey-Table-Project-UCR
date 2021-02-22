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

from linex import*


class Puck(object):
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.position = Vector2(x,y)
        self.lastposition = Vector2(x,y)
        self.velocity = Vector2(0,0)
        self.radius = PUCK_RADIUS
        self.trajectory =Vector2(0,0)
        self.PathLine1 = [(0,0),(0,0),(0,0),(0,0)]

    def declareVelocity(self,velocity):
        self.velocity = velocity


    def updateSpeed(self):
        self.velocity = (Vector2(x,y))
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
        try:
            nvec = vec.normalize()
            self.trajectory = nvec *25
        except:
            self.trajectory = vec
        # print("traject = ", self.trajectory)
        return self.trajectory



    def borderdetect(self,Border):
        #Creates lines that are used for intersection
        radilinespp = [(int(self.position[0]),int(self.position[1])),(int(self.position[0]+self.radius),int(self.position[1]+self.radius))]
        radilinesmm = [(self.position[0],self.position[1]),(self.position[0]-self.radius,self.position[1]-self.radius)]
        radilinespm = [(self.position[0],self.position[1]),(self.position[0]+self.radius,self.position[1]-self.radius)]
        radilinesmp = [(self.position[0],self.position[1]),(self.position[0]-self.radius,self.position[1]+self.radius)]

        radilines = [radilinespp, radilinesmm, radilinespm, radilinesmp]
        borderlines =[Border.leftborder,Border.topborder,Border.rightborder,Border.bottomborder]
        x1 = Border.topborder[0]
        x2 = Border.topborder[1]
        y1 = Border.topborder[2]
        y2 = Border.topborder[3]

        bord = [(x1,y1),(x2,y2)]


        for i in range(4):
            for j in range(4):



                corr = segment_intersect([(borderlines[j][0],borderlines[j][1]),(borderlines[j][2],borderlines[j][3])],radilines[i])




                if(corr == None):
                    None

                else:
                    return corr,(i, j)

        return corr,(None,None)



    def bounceb(self, Border):
        #j decides which border we are using

        corr,pos = self.borderdetect(Border)

        if not(corr == None):
            #leftborder
            if pos[1] ==  0 or 2:
                print("a")
                print(self.velocity[1])
                self.velocity[1] = self.velocity[1] *-1
            #topborder
            if pos[1] ==  1 or 3:
                self.velocity[0] = self.velocity[0] *-1





    def bounce1(self):
        traj = self.getTrajectory()
        sarray = np.sign(np.array([traj[0],traj[1]]))
        result = Vector2(sarray[0]*self.velocity[0],sarray[1]*self.velocity[1])


    def coordinate(self,Border):
        borderlines =[Border.leftborder,Border.topborder,Border.rightborder,Border.bottomborder]
        testo = Vector2( self.getTrajectory() )* 1000
        # print("testo ", testo)
        longline = [(self.position[0],self.position[1]),(self.position[0]+testo[0],self.position[1]+testo[1])]
        # print("longlin= ",longline)
        
        for j in range(4):
            corr = segment_intersect([(borderlines[j][0],borderlines[j][1]),(borderlines[j][2],borderlines[j][3])],longline)
            # print(corr)
            if(corr == None):
                corr = self.position

            else:

                self.PathLine1 = [self.position, corr]
                
                return corr

        return corr



    def strikercorr(self,Striker):
        corr = segment_intersect(Striker.centeryline,self.PathLine1)

        if (corr == None):
            return self.position
        #elif ((BORDER_POSITION[1]<= corr[1]) or (corr[1] <= (BORDER_POSITION[1] + FACE_WIDTH[1]) )):
            #return self.position


        return corr




    # For Drawing Pygame simulation purposes
    def updatedrawpos(self):
        self.position += self.velocity
        self.x += self.velocity[0]
        self.y += self.velocity[1]


    def draw(self, win):

        pygame.draw.circle(win, PUCK_COLOR, (self.x,self.y), self.radius)
        pygame.draw.line(win, PUCK_TRAJECTORY_COLOR, self.position, self.position+ self.getTrajectory())


    def drawTL(self, win,Border):
        print(self.coordinate(Border))
        pygame.draw.line(win, PUCK_PATH_COLOR, self.position+[1,1], self.coordinate(Border))

    def drawStrikercorr(self,win,Striker):
        pygame.draw.circle(win, PUCK_TRAJECTORY_COLOR,self.strikercorr(Striker), 4)

    def writetoscreen(self, win):
        font = pygame.font.SysFont(None,25)
        msg = str(self.findAngle())
        msg2 = str(self.getTrajectory())
        color = (255,255,255)
        screen_text = font.render(msg,True,color)
        screen_text1 = font.render(msg2,True,color)
        win.blit(screen_text,[100,100])
        win.blit(screen_text1,[200,200])
