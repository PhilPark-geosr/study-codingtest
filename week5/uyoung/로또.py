def solution(lottos, win_nums):
    zeroN = lottos.count(0)
    common = set(win_nums) & set(lottos)
    zero_candidate = set(win_nums) - set(lottos)

    best = 7 - len(common) - zeroN if len(common)+zeroN != 0 else 6
    worst = 7 -len(common) if len(common) != 0 else 6

    return [best, worst]