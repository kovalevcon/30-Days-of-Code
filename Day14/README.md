# 30 Days of Code - Day 14

To view solutions, see the file `scope.py` in your text editor.

##Day 14: Scope

**Objective**:

The absolute difference between two integers, `a` and `b`, is written as `|a - b|`. The maximum absolute difference
between two integers in a set of positive integers, `elements`, is the largest absolute difference between any 
two integers in `elements`.

The Difference class is started for you in the editor. It has a private integer array (`elements`) for storing `N` 
non-negative integers, and a public integer (`maximumDifference`) for storing the maximum absolute difference.

**Task**:

Complete the Difference class by writing the following:

* A class constructor that takes an array of integers as a parameter and saves it to the `elements` instance variable.
* A computeDifference method that finds the maximum absolute difference between any `2` numbers in `N` and stores it 
in the `maximumDifference` instance variable.

**Input Format**

You are not responsible for reading any input from stdin. The locked Solution class in your editor reads in `2` 
lines of input; the first line contains `N`, and the second line describes the `elemants` array.

**Constraints**:
* `1 <= N <= 10`
* `1 <= elements[i] <= 100, where 0 <= i <= N - 1`


**Output Format**

You are not responsible for printing any output; the Solution class will print the value of the `maximumDifference`
instance variable.

**Sample Input**

```
3
1 2 5
```

**Sample Output**

```
4
```

**Solution**:

In `scope.py`.

Return to [navigation list](/README.md "navigation list")