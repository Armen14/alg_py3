#!/usr/bin/python
# -*- coding:utf-8 -*-

import numpy as np

class QuickSort(object):
    def __init__(self, array_list):
        self.array_list = array_list

    def q_sort(self):
        if len(self.array_list) <= 1:
            return self.q_sort(filter(lambda x: x < self.array_list[0], self.array_list[1:])) + self.array_list[0:1] + self.q_sort(filter(lambda x: x >= self.array_list[0], self.array_list[1:]))
        return self.array_list


if __name__ == '__main__':
    qs = QuickSort(np.random.sample(5))
    print(qs.q_sort())
