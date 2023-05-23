from typing import List
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        visited = [[0]*n for _ in range(n)]
        def dfs(i, j, prev):    
            # print(f"dfs{i,j, prev, matrix}")
            
                
            new_i, new_j = j, n-i-1 #새로운 좌표
            if visited[new_i][new_j] ==0:
                visited[new_i][new_j] =1
            # prev = matrix[new_i][new_j] #원래 그 자리에 있던 값
                value = matrix[new_i][new_j]
                matrix[new_i][new_j] = prev#값 교체
                
                dfs(new_i, new_j, value)
        for i in range(n):
            for j in range(n):
                # visited[i][j] =1
                dfs(i,j,matrix[i][j])
        return matrix
            