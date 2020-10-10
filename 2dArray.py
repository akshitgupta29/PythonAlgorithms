#!/bin/python3

import math
import os
import random
import re
import sys


if __name__ == '__main__':
    arr = [[1, 1, 1, 0, 0, 0], [0, 1, 0, 0, 0, 0], [1, 1, 1, 0, 0, 0],
           [0, 0, 2, 4, 4, 0], [0, 0, 0, 2, 0, 0], [0, 0, 1, 2, 4, 0]]

    # for _ in range(6):
    #     arr.append(list(map(int, input().rstrip().split())))
    print(arr)
    max_sum = -10000
    for j in range(4):
        for i in range(4):
            top_sum = arr[j][i] + arr[j][i+1] + arr[j][i+2]
            middle_sum = arr[j+1][i+1]
            bottom_sum = arr[j+2][i] + arr[j+2][i+1] + arr[j+2][i+2]

            total_sum = top_sum + middle_sum + bottom_sum

            if total_sum > max_sum:
                max_sum = total_sum
    print (max_sum)
