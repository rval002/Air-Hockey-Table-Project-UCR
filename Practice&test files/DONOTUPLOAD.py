## test
import pygame , sys
import numpy as np
from pygame.math import Vector2
from numpy import sign
from pygame.math import Vector2
import time

pygame.init()
clock = pygame.time.Clock()


# Color definitions
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 50, 50)
LIGHT_RED = (200, 150, 150)
DIMMED_RED = (120,60,60)
YELLOW = (255, 255, 0)
DIMMED_YELLOW = (150, 150, 0)
GREEN = (0, 255, 50)
BLUE = (50, 50, 255)
GREY = (100, 100, 100)
LIGHT_GREY = (200, 200, 200)
ORANGE = (200, 100, 50)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)
TRANS = (1, 1, 1)

class Graphics():
	def __init__(self, title, w, h):
		self.pixelWidth = w
		self.pixelHeight = h
		self.window = pygame.display.set_mode((self.pixelWidth, self.pixelHeight))
		pygame.display.set_caption(title)

	def drawBackgrond(self, color=WHITE):
		# Draw background
		self.window.fill(color)

	#----------------------------- Low level function -----------------------------
	def drawSlider(self, portion, rect = [0, 0, 100, 10]):
		pygame.draw.rect(self.window, RED, rect , 1)
		pygame.draw.rect(self.window, RED, [rect[0], rect[1], rect[2]*portion, rect[3]] , 0)

	def drawRect(self, _rect, color, thickness = None):
		if thickness is None:
			pygame.draw.rect(self.window, color, _rect)
		else:
			pygame.draw.rect(self.window, color, _rect, thickness)


	def drawCircle(self, _pos, rad, color, thickness = None):
		pos = toList(_pos)
		if thickness is None:
			pygame.gfxdraw.aacircle(self.window, *pos, rad, color)
			pygame.gfxdraw.filled_circle(self.window, *pos, rad, color)
		elif thickness == 1:
			pygame.gfxdraw.aacircle(self.window, *pos, rad, color)
		else:
			pygame.draw.circle(self.window, color, pos, rad, thickness)

	def drawPolygon(self, _vertices, color):
		pygame.draw.polygon(self.window, color, _vertices)

	def drawLine(self, startPos, endPos, color, thickness = 1):
		if thickness == 1:
			pygame.draw.aaline(self.window, color, toTuple(startPos), toTuple(endPos))
		else:
			pygame.draw.line(self.window, color, toTuple(startPos), toTuple(endPos), 5)

#intiate
while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit

	cool = Graphics("test",100,100)
	cool.drawBackgrond()
	clock.tick(30)
