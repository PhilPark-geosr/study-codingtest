# 풀이 1: module 사용 
from itertools import combinations
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        arr = [[], nums]
        for i in range(1,len(nums)):
            arr.extend([*combinations(nums, i)])
        return arr

# 풀이 2: DP 
# class Solution:
#     def subsets(self, nums: List[int]) -> List[List[int]]:
#         arr = [[], [nums[0]]]
#         for n in nums[1:]:
#             arr += [v+[n] for v in arr]
#         return arr