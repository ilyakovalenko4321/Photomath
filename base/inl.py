"""Отделение смысловой части от шума"""
import numpy as np


def trim_edges(photo):
    start = np.argwhere(photo >= 0.5).min(axis=0)
    end = np.argwhere(photo >= 0.5).max(axis=0) + 1
    return photo[tuple(map(slice, start, end))]


def creator(x_train, y_train=False):

    informative_list_answer = y_train
    informative_list = []
    for i in range(60000):
        x = x_train[i, :, :]
        x = trim_edges(x)
        informative_list.append(x)
    if informative_list_answer:
        return informative_list, informative_list_answer
    else:
        return informative_list


