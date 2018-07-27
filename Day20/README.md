# 30 Days of Code - Day 20

To view solutions, see the file `bubble-sort.py` in your text editor.

## Day 20: Sorting

**Task**:

Given an array, `a`, of size `n` distinct elements, sort the array in ascending order using the `Bubble Sort` algorithm
above. Once sorted, print the following `3` lines:

1. `Array is sorted in numSwaps swaps.` where `numSwaps` is the number of swaps that took place.

2. `First Element: firstElement` where `firstElement` is the first element in the sorted array.

3. `Last Element: lastElement` where `lastElement` is the last element in the sorted array.

**Hint**: To complete this challenge, you will need to add a variable that keeps a running tally of all swaps that
occur during execution. 

**Input Format**

The first line contains an integer, `n`, denoting the number of elements in array `a`.
The second line contains `n` space-separated integers describing the respective values of `a0, a1, ... a(n-1)`.

**Constraints**

* `2 <= n <= 600`
* `1 <= a(i) <= 2 x pow(10, 6)`, where `0 <= i < n`

**Output Format**

Print the following three lines of output:

1. `Array is sorted in numSwaps swaps` where `numSwaps` is the number of swaps that took place.

2. `First Element: firstElement` where `firstElement` is the first element in the sorted array.

3. `Last Element: lastElement` where `lastElement` is the last element in the sorted array.

**Sample Input**

```
3
1 2 3
```

**Sample Output**

```
Array is sorted in 0 swaps.
First Element: 1
Last Element: 3
```

**Solution**:

In `bubble-sort.py`.

Return to [navigation list](/README.md "navigation list")