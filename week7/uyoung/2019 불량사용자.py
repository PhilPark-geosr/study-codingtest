from itertools import permutations
def solution(user_id, banned_id):
    answer = set()
    candidate = list(permutations(user_id, len(banned_id)))
    for cand in candidate:
        isSame = True
        for a, b in zip(cand, banned_id):
            if not isSame:
                break
            if len(a) != len(b):
                isSame = False
                break
                
            for idx, s in enumerate(b):
                if s != '*' and a[idx] != s:
                    isSame = False
                    break
        if isSame:
            answer.add(frozenset(cand))

    return len(answer)
                    
    
   