# Day 23 (22 August 2023)

## [Data Structures & Algorithms in Python (Google)](https://learn.udacity.com/courses/ud513)

### Trees

The first element is called root. The last elements are called leaves.

- A tree must be completely connected
- There should not be a cycle

#### Tree Terms

Parent - P
Child - C
Level 1 - Ancestor / Root
Level 2 - Parents of Descendant / Children of Ancestor / Branch
Level 3 - Descendant / Childrens / Leafs
Leafs - Which elements don't have any childrens
Height - Number of edges between it and the furthest leaf on the tree
Depth - Number of edges to the root.

This is not a real family tree as childrens can only have one parent.

All the elements which are on same level and have a same parent then they are siblings.

### Tree Traversal

#### Depth-First Search (DFS)

- Pre-order
  Traverse to every level from left until every element is printed.

- In-Order
  Traverse thorough children until every element is printed. The root will me in the middle.

- Post-Order
  Traverse all the children first of a parent then the parent same with all the elements in the tree.

#### Breadth-First Search (BFS)

- Level Order
  Traverse Every Element on the same Level and Start from left to right.

### Search and Delete (Binary Search Tree)

Search Time Complexity - O(n) [linear]
Delete (leaf) Time Complexity - O(1)
Delete (parent) Time Complexity - O(n)
