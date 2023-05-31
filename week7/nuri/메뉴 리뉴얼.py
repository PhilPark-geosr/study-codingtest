from itertools import combinations
from collections import Counter

def solution(orders, course):
    candidates = []
    cnts = Counter()
    for v in orders:
        lst = sorted(list(v))
        for i in course:
            cnts += Counter(combinations(lst, i))

    maxCnts = {k:0 for k in course}
    for v, cnt in cnts.most_common():
        if cnt >= 2 and cnt >= maxCnts[len(v)]:
            candidates.append(''.join(v))
            maxCnts[len(v)] = cnt
        
    return sorted(candidates)