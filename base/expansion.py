"""Берет данные и обрезает по некоторым пунктам"""
from math import ceil
import numpy as np


def dispersion(i, extern_agreement=(28, 28)):
	"""Использовать For.
	Берет данные и обрезает по некоторым пунктам"""
	return_list = []
	f = i.shape[1]
	t = i.shape[0]
	to_brought_y, to_brought_x = extern_agreement
	min_push_x = ceil((to_brought_x - i.shape[1]) / 2)
	min_push_y = ceil((to_brought_y - i.shape[0]) / 2)
	if i.shape[1] + min_push_x * 2 == to_brought_x:
		min_push_x_1, min_push_x_2 = min_push_x, min_push_x
	else:
		min_push_x_1, min_push_x_2 = min_push_x - 1, min_push_x
	push_or_cut_x = np.random.randint(0, min_push_x_1 + 1)
	right_left = np.random.choice((-1, 1))
	if right_left == - 1:
		i = np.concatenate((np.zeros((i.shape[0], min_push_x_1 + push_or_cut_x)), i,
		                    np.zeros((i.shape[0], min_push_x_2 - push_or_cut_x))), axis=1)
		# Добавляем координаты обрезки возвращаемого списка
		return_list.append((min_push_x_1 + push_or_cut_x, min_push_x_1 + push_or_cut_x + f))
	else:
		i = np.concatenate((np.zeros((i.shape[0], min_push_x_1 - push_or_cut_x)), i,
		                    np.zeros((i.shape[0], min_push_x_2 + push_or_cut_x))), axis=1)
		# Добавляем координаты обрезки возвращаемого списка
		return_list.append((min_push_x_1 - push_or_cut_x, min_push_x_1 - push_or_cut_x + f))

	if i.shape[0] + min_push_y * 2 == to_brought_y:
		min_push_y_1, min_push_y_2 = min_push_y, min_push_y
	else:
		min_push_y_1, min_push_y_2 = min_push_y - 1, min_push_y
	push_or_cut_y = np.random.randint(0, min_push_y_1 + 1)
	up_down = np.random.choice((-1, 1))
	if up_down == -1:
		i = np.concatenate((np.zeros((min_push_y_1 - push_or_cut_y, i.shape[1])), i,
		                    np.zeros((min_push_y_2 + push_or_cut_y, i.shape[1]))), axis=0)
		# Добавляем координаты обрезки возвращаемого списка
		return_list.append((min_push_y_1 - push_or_cut_y, min_push_y_1 - push_or_cut_y + t))
	else:
		i = np.concatenate((np.zeros((min_push_y_1 + push_or_cut_y, i.shape[1])), i,
		                    np.zeros((min_push_y_2 - push_or_cut_y, i.shape[1]))), axis=0)
		# Добавляем координаты обрезки возвращаемого списка
		return_list.append((min_push_y_1 + push_or_cut_y, min_push_y_1 + push_or_cut_y + t))

	# Возвращаем обрезанный массив и координаты обрезки
	return i, return_list


