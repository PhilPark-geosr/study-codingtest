'''board
[
[0,0,0,0,0],
[0,0,1,0,3],
[0,2,5,0,1],
[4,2,4,4,2],
[3,5,1,3,1]
]
'''
'''moves
[1,5,3,5,1,2,1,4]
'''
'''basket
[4,3,1,1,3,2, ,4] -> 1과 3이 사라져 답은 4가 된다
만약 정렬 한다면? [1,1,2,3,4,4] -> 1과 4가 사라지게 되는 오답이 나오게 된다
'''


def solution(board, moves):
    count = 0
    basket = []  # basket의 최대 크기는 moves의 크기와 같으므로, 공간 복잡도는 O(n) = O(moves의 크기)
    for i in moves:
        for j in range(len(board)):
            if board[j][i-1] > 0:  # 시간 복잡도는 O(n*m) = O(board의 크기 * moves의 크기)
                basket.append(board[j][i-1])
                board[j][i-1] = 0
                break

    while is_remain := [i for i in range(1, len(basket)) if basket[i - 1] == basket[i]]:
        i = is_remain[0]
        basket.pop(i)  # O(basket의 길이)
        basket.pop(i-1)
        count += 2

    return count
# 공간 복잡도는 주로 board 변수와 basket 변수 때문에 발생합니다. 여기서 board는 문제에서 주어진 2차원 배열로 이미 고정된 메모리를 차지하고 있습니다. 따라서 공간 복잡도를 계산할 때 추가적으로 고려해야 하는 부분은 basket 변수입니다. basket 변수는 moves에 따라 인형을 담을 수 있는 최대 공간이므로 최악의 경우 moves의 길이(m)에 비례하게 됩니다. 따라서 공간 복잡도는 O(m)이라고 할 수 있습니다.