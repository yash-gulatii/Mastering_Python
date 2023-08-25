# Day 24 (23 August 2023)

## [Leetcode (Group Anagrams)](https://leetcode.com/problems/group-anagrams/)

### Solution -

```python
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = collections.defaultdict(list)

        for s in strs:
            count = [0] * 26

            for c in s:
                count[ord(c) - ord("a")] += 1

            res[tuple(count)].append(s)

        return res.values()

```

## [Django Course by Programming with Mosh](https://www.youtube.com/watch?v=rHux0gMZ3Eg)

### What is Django?

Django is a Free and open-source **framework for building web apps** with **Python**.

#### Django Features

- The admin side
- Object-relational mapper (ORM)
- Authentication
- Caching

### Learnings in the Code

- Learned about views, urls and settings in django

**All the code is in the [Code](./Code/) Folder**
