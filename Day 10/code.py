
# Question 1 - Approach 1

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        x = [*s]
        y = [*t]
        x.sort()
        y.sort()
        if x == y:
            print(True)
        else:
            print(False)

obj = Solution()

obj.isAnagram("yash", "shyya")
