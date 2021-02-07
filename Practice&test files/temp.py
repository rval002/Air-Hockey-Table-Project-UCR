from pygame.math import Vector2
import pygame
import numpy as np

test = Vector2(-20,31)

toup = (1,2)
testv = Vector2(toup) +toup

ntest = test.normalize()

sarray = np.sign(np.array([ntest[0],ntest[1]]))
result = Vector2(sarray[0]*test[0],sarray[1]*test[1])




print(ntest)
print(sarray)
print(result)
print(test)
print(testv)
