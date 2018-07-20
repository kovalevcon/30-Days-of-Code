#!/bin/python3

# import sys


S = input().strip()

try:
    res = int(S)
except ValueError:
    res = 'Bad String'

print(res)
