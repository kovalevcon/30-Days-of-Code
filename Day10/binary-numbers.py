#!/bin/python3

# import math
# import os
# import random
# import re
# import sys


if __name__ == '__main__':
    n = int(input())

max_consecutive = 0
consecutive = 0

while(n > 0):
    if n % 2 == 1:
        consecutive += 1
        if consecutive > max_consecutive:
            max_consecutive = consecutive
    else:
        consecutive = 0
    n = int(n / 2)

print(max_consecutive)
