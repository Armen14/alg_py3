#!/usr/bin/python
# -*- coding:utf-8 -*-

import numpy as np

class BubbleSort(object):
    def __init__(self, array_elements):
        self.array_elements = array_elements

    def b_sort(self):
        for i in range(len(self.array_elements)):
            for j in range(len(self.array_elements) - 1, i, -1):
                if self.array_elements[j] < self.array_elements[j - 1]:
                    self.array_elements[j], self.array_elements[j - 1] = self.array_elements[j - 1], self.array_elements[j]
        return self.array_elements

if __name__ == '__main__':
    sort = BubbleSort(np.random.sample(1000))
    print(sort.b_sort())
