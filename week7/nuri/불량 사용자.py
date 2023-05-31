from itertools import product

def isMatching(u_id, b_id):
    if len(u_id) != len(b_id): return False
    for u, b in zip(u_id, b_id):
        if b == '*': continue
        if u != b: return False
    return True

def solution(user_id, banned_id):
    result = set()
    candidate = []
    for b_id in banned_id:
        candidate += [set([str(i) for i, v in enumerate(user_id) if isMatching(v, b_id)])]

    for v in product(*candidate):
        if len(set(v)) == len(banned_id):
            result |= set([''.join(sorted(v))])
            
    return len(result)