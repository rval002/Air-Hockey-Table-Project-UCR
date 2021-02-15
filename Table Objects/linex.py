#! /usr/bin/env python

import pygame

def slope(p1, p2) :
   return (p2[1] - p1[1]) * 1. / (p2[0] - p1[0])
   
def y_intercept(slope, p1) :
   return p1[1] - 1. * slope * p1[0]
   
def intersect(line1, line2) :
   min_allowed = 1e-5   # guard against overflow
   big_value = 1e10     # use instead (if overflow would have occurred)
   m1 = slope(line1[0], line1[1])
   print( 'm1: %d' % m1 )
   b1 = y_intercept(m1, line1[0])
   print( 'b1: %d' % b1 )
   m2 = slope(line2[0], line2[1])
   print( 'm2: %d' % m2 )
   b2 = y_intercept(m2, line2[0])
   print( 'b2: %d' % b2 )
   if abs(m1 - m2) < min_allowed :
      x = big_value
   else :
      x = (b2 - b1) / (m1 - m2)
   y = m1 * x + b1
   y2 = m2 * x + b2
   print( '(x,y,y2) = %d,%d,%d' % (x, y, y2))
   return (int(x),int(y))
   
def segment_intersect(line1, line2) :
   intersection_pt = intersect(line1, line2)
   
   print( line1[0][0], line1[1][0], line2[0][0], line2[1][0], intersection_pt[0] )
   print( line1[0][1], line1[1][1], line2[0][1], line2[1][1], intersection_pt[1] )
   
   if (line1[0][0] < line1[1][0]) :
      if intersection_pt[0] < line1[0][0] or intersection_pt[0] > line1[1][0] :
         print( 'exit 1' )
         return None
   else :
      if intersection_pt[0] > line1[0][0] or intersection_pt[0] < line1[1][0] :
         print( 'exit 2' )
         return None
         
   if (line2[0][0] < line2[1][0]) :
      if intersection_pt[0] < line2[0][0] or intersection_pt[0] > line2[1][0] :
         print( 'exit 3' )
         return None
   else :
      if intersection_pt[0] > line2[0][0] or intersection_pt[0] < line2[1][0] :
         print( 'exit 4' )
         return None

   return intersection_pt
   

# window dimensions
w = 800
h = 800
# slightly off-white background
bgcolor = (0xf1,0xf2,0xf3)
# black for drawing
fgcolor = (0,0,0)
# red for "active" segment endpt
redcolor = (0xff,0,0)
# CPU throttle, higher number = less CPU hogging
delay = 200
# key repeat delay, interval
key_delay = 20
key_interval = 20

# using +1 here to avoid using -1 elsewhere
screen = pygame.display.set_mode((w+1, h+1))
clock = pygame.time.Clock()
pygame.key.set_repeat(key_delay, key_interval)

line1 = [(100.,100.),(700.,700.)]
line2 = [(100.,700.),(700.,100.)]
intersection = segment_intersect(line1, line2)

screen.fill(bgcolor)
pygame.draw.aaline(screen, fgcolor, line1[0], line1[1])
pygame.draw.aaline(screen, fgcolor, line2[0], line2[1])
if intersection is not None :
   pygame.draw.circle(screen, fgcolor, intersection, 10, 2)
pygame.draw.circle(screen, redcolor, (int(line1[0][0]), int(line1[0][1])), 5, 1)    
pygame.display.flip()

active_pt = 0
prev_active_pt = 0
running = True

while running:

   for event in pygame.event.get() :
      
      if event.type == pygame.QUIT :
         running = False
         
      elif event.type == pygame.KEYDOWN :
         if event.key == pygame.K_q : 
            # quit
            running = False
            
      elif event.type == pygame.KEYUP :      
         if event.key == pygame.K_0 : 
            active_pt = 0
         elif event.key == pygame.K_1 :
            active_pt = 1         
         elif event.key == pygame.K_2 :
            active_pt = 2
         elif event.key == pygame.K_3 :
            active_pt = 3
            
         if prev_active_pt != active_pt :
            prev_active_pt = active_pt
            screen.fill(bgcolor)
            pygame.draw.aaline(screen, fgcolor, line1[0], line1[1])
            pygame.draw.aaline(screen, fgcolor, line2[0], line2[1])
            if intersection is not None :
               pygame.draw.circle(screen, fgcolor, intersection, 10, 2)               
            if (active_pt < 2) :
               red_pt = (int(line1[active_pt][0]), int(line1[active_pt][1]))
            else :
               red_pt = (int(line2[active_pt - 2][0]), int(line2[active_pt - 2][1]))
            pygame.draw.circle(screen, redcolor, red_pt, 5, 1)
            pygame.display.flip()            
            
      elif event.type == pygame.MOUSEBUTTONUP :
         # pygame.draw.circle(screen, fgcolor, pygame.mouse.get_pos(), 13, 3)
         # pygame.display.flip()
         if (active_pt < 2) :
            line1[active_pt] = pygame.mouse.get_pos()
            print( line1[active_pt] )
         else :
            line2[active_pt - 2] = pygame.mouse.get_pos()
            print( line2[active_pt - 2] )
         
         intersection = segment_intersect(line1, line2)
         screen.fill(bgcolor)
         pygame.draw.aaline(screen, fgcolor, line1[0], line1[1])
         pygame.draw.aaline(screen, fgcolor, line2[0], line2[1])
         if intersection is not None :
            pygame.draw.circle(screen, fgcolor, intersection, 10, 2)
         if (active_pt < 2) :
            pygame.draw.circle(screen, redcolor, line1[active_pt], 5, 1)
         else :
            pygame.draw.circle(screen, redcolor, line2[active_pt - 2], 5, 1)
         pygame.display.flip()
           
   # sleep   
   clock.tick(delay)
