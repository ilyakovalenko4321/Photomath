import numpy as np
import keras

test_images = np.load('networks/test_images.npy')
test_validation_selestion = np.load("networks/test_validation_selection1.npy")
network = keras.models.load_model('networks/!Ncoords_of_number_test.keras')
network.evaluate(test_images, test_validation_selestion)
