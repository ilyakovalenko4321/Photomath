import numpy as np


def max_y(num_1, num_2, size, side_of_trim):
	if num_1.shape[0] > num_2.shape[0]:
		y = num_1.shape[0]
		y = y - num_2.shape[0]
		num_2 = np.concatenate((num_2, np.zeros((y, num_2.shape[1]))), axis=0)
		if side_of_trim == 'LEFT':
			i = np.concatenate((num_1, num_2), axis=1)
		else:
			i = np.concatenate((num_2, num_1), axis=1)
		return i
	else:
		y = num_2.shape[0]
		y = y - num_1.shape[0]
		num_1 = np.concatenate((num_1, np.zeros((y, num_1.shape[1]))), axis=0)
		if side_of_trim == 'LEFT':
			i = np.concatenate((num_1, num_2), axis=1)
		else:
			i = np.concatenate((num_2, num_1), axis=1)
		return i


def number_creator(num_1, num_2, side_of_trim='LEFT'):
	"""Использовать цикл for.
		Соединяет несколько объектов в 1"""
	size = 560
	if num_1.shape[1] + num_2.shape[1] == size:
		y_1 = 28 - num_1.shape[0]
		y_2 = 28 - num_2.shape[0]
		num_1 = np.concatenate((np.zeros((y_1, num_1.shape[1])), num_1), axis=0)
		num_2 = np.concatenate((np.zeros((y_2, num_2.shape[1])), num_2), axis=0)
		i = np.concatenate((num_1, num_2), axis=1)
		return i
	if num_1.shape[1] + num_2.shape[1] <= size:
		'''Сделать pad по Х'''
		max_pad_x = size - (num_1.shape[1] + num_2.shape[1])
		pad_x = np.random.randint(0, 3)
		num_1 = np.concatenate((num_1, np.zeros((num_1.shape[0], pad_x))), axis=1)
		i = max_y(num_1, num_2, size, side_of_trim)
		return i

	if num_1.shape[1] + num_2.shape[1] > size:
		pass



