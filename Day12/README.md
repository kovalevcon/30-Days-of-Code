# 30 Days of Code - Day 12

To view solutions, see the file `inheritance.py` in your text editor.

## Day 12: Inheritance

**Task**:

You are given two classes, Person and Student, where Person is the base class and Student is the derived class.
Completed code for Person and a declaration for Student are provided for you in the editor.
Observe that Student inherits all the properties of Person.

Complete the Student class by writing the following:

* A Student class constructor, which has `4` parameters:
    A string, `firstName`.
    A string, `lastName`.
    An integer, `id`.
    An integer array (or vector) of test scores, `scores`.
    
* A char calculate() method that calculates a Student object's average and returns the grade character representative
of their calculated average:

```
       Grading Scale
 ---------------------------
|  Letter  | Average (a)    |
|    O     | 90 <= a <= 100 |
|    E     |  80 <= a < 90  |
|    A     |  70 <= a < 80  |
|    P     |  55 <= a < 70  |
|    D     |  40 <= a < 55  |
|    T     |     a < 40     |
 ---------------------------
```

**Input Format**

The locked stub code in your editor calls your Student class constructor and passes it the necessary arguments.
It also calls the calculate method (which takes no arguments).

You are not responsible for reading the following input from stdin:
The first line contains `firstname`, `lastName`, and `id`, respectively.
The second line contains the number of test scores. The third line of space-separated integers describes `scores`.

**Constraints**

* `1 <=|firstName|, |lastName| <= 10`
* `|id| = 7`
* `0 <= score, average <= 100`

**Output Format**

This is handled by the locked stub code in your editor. Your output will be correct if your Student class
constructor and calculate() method are properly implemented.

**Sample Input**

```
Heraldo Memelli 8135627
2
100 80
```

**Sample Output**

```
 Name: Memelli, Heraldo
 ID: 8135627
 Grade: O
```

**Solution**:

In `inheritance.py`.

Return to [navigation list](/README.md "navigation list")