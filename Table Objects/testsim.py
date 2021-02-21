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


#intialize
pygame.init()
clock = pygame.time.Clock()
pygame.display.set_caption('plip plop')


#setup
border = Border(BORDER_POSITION[0],BORDER_POSITION[1])
puck = Puck(STRIKER_POSITION[0]+50,STRIKER_POSITION[1]+10)
striker = Striker(STRIKER_POSITION[0],STRIKER_POSITION[1])
win = pygame.display.set_mode((FACE_LENGTH,ScreenWidth))
pygame.display.set_caption('plip plop')





def mousemov():
    mpos = pygame.mouse.get_pos()
    if mpos == puck.position:
        puck.bounce1()

puck.addSpeed(1,4)




while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit

            #puck.bounce1()

        striker.StrikerEyes()
        #draw

        win.fill(GREY)
        border.draw(win)
        puck.drawTL(win,border)
        puck.draw(win)
        puck.drawStrikercorr(win, striker)
        striker.draw(win)
        puck.addSpeed(0,1)




        puck.updatedrawpos()
        puck.writetoscreen(win)
        puck.bounceb(border)







        #updates
        pygame.display.update()
        clock.tick(10)
