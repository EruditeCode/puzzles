# A program to explore Viviani's Theorem.

# Video Walkthrough: https://www.youtube.com/watch?v=WUvLSvT75pI

import pygame
import triangle_modules
from sys import exit

WIDTH = 800
HEIGHT = 450

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Viviani's Theorem")
clock = pygame.time.Clock()

bg = pygame.Surface((WIDTH, HEIGHT))
bg.fill((239, 239, 239))

point_A = (100, 50)
point_B = (300, 396)
point_C = (500, 50)

point_P = (300, 165)
alpha_height, beta_height, gamma_height = 115, 115, 115


while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			exit()

	# Displaying the background surface.
	screen.blit(bg, (0, 0))

	# Drawing the lines from point P to the side of the main triangle.
	alpha = triangle_modules.get_point(point_P, 150, alpha_height)
	beta = triangle_modules.get_point(point_P, 30, beta_height)
	gamma = triangle_modules.get_point(point_P, 270, gamma_height)
	pygame.draw.line(screen, (17, 43, 60), alpha, point_P, 3)
	pygame.draw.line(screen, (32, 83, 117), beta, point_P, 3)
	pygame.draw.line(screen, (246, 107, 14), gamma, point_P, 3)

	# Drawing rectangles to show the sum of the individual lines from point P.
	alpha_rect = pygame.Rect(600, 396-alpha_height, 50, alpha_height)
	beta_rect = pygame.Rect(600, 396-alpha_height-beta_height, 50, beta_height)
	gamma_rect = pygame.Rect(600, 396-alpha_height-beta_height-gamma_height, 50, gamma_height)
	pygame.draw.rect(screen, (17, 43, 60), alpha_rect)
	pygame.draw.rect(screen, (32, 83, 117), beta_rect)
	pygame.draw.rect(screen, (246, 107, 14), gamma_rect)

	# Drawing the main triangle.
	pygame.draw.line(screen, (17, 43, 60), point_A, point_B, 5)
	pygame.draw.line(screen, (17, 43, 60), point_B, point_C, 5)
	pygame.draw.line(screen, (17, 43, 60), point_C, point_A, 5)

	mouse_check = pygame.mouse.get_pos()
	if triangle_modules.in_triangle(point_A, point_B, point_C, mouse_check):
		point_P = mouse_check
		alpha_height = triangle_modules.triangle_height(point_P, point_A, point_B)
		beta_height = triangle_modules.triangle_height(point_P, point_B, point_C)
		gamma_height = triangle_modules.triangle_height(point_P, point_C, point_A)

	pygame.display.update()
	clock.tick(60)
