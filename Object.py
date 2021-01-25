# **************************************************************************** #
# Air Hockey Table Project

# Author: Ricardo Valverde
# -------------------------

#This Code is Created for UCR's EE175 Senior Design Project

# This Code contains The Objects

#For Pygame Documentation please see:
#https://www.pygame.org/docs/index.html

# **************************************************************************** #
import pygame , sys
import numpy as np
from Filtertest import Filter

global width,height
width = 900
height = 960
def puck_animation():
    global puck_speed_x,puck_speed_y

    puck.x += puck_speed_x
    puck.y += puck_speed_y


    if puck.colliderect(border[0]) or puck.colliderect(border[3]):
        puck_speed_x *=-1
    if puck.colliderect(border[1]) or puck.colliderect(border[2]):
        puck_speed_y *=-1

#intialize
pygame.init()
clock = pygame.time.Clock()
Kf = Filter()

#otherstuff practice
screen_w = 900
screen_h = 960
screen = pygame.display.set_mode((screen_w,screen_h))
pygame.display.set_caption('plip plop')
puck_speed_x = 2
puck_speed_y = 2
center1 = np.array([width/2 -12,height/2 - 12])



## other stuff

width = 900
height = 960
getlocation = [0,0]
getlocation = np.array(getlocation)

#Helper functions

def create_border(x,y,width,height):
    "creates border starting at bl postion of size width and height returns list of Objects"
    lborder = pygame.Rect(0+x,0+y,8,height)
    bborder = pygame.Rect(0+x,0+y,width,8)
    tborder = pygame.Rect(0+x,height-8+y,width,8)
    rborder = pygame.Rect(width-8+x,0+y,8,height)

    border = [lborder, bborder,tborder,rborder]

    return border;

def get_location(rectobj):
    "This returns a numpy array with location of corners [bl ,br ,tl ,tr]"
    location = rectobj.bottomleft + rectobj.bottomright + rectobj.topleft + rectobj.topright
    location = np.array(location)
    return location;

def get_trajectory(center1, center2):
    "This returns the Trajectory in a numpy array [X Y]"
    trajectory =  (np.array(center2) - np.array(center1))
    return trajectory;

def get_line_end(puck,border,trajectory):
    "This gets the coordinate at the end of the line in numpy [X Y]"
    #while
    return;



border = create_border(0, 0, width, height)
border1 = border[0]




puck = pygame.Rect(width/2 -12,height/2 - 12,25,25)
puckt = pygame.Rect(width/2 -12,height/2 - 12,1,1)


#other otherstuff
bg_color = pygame.Color('grey12')
puck_color = pygame.Color('blue2')
light_grey = pygame.Color('yellow2')
linecolor = pygame.Color('red2')



while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit


            mpos = pygame.mouse.get_pos()
            if mpos == puck.center:
                puck_speed_x = 0
                puck_speed_y = 0
            if mpos[1] <= puck.centerx:
                puck_speed_x = +3
            if mpos[1] >= puck.centerx:
                puck_speed_x = -3
            if mpos[0] <= puck.centery:
                puck_speed_x= +3
            if mpos[0] >= puck.centery:
                puck_speed_y = -3

        Kf.predict()

        z =np.array(puck.center) 

        Kf.update(z)




        ppos = Kf.x


        trajectory = get_trajectory(puck.center, ppos[0:1])
            #puckt.move(puck.centerx, puck.centery)
            #while not puckt.colliderect(border[0]) or not puckt.colliderect(border[1]) or not puckt.colliderect(border[2]) or not puckt.colliderect(border[3]):
                #puckt.x += trajectory[0]
                #puckt.y += trajectory[1]



        lineend = (np.array(puck.center) - trajectory)



        puck_animation()

        #visuals
        screen.fill(bg_color)
        pygame.draw.line(screen,linecolor,puck.center,tuple(lineend))
        pygame.draw.rect(screen,light_grey,border[0])
        pygame.draw.rect(screen,light_grey,border[1])
        pygame.draw.rect(screen,light_grey,border[2])
        pygame.draw.rect(screen,light_grey,border[3])


        pygame.draw.ellipse(screen,puck_color,puck)

        #updates
        pygame.display.flip()
        clock.tick(120)
















pygame.quit()
