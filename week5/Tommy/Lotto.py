score = {
    6: 1,
    5: 2,
    4: 3,
    3: 4,
    2: 5,
    1: 6,
    0: 6
}


def solution(lottos, win_nums):
    return [
        score[len(set(lottos) & set(win_nums)) + lottos.count(0)],
        score[len(set(lottos) & set(win_nums))]
        ]
