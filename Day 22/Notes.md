# Day 22 (21 August 2023)

## [Data Structures & Algorithms in Python (Google)](https://learn.udacity.com/courses/ud513)

### Maps

Maps are similar to dictionary where key = name and value = defination.

#### Sets

| Lists | Sets |
| ----- | ---- |
| A     | B    |
| B     | A    |
| A     | C    |

Map = {key, value}

A group of keys is a set.

A same word can have different definitions.

### Hashing

#### Hash Functions

Value --(Hash Function)--> Hash

#### Collisions

When the two hashes has same values.

Sol : Store in a Bucket

The perfect hash function depend on your data.

### Hash Maps

<Key,Value> --(Hash Function on Key)--> Hash - <k,v> - Value

### String Keys

ASCII

A = 65, B = 66, C = 67

String Keys Formula = s[0] \* 31 \*\* ( n - 1 ) + s[1] \* 31 \*\* ( n - 2 ) + ... + s[ n - 1 ]

**All the Code is in the Code Folder**
