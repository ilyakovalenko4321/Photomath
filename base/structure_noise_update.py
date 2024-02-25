import numpy as np
from math import ceil


def noise(array=None):
	if array is not None:
		y, x = array.shape
		array_to_add = np.random.randint(0, 102, size=(y, x))
		array_to_add = array_to_add / 255
		to_return = array + array_to_add
		divisor = np.max(to_return)
		to_return = to_return / divisor
		return to_return


def structured_noise(array=None):
	coof = 20
	if array is not None:
		average_y, average_x = array.shape
		y, x = ceil(average_y/coof), ceil(average_x/coof)
		start_coords_y = np.random.randint(0, coof)
		start_coords_x = np.random.randint(0, coof)
		for i in range(y):
			for t in range(average_x):
				o = 0.3
				if array[y*coof - start_coords_y - 1][t] == 0:
					array[y*coof - start_coords_y - 1][t] = array[y*coof - start_coords_y - 1][t] + o
				else:
					pass
			start_coords_y += coof
		for i in range(x):
			for t in range(average_y):
				o = 0.3
				if array[t][x*coof - start_coords_x - 1] == 0:
					array[t][x*coof - start_coords_x - 1] = array[t][x*coof - start_coords_x - 1] + o
				else:
					pass
			start_coords_x += coof
		return array


