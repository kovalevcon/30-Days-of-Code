#!/bin/python3

# n = int(input().strip())
# a = list(map(int, input().strip().split(' ')))
a = [3, 2, 1]  # 1, 2, 3
n = len(a)
# Write Your Code Here

num_swaps = 0
for i in range(n):
    swapped = False
    for j in range(0, n-1):
        if a[j] > a[j + 1]:
            a[j], a[j + 1] = a[j + 1], a[j]
            num_swaps += 1
            swapped = True
    if not swapped:
        break

print("Array is sorted in {} swaps.\r\n"
      "First Element: {}\r\n"
      "Last Element: {}".format(num_swaps, a[0], a[n - 1]))
