from itertools import combinations
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        result = []
        for i in range(n+1):
            result+=list(combinations(nums, i))
        return result
        