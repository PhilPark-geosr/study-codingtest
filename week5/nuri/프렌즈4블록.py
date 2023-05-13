def find4Block(b, m, n):
    b4 = set()
    for i in range(n-1):
        for j in range(m-1):
            v = b[i][j]
            if v == ' ': continue
            if v == b[i+1][j] and v == b[i][j+1] and v == b[i+1][j+1]:
                b4 |= set([(i,j), (i+1,j), (i,j+1), (i+1,j+1)])
    return b4

def delete4Block(board, sets, m, n):
    new = [[] * m for _ in range(n)]
    for x, y in sorted(sets):
        new[x].append(board[x][y])
    for i in range(n):
        board[i] = new[i] + [' '] * (m - len(new[i]))
    
def solution(m, n, board):
    board = [[board[i][j] for i in range(m-1, -1, -1)] for j in range(n)]
    cnt = 0
    sets = set([(i,j) for i in range(n) for j in range(m)])
    while True:
        find = find4Block(board, m, n)
        if find:
            cnt += len(find)
            delete4Block(board, sets - find, m, n)
        else:
            break
    return cnt