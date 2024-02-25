from base import big_digits
import numpy as np
import os


"Creating the data and increasing volume of memory"
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
number_list, banner_list_to_return, pre_first_neural_network_outputs = big_digits.big_digits(1000)
banner_list_to_return = np.asarray(banner_list_to_return)
first_neural_network_outputs = []

"Repositions coordinates in list"
for i in pre_first_neural_network_outputs:
	x_1, x_2, y_1, y_2 = i[0][0], i[0][1], i[1][0], i[1][1]
	coordinates = (x_1, y_1, x_2, y_2)
	first_neural_network_outputs.append(coordinates)

"Transformation data to tensors"
print(banner_list_to_return[1], first_neural_network_outputs[1])
first_neural_network_outputs = np.asarray(first_neural_network_outputs)
banner_list_to_return = np.asarray(banner_list_to_return)
number_list = np.asarray(number_list)
number_list = number_list.astype(np.float16)
np.save("test_images.npy", number_list)
np.save("test_banner_list", banner_list_to_return)
np.save("test_validation selection1", first_neural_network_outputs)

