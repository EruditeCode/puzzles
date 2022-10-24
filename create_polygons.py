# A program to create and visualise regular polygons.

# Video Walkthrough: ###

import pygame
import math
from sys import exit

def create_polygon(point, sides, distance):
	angle = 360 / sides
	angle = angle * (math.pi / 180)
	points = []
	for i in range(0, sides):
		x = point[0] + distance * math.cos(angle*i)
		y = point[1] + distance * math.sin(angle*i)
		points.append((x, y))
	return points

WIDTH = 400
HEIGHT = 400

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Polygon Generator")
clock = pygame.time.Clock()

bg = pygame.Surface((WIDTH, HEIGHT))
bg.fill((63, 62, 62))

CENTRE = (200, 200)
SHAPE_DISTANCE = 150
NUMBER_SIDES = 3
addition = 1

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			exit()

	# Displaying the background surface.
	screen.blit(bg, (0, 0))

	shape = create_polygon(CENTRE, NUMBER_SIDES, SHAPE_DISTANCE)

	for index, point in enumerate(shape):
		pygame.draw.line(screen, (240, 240, 240), point, shape[index - 1], 5)

	if NUMBER_SIDES > 15:
		addition = -1
	elif NUMBER_SIDES < 4:
		addition = 1

	NUMBER_SIDES += addition

	pygame.display.update()
	clock.tick(2)
	