#!/bin/python3

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

arr.reverse()
arr = map(str, arr)
print(' '.join(arr))
