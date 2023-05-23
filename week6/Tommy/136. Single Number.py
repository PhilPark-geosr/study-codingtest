from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        check = {}
        for num in nums:
            if num in check:
                check.pop(num)
            else:
                check[num] = True
        return list(check.keys())[0]