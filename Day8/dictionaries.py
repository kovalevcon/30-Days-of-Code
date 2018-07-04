#!/bin/python3

n = int(input())
dictionary = dict(input().split() for _ in range(n))

for i in range(n):
    find = str(input())
    if find in dictionary:
        print(find + '=' + dictionary.get(find))
    else:
        print('Not found')
