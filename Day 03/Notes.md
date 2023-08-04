# Day 3 (29 June 2023)

## [Datastructures and Algorithms](https://www.programiz.com/dsa)

## Divide and Conquer Algorithm

A **divide and conquer algorithm** is a strategy of solving a large problem by:

1. breaking the problem into smaller sub-problems
2. solving the sub-problems, and
3. combining them to get the desired output.

To use the divide and conquer algorithm, **recursion** is used.

### How Divide and Conquer Algorithms Work?

Here are the steps involved:

1. **Divide:** Divide the given problem into sub-problems using recursion.
2. **Conquer:** Solve the smaller sub-problems recursively. If the subproblems is small enough, then solve it directly.
3. **Combine:** Combine the solutions of the sub-problems that are part of the recursive process to solve the actual problem.

Let us understand this concept with the help of an example.

Here, we will sort an array using the divide and conquer approach (i.e. merge sort).

1. Let the given array be:
   ![Array for merge sort](image.png)

2. **Divide** the array into two halves.
   ![Divide the array into two subparts](image-1.png)

Again, divide each subpart recursively into two halves until you get individual elements.
![Divide the array into smaller subparts](image-2.png)

3. Now, Combine the individual elements in a sorted manner. Here, **conquer** and **combine** steps go side by side.
   ![Combine the subparts](image-3.png)

### Time Complexity

The complexity of the divide and conquer algorithm is calculated using the mater theorem.

```
T(n) = aT(n/b) + f(n),
where,
n = size of input
a = number of subproblems in the recursion
n/b = size of each subproblem. All subproblems are assumed to have the same size.
f(n) = cost of the work done outside the recursive call, which includes the cost of dividing the problem and cost of
 merging the solutions
```

Let us take an example to find the time complexity of a recursive problem.

For a merge sort, the equation can be written as:

```
T(n) = aT(n/b) + f(n)
     = 2T(n/2) + O(n)
Where,
a = 2 (each time, a problem is divided into 2 subproblems)
n/b = n/2 (size of each sub problem is half of the input)
f(n) = time taken to divide the problem and merging the subproblems
T(n/2) = O(n log n) (To understand this, please refer to the master theorem.)

Now, T(n) = 2T(n log n) + O(n)
          ≈ O(n log n)
```

### Divide and Conquer Vs Dynamic approach

The divide and conquer approach divides a problem into smaller sub-problems; these subproblems are further solved recursively. The result of each subproblem is not stored for future reference, whereas, in a dynamic approach, the result of each subproblem is stored for future reference.

Use the divide and conquer approach when the same subproblem is not solved multiple times. Use the dynamic approach when the same subproblem is to be used multiple times in the future.

Lets us understand this with an example. Suppose we are trying to find the Fibonacci series. Then,

#### Divide and Conquer Approach:

```
fib(n)
    If n < 2, return 1
    Else , return f(n - 1) + f(n -2)
```

#### Dynamic Approach:

```
mem = []
fib(n)
    If n in mem: return mem[n]
    else,
        If n < 2, f = 1
        else , f = f(n - 1) + f(n -2)
        mem[n] = f
        return f
```

In a dynamic approach, `mem` stores the result of each subproblem.

### Advantages of Divide and Conquer Algorithm

- The complexity for the multiplication of two matrices using the naive method is `O(n^3)`, whereas using the divide and conquer approach (i.e. Strassen's matrix multiplication) is `O(n^2)`. This approach also simplifies other problems, such as the Tower of Hanoi.
- This approach is suitable for multiprocessing systems.
- It makes efficient use of memory caches.

## [Data Structures & Algorithms in Python (Google)](https://learn.udacity.com/courses/ud513)

## Introduction

Will be learning:

- Algorithms
- Data Structures

### Course Outline

1. Introduction and Efficiency
   - Course Introduction
   - Syntax
   - Efficiency
   - Notation of Efficiency
2. List-Based Collections
   - Lists/Arrays
   - Linked Lists
   - Stacks
   - Queues
   - Searching and Sorting
   - Binary Search
   - Recursion
   - Bubble Sort
   - Merge Sort
   - Quick Sort
   - Maps and Hashing
   - Maps
   - Hashing
   - Collisions
   - Hashing Conventions
3. Trees
   - Trees
   - Tree Traversal
   - Binary Trees
   - Binary Search Trees
   - Heaps
   - Self-Balancing Trees
4. Graphs
   - Graphs
   - Graph Properties
   - Graph Representation
   - Graph Traversal
   - Graph Paths
5. Case Studies in Algorithms
   - Shortest Path Problem
   - Knapsack Problem
   - Traveling Salesman Problem
6. Technical Interview Tips
   - Mock Interview Breakdown
   - Additional Tips
   - Practice with Pramp
   - Next Steps

**Wrote some codes in Day 3/DSA(Google)**
