#!/usr/bin/python
# -*- coding:utf-8 -*-

import numpy as np

class GnomeSort(object):
    def __init__(self, my_array):
        self.my_array = my_array

    def gnome_sort(self):
        length_array = len(self.my_array)
        i = 1
        while i < length_array:
            if not i or self.my_array[i - 1] <= self.my_array[i]:
                i += 1
            else:
                self.my_array[i], self.my_array[i - 1] = self.my_array[i - 1], self.my_array[i]
                i -= 1
        return self.my_array

if __name__ == '__main__':
    gsort = GnomeSort(np.random.sample(10))
    print(gsort.gnome_sort())
