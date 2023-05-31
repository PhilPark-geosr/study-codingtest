def solution(board, moves):
    cnt = 0
    stack = []

    for m in moves:
        for i in range(len(board)):
            if board[i][m-1]:
                v, board[i][m-1] = board[i][m-1], 0
                if stack and stack[-1] == v:
                    stack.pop()
                    cnt += 2
                else:
                    stack.append(v)
                break
    return cnt