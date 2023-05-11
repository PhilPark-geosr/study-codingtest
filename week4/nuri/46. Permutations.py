# 풀이 1: modul 사용
from itertools import permutations
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        return [*permutations(nums,len(nums))]

# 풀이 2: DFS 
# class Solution:
#     def permute(self, nums: List[int]) -> List[List[int]]:
#         ret = []
#         def dfs(nums, perm, visited):
#             if len(perm) == len(nums):
#                 ret.append(perm)
#                 return
#             for n in nums:
#                 if n not in visited:
#                     dfs(nums, perm + [n], visited | set([n]))
#         dfs(nums,[], set())
#         return ret