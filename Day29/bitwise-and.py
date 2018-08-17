#!/bin/python3

# import math
# import os
# import random
# import re
# import sys


if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n, k = map(int, input().split())
        print(k - 1 if ((k - 1) | k) <= n else k - 2)

        # max_bitwise = 0
        # for i in range(1, n + 1):
        #     for j in range(i + 1, n + 1):
        #         bitwise = i & j
        #         if max_bitwise < bitwise < k:
        #             max_bitwise = bitwise

        # bitwises = []
        # for i in range(1, n + 1):
        #     for j in range(i + 1, n + 1):
        #         bitwises.append(i & j)
        # while len(bitwises):
        #     maximum = max(bitwises)
        #     if maximum < k:
        #         print(maximum)
        #         break
        #     bitwises.remove(maximum)
