#!/bin/python3

# import math
# import os
# import random
# import re
# import sys


# if __name__ == '__main__':
#     arr = []
#
#     for _ in range(6):
#         arr.append(list(map(int, input().rstrip().split())))

arr = [
    [1, 1, 1, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [1, 1, 1, 0, 0, 0],
    [0, 0, 2, 4, 4, 0],
    [0, 0, 0, 2, 0, 0],
    [0, 0, 1, 2, 4, 0],
]
# arr = [[random.randint(-9, 9) for x in range(6)] for y in range(6)]

hourglass_sums = []
for i in range(4):
    for j in range(4):
        hourglass_sums.append(
            arr[i][j] + arr[i][j + 1] + arr[i][j + 2] +  # first line
            arr[i + 1][j + 1] +  # second line
            arr[i + 2][j] + arr[i + 2][j + 1] + arr[i + 2][j + 2]  # third line
        )

print(max(hourglass_sums))
