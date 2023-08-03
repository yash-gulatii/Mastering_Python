# Question 3 - Approach 1 Brute Force

# def twoSum(nums, target):

#     n = len(nums)
#     p = False

#     for i in range(n):
#         for j in range(n):
#             if nums[i]+nums[j] == target and i != j:
#                 print([i,j])
#                 p = True
#                 break
#         if p:
#             break
        

# twoSum([3,2,4], 6)

# Question 3 - Approach 2 (Better Time Complexity)

def twoSum( nums, target):
    prevMap = {}  # val -> index
    for i, n in enumerate(nums):
        diff = target - n
        print(diff)
        if diff in prevMap:
            print(prevMap[diff], i)
        prevMap[n] = i

twoSum([3,2,4], 6)