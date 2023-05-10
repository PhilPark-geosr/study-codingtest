from typing import List
class Solution:
    # using dfs
    # def permute(self, nums: List[int]) -> List[List[int]]:
    #     n = len(nums)
        
    #     def dfs(v, result):
    #         if len(result) == n:
    #             answer.append(result)
    #         else:
    #             for i in range(n):
    #                 if visited[i] ==0:
    #                     visited[i] =1
    #                     dfs(i, result+ [nums[i]])
    #                     visited[i] =0
    #     final_answer = []
    #     for k in range(n):
    #         answer = []
    #         visited = [0]*n
    #         visited[k] =1
    #         dfs(k, [nums[k]])
    #         final_answer = final_answer  + answer
    #     return final_answer

    # do pythonic
    import itertools
    def permute(self, nums: List[int]) -> List[List[int]]:
        caselist = list(map(list, itertools.permutations(nums, len(nums))))
        
        return caselist

