from typing import List


class Solution:
    @staticmethod
    def generate(numRows: int) -> List[List[int]]:
        triangle = []

        for row in range(numRows):
            row_array = []
            for col in range(row + 1):
                if col == 0 or col == row:
                    row_array.append(1)
                elif row >= 2:
                    data = triangle[row - 1][col - 1] + triangle[row - 1][col]
                    row_array.append(data)
            triangle.append(row_array)
        return triangle
