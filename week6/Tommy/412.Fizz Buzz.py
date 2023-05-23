from typing import List


class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        result: List[int] = []
        for i in range(n):
            index = i + 1
            if index % 3 == 0 and index % 5 == 0:
                result.append("FizzBuzz")
            elif index % 3 == 0:
                result.append("Fizz")
            elif index % 5 == 0:
                result.append("Buzz")
            else:
                result.append(str(index))
        return result
