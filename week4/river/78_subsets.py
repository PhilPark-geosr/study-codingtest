import itertools
from typing import List


class Solution:
    @staticmethod
    def subsets(nums: List[int]) -> List[List[int]]:
        combinations = itertools.chain.from_iterable(itertools.combinations(nums, r) for r in range(1, len(nums) + 1))
        answer = list()
        answer.append([])
        for com in combinations:
            answer.append(list(com))
        return answer


print(Solution.subsets([1, 2, 3]))
print(Solution.subsets([0]))
