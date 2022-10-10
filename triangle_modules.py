# Modules to support exploration of triangles.

# Video Walkthrough: https://www.youtube.com/watch?v=WUvLSvT75pI

import math

def euclidean_distance(point_1, point_2):
	s = 0.0
	for i in range(len(point_1)):
		s += ((point_1[i] - point_2[i]) ** 2)
	return s ** 0.5

# Heron's Formula
def triangle_area(point_1, point_2, point_3):
	# This function makes use of Heron's Formula.
	side_1 = euclidean_distance(point_1, point_2)
	side_2 = euclidean_distance(point_2, point_3)
	side_3 = euclidean_distance(point_3, point_1)
	s = (side_1 + side_2 + side_3) / 2
	area = (s * (s - side_1) * (s - side_2) * (s - side_3)) ** 0.5
	return area

def triangle_height(point_1, point_2, point_3):
	area = triangle_area(point_1, point_2, point_3)
	h = area / (0.5 * euclidean_distance(point_2, point_3))
	return h

def in_triangle(point_1, point_2, point_3, point_P):
	area_main = triangle_area(point_1, point_2, point_3)
	area_1 = triangle_area(point_1, point_2, point_P)
	area_2 = triangle_area(point_1, point_3, point_P)
	area_3 = triangle_area(point_2, point_3, point_P)
	area_sum = area_1 + area_2 + area_3
	if area_sum - 1 < area_main < area_sum + 1:
		return True
	else:
		return False

def get_point(point, angle, length):
	angle = angle * (math.pi / 180)
	x = point[0] + length * math.cos(angle)
	y = point[1] + length * math.sin(angle)
	return (x, y)
