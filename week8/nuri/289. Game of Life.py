# time complexity: O(m*n) // 최악의 경우, O(2*(m*n*8))
# space complexity: O(m*n)
class Solution:
    
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])
        c = dict()
        delta = [(0,1),(0,-1),(1,0),(-1,0),(1,1),(1,-1),(-1,1),(-1,-1)]
        checkAlive = lambda i, j: i > -1 and i < m and j > -1 and j < n and board[i][j]

        for i in range(m):
            for j in range(n):
                cnt = sum([checkAlive(i+d1, j+d2) for d1, d2 in delta])
                if board[i][j] and cnt < 2 or cnt > 3:
                    c[(i,j)] = 0
                elif not board[i][j] and cnt ==3:
                    c[(i,j)] = 1
                    
        for i, j in c:
            board[i][j] = c[(i,j)]