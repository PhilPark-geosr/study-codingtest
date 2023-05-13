def solution(lottos, win_nums):
    win = len(set(lottos) & set(win_nums))
    zero = lottos.count(0)
    return [7 - max(win + zero, 1) ,7 - max(win, 1)]