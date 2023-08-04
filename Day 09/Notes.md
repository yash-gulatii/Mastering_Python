# Day 9 (01 August 2023)

## [Datastructures and Algorithms](https://www.programiz.com/dsa)

## Decrease Key and Delete Node Operations on a Fibonacci Heap

A fibonacci heap is a tree based data structure which cosists of a collection of trees with min heap or max heap property. Its operations are more efficient in terms of time complexity than those of its similar data structures like binomial heap and binary heap.

Now, we will discuss two of its important operations.

1. **Decrease a key:** decreases the value of the key to any lower value

2. **Delete a node:** deletes the given node

### Decreasing a Key

In decreasing a key operation, the value of a key is deacreased to a lower value.

Following functions are used for decreasing the key.

#### Decrease Key

1. Select the node to be decreased, `x`, and change its value to the new value `k`.
2. If the parent of `x`, `y`, is not null and the key of parent is greater than that of the `k` then call `Cut(x)` and `Cascading-Cut(y)` subsequently.
3. If the key of `x` is smaller than the key of min, then mark `x` as min.

#### Cut

1. Remove `x` from the current position and add it to the root list.
2. If `x` is marked, then mark it as false.

#### Cascading-Cut

1. If the parent of `y` is not null then follow the following steps.
2. If `y` is unmarked, then mark `y`.
3. Else, call `Cut(y)` and `Cascading-Cut(parent of y)`.

### Decrease Key Example

The above operations can be understood in the examples below.

#### Example: Decreasing 46 to 15.

1. Decrease the value 46 to 15.

![Decrease 46 to 15](image.png)

2. **Cut part:** Since `24 != null` and `15 < its parent`, cut it and add it to the root list.
   **Cascading-Cut part:** mark 24.

![Add 15 to root list and mark 24](image-1.png)

#### Example: Decreasing 35 to 5

1. Decrease the value 35 to 5.

![Decrease 35 to 5](image-2.png)

2. **Cut part:** Since `26 != null` and `5 < its parent`, cut it and add it to the root list.

![Cut 5 and add it to root list](image-3.png)

3. **Cascading-Cut part:** Since 26 is marked, the flow goes to `Cut` and `Cascading-Cut`.
   **Cut(26):** Cut 26 and add it to the root list and mark it as false.

![Cut 26 and add it to root list](image-4.png)

**Cascadig-Cut(24):** Since the 24 is also marked, again call `Cut(24)` and `Cascading-Cut(7)`. These operations result in the tree below.

![Cut 24 and add it to root list](image-5.png)

4. Since `5 < 7`, mark 5 as min.

![Mark 5 as min](image-6.png)

### Deleting a Node

This process makes use of decrease-key and extract-min operations. The following steps are followed for deleting a node.

1. Let `k` be the node to be deleted.

2. Apply decrease-key operation to decrease the value of `k` to the lowest possible value (i.e. -∞).

3. Apply extract-min operation to remove this node.

### Decrease key and Delete ode operations in Python

```python
# Fibonacci Heap in python

import math

class FibonacciTree:
    def __init__(self, key):
        self.key = key
        self.children = []
        self.order = 0

    def add_at_end(self, t):
        self.children.append(t)
        self.order = self.order + 1

class FibonacciHeap:
    def __init__(self):
        self.trees = []
        self.least = None
        self.count = 0

    def insert(self, key):
        new_tree = FibonacciTree(key)
        self.trees.append(new_tree)
        if (self.least is None or key < self.least.key):
            self.least = new_tree
        self.count = self.count + 1

    def get_min(self):
        if self.least is None:
            return None
        return self.least.key

    def extract_min(self):
        smallest = self.least
        if smallest is not None:
            for child in smallest.children:
                self.trees.append(child)
            self.trees.remove(smallest)
            if self.trees == []:
                self.least = None
            else:
                self.least = self.trees[0]
                self.consolidate()
            self.count = self.count - 1
            return smallest.key

    def consolidate(self):
        aux = (flooe_log2(self.count) + 1) * [None]

        while self.trees != []:
            x = self.trees[0]
            order = x.order
            self.trees.remove(x)
            while aux[order] is not None:
                y = aux[order]
                if x.key > y.key:
                    x, y = y, x
                x.add_at_end(y)
                aux[order] = None
                order = order + 1
            aux[order] = x

        self.least = None
        for k in aux:
            if k is not None:
                self.trees.append(k)
                if (self.least is None or k.key < self.least.key):
                    self.least = k

def floor_log2(x):
    return math.frexp(x)[1] - 1

fheap = FibonacciHeap()

fheap.insert(11)
fheap.insert(10)
fheap.insert(39)
fheap.insert(26)
fheap.insert(24)

print('Minimum value: {}'.format(fheap.get_min()))

print('Minimum value removed: {}'.format(fheap.extract_min()))
```

### Complexities

| Name         | Time Complexity |
| ------------ | --------------- |
| Decrease Key | O(1)            |
| Delete Node  | O(log n)        |

## [Leetcode Question (Contains Duplicate) ](https://leetcode.com/problems/contains-duplicate/)

### Answer

```python
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashset = set()

        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False
```
