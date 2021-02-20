#! /usr/bin/env python

import pygame

def slope(p1, p2) :
   try:
       r =(p2[1] - p1[1]) * 1. / (p2[0] - p1[0])

   except:
       r = 0

   return r


def y_intercept(slope, p1) :
   return p1[1] - 1. * slope * p1[0]

def intersect(line1, line2) :
   min_allowed = 1e-5   # guard against overflow
   big_value = 1e10     # use instead (if overflow would have occurred)
   m1 = slope(line1[0], line1[1])
   #print( 'm1: %d' % m1 )
   b1 = y_intercept(m1, line1[0])
  # print( 'b1: %d' % b1 )
   m2 = slope(line2[0], line2[1])
   #print( 'm2: %d' % m2 )
   b2 = y_intercept(m2, line2[0])
   #print( 'b2: %d' % b2 )
   if abs(m1 - m2) < min_allowed :
      x = big_value
   else :
      x = (b2 - b1) / (m1 - m2)
   y = m1 * x + b1
   y2 = m2 * x + b2
   #print( '(x,y,y2) = %d,%d,%d' % (x, y, y2))
   return (int(x),int(y))

def segment_intersect(line1, line2) :
   intersection_pt = intersect(line1, line2)

   #print( line1[0][0], line1[1][0], line2[0][0], line2[1][0], intersection_pt[0] )
   #print( line1[0][1], line1[1][1], line2[0][1], line2[1][1], intersection_pt[1] )

   if (line1[0][0] < line1[1][0]) :
      if intersection_pt[0] < line1[0][0] or intersection_pt[0] > line1[1][0] :
         #print( 'exit 1' )
         return None
   else :
      if intersection_pt[0] > line1[0][0] or intersection_pt[0] < line1[1][0] :
         #print( 'exit 2' )
         return None

   if (line2[0][0] < line2[1][0]) :
      if intersection_pt[0] < line2[0][0] or intersection_pt[0] > line2[1][0] :
         #print( 'exit 3' )
         return None
   else :
      if intersection_pt[0] > line2[0][0] or intersection_pt[0] < line2[1][0] :
         #print( 'exit 4' )
         return None

   return intersection_pt
