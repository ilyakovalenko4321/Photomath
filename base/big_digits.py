"""Надо в expansion получить координаты их прикрепления по y
И там же рассчитать координаты которые мне должна вернуть 2 НС для выделения уже чисел
И понять как вырезать число из общего ряда.
Наложить шум в 6 по у и 10 по х"""

import numpy as np
from base import inl
from base import expansion
from base import Data_Base as Bd
from base import number_creation as num
from base import structure_noise_update as noise


x_train, y_train, x_test, y_test = Bd.ddd()
information_list = inl.creator(x_train)


def number_creator(digit_1, digit_2, size_of_eye, *extra_digits):
	number = num.number_creator(digit_1, digit_2)
	for r in extra_digits[0]:
		number = num.number_creator(number, r)
	number, ui = expansion.dispersion(number, size_of_eye)
	return number, ui


def big_digits(num):
	number_list = []
	ui_list = []
	banner_list_to_return = []
	for i in range(num):
		number_of_number = np.random.randint(3, 13)
		digit_list = []
		list_to_return = []
		for q in range(number_of_number):
			c = np.random.randint(len(information_list))
			digit_list.append(information_list[c])
			list_to_return.append(y_train[c])
		new_number, ui = number_creator(digit_list[0], digit_list[1], (140, 280), digit_list[2:])
		ui_list.append(ui)
		new_number = noise.structured_noise(new_number)
		number_list.append(new_number)
		u = 0
		while u < (12 - len(list_to_return)):
			list_to_return.append(np.array([0., 0., 0., 0., 0., 0., 0., 0., 0., 0.,]))
		list_to_return = np.asarray(list_to_return)
		banner_list_to_return.append(list_to_return)
	return number_list, banner_list_to_return, ui_list


