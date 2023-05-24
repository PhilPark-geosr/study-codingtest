from collections import deque
class Solution:
    def rotate(self, matrix) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        N = len(matrix)
        length = N
        for i in range(N//2):
            idx = [(i, i+j) for j in range(length)]
            idx +=  [(i+j, i+length-1) for j in range(1, length)]
            idx += [(i+length-1, i+length-1-j) for j in range(1, length)]
            idx += [(i+length-1-j, i) for j in range(1, length-1)]
            
            # print(idx)
            arr =  deque([matrix[y][x] for y, x in idx])
            idx = idx[length-1:] + idx[:length-1]
            # print(len(arr), len(idx))
            for y, x in idx:
                matrix[y][x] = arr.popleft()
            length -= 2

sol = Solution()
matrix = [[1,2,3],[4,5,6],[7,8,9]]
matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
sol.rotate(matrix)
print(matrix)

# 처음에는 left, up, right, down 배열을 따로 만들어서 풀었는데, 그러면 각 꼭짓점 부분에서 문제 발생! 