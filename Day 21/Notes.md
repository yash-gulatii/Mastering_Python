# Day 20 (16 August 2023)

## [Data Structures & Algorithms in Python (Google)](https://learn.udacity.com/courses/ud513)

### Sorting

#### Bubble Sort (Naive Approach)

**Algorithm -**

**Step 1 -** Check the value of i and i+1 using for loop for a array.

**Step 2-** If array[i] > array[i+1] then swap these values else pass.

**Step 3-** Print the Final Array.

**Efficiency -**

| Iteratoin | No. of Comparisons |
| --------- | ------------------ |
| 1         | n - 1              |
| 2         | n - 1              |
| 3         | n - 1              |
| 4         | n - 1              |

(n - 1)(n - 1) = n^2 - 2n + 1

=> O(n\*\*2) [Worst Case & Average Case]

=> O(n) [Best Case]

**Space Complexity -**

=> O(1)

#### Merge Sort

Uses Divide and Conquer

**Algorithm -**

**Step 1 -** Break the array into array's of containing only one element.

**Step 2-** Merge in Pairs and in Order.

**Step 3-** Repeat Step 2 till the array is sorted.

**Efficiency -**

| Array Size | Iterations |
| ---------- | ---------- |
| 1          | 0          |
| 2          | 1          |
| 3          | 2          |
| 4          | 2          |
| 5          | 3          |
| 6          | 3          |
| 7          | 3          |
| 8          | 3          |
| 9          | 4          |

=> O(n\*log(n))

Better than bubble sort.

**Space Complexity -**

Auxillary Space = O(n)

Worst than bubble sort.

#### Quick Sort

**Algorithm -**

**Step 1 -** Pick a pivot and then compare the pivot with the first element of the array.

**Step 2 -** If pivot < first element of array then move the first value in the place of pivot and move pivot to one left and the left element to the first element of the array. Else repeat step 1 with the second element of the array.

**Step 3-** Now to fix the pivot's location.

**Step 4 -** Change the pivot until all the elements position is fixed and the repeat the step 1, 2 and 3.

**Step 5 -** Print the sorted array.

**Efficiency -**

1. Worst Case - O(n\*\*2)

2. Average and Best Case - O(n\*log(n))

**Space Complexity -**

=> O(1)

**Code of Quick Sort in the Code Folder**
