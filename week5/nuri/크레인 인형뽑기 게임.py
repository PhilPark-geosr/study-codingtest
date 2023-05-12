def solution(board, moves):
    ret = 0
    n = len(board)
    dic ={i+1: [board[j][i] for j in range(n-1, -1, -1) if board[j][i] ] for i in range(n)}
    stack = []
    for m in moves:
        if not dic[m]: continue
        v = dic[m].pop()
        if stack and v == stack[-1]:
            stack.pop()
            ret += 2
        else:
            stack.append(v)
    return ret