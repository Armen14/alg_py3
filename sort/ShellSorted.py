#!/usr/bin/python
# -*- coding:utf-8 -*-

import numpy as np

class ShellSort(object):
    def __init__(self, arr_data):
        self.arr_data = arr_data

    def new_inc(self):
        # self.arr = arr
        i = int(len(self.arr_data) / 2)
        yield i

        while i != 1:
            if i == 2:
                i = 1
            else:
                i = int(np.round(i / 2.2)) #?
            yield i

    def shell_alg(self):
        for incrimention in ShellSort(self.arr_data).new_inc():
            for i in range(incrimention, len(self.arr_data)):
                for j in range(i, incrimention - 1, -incrimention):
                    if self.arr_data[j - incrimention] < self.arr_data[j]:
                        break
                    self.arr_data[j], self.arr_data[j - incrimention] = self.arr_data[j - incrimention], self.arr_data[j]
        return self.arr_data

if __name__ == '__main__':

    shell = ShellSort(np.random.sample(100))
    print(shell.shell_alg())
