import collections


def solution(m, n, board):
    answer = 0
    remove_array = set()
    board = [list(i) for i in board]

    def check(array):
        for i in range(len(array) - 1):
            for j in range(len(array[0]) - 1):
                if array[i][j] == array[i + 1][j] == array[i][j + 1] == array[i + 1][j + 1] and array[i][j] != []:
                    remove_array.add((i, j))
                    remove_array.add((i + 1, j))
                    remove_array.add((i, j + 1))
                    remove_array.add((i + 1, j + 1))

    # 빈 배열 재정렬
    def arrange(array):
        for j in range(len(array[0])):
            q = collections.deque([])
            for i in range(len(array) - 1, -1, -1):
                if not array[i][j]:
                    q.append((i, j))
                else:
                    if q:
                        qi, qj = q.popleft()
                        array[qi][qj] = array[i][j]
                        array[i][j] = []
                        q.append((i, j))

    while True:
        check(board)
        if remove_array:
            answer += len(remove_array)
            for row, col in remove_array:
                board[row][col] = []
            remove_array.clear()
            arrange(board)
        else:
            break
    return answer
