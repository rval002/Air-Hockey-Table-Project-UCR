# **************************************************************************** #
# Air Hockey Table Project

# Author: Ricardo Valverde
# -------------------------

#This Code is Created for UCR's EE175 Senior Design Project

# This Code contains The test file to test table objects. Visually

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
from Timing import*


#intialize
pygame.init()
clock = pygame.time.Clock()
pygame.display.set_caption('plip plop')
ScreenWidth = 800


#setup
border = Border(BORDER_POSITION[0],BORDER_POSITION[1])
puck = Puck(STRIKER_POSITION[0]+100,STRIKER_POSITION[1]+60)
striker = Striker(STRIKER_POSITION[0],STRIKER_POSITION[1])
win = pygame.display.set_mode((FACE_LENGTH,ScreenWidth))
pygame.display.set_caption('plip plop')

mouseR = pygame.Rect(0, 0, 2, 2)


def moveit(puck,striker):

    if not(puck.position == puck.strikercorr(striker)):
        despos = puck.strikercorr(striker)
        puckpos = puck.position
        strikerpos = striker.position
        puckvel = puck.velocity

        puckdist = distance(despos,puckpos)
        sdist = distance(despos, strikerpos)

        time = sometime(puckvel, puckpos)
        striker.movetovel(despos,sdist,time)






def mousemov(mrel):

    mpos = pygame.mouse.get_pos()
    mouseR.update(mpos,(10,10))

    if mouseR.colliderect(puck.Rect):
        puck.bounce1(mrel)

def strikerb(puck, striker):
    if puck.Rect.colliderect(striker.Rect):
        puck.bounceS()


puck.addSpeed(4,1)




while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit

            mrel = pygame.mouse.get_rel()
            mousemov(mrel)

        striker.StrikerEyes()
        #draw

        win.fill(GREY)
        border.draw(win)
        puck.drawTL(win,border)
        puck.draw(win)
        puck.drawStrikercorr(win, striker)
        striker.draw(win)
        moveit(puck, striker)
        striker.updatedrawpos()
        strikerb(puck,striker)





        puck.updatedrawpos()


        puck.writetoscreen(win)
        puck.bounceb(border)







        #updates
        pygame.display.update()
        clock.tick(10)
