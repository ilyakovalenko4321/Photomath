from keras.datasets import mnist
import keras


def ddd():
    (x_train, y_train), (x_test, y_test) = mnist.load_data()
    x_train = x_train / 255
    x_test = x_test / 255
    y_test = keras.utils.to_categorical(y_test, 10)
    y_train = keras.utils.to_categorical(y_train, 10)
    return x_train, y_train, x_test, y_test

