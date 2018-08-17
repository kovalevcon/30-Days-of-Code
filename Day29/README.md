# 30 Days of Code - Day 29

To view solutions, see the file `bitwise-and.py` in your text editor.

## Day 29: Bitwise AND

**Task**:

Given set `S = {1, 2, 3, ..., N}`. Find two integers, `A` and `B` (where `A < B`), from set `S` such that the value of
`A & B` is the maximum possible and also less than a given integer, `K`. In this case, `&` represents the bitwise AND 
operator.

**Input Format**

The first line contains an integer, `T`, the number of test cases.
Each of the `T` subsequent lines defines a test case as `2` space-separated integers, `N` and `K`, respectively.

**Constraints**

* `1 <= T <= pow(10, 3)`
* `2 <= N <= pow(10, 3)`
* `2 <= K <= N`

**Output Format**

For each test case, print the maximum possible value of `A & B` on a new line.

**Sample Input**

```
3
5 2
8 5
2 2
```

**Sample Output**

```
1
4
0
```

**Solution**:

In `bitwise-and.py`.

Return to [navigation list](/README.md "navigation list")