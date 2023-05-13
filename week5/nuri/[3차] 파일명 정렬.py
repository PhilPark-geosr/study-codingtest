def extract(strs, idx):
    p1, p2 = 0, len(strs)
    for i, s in enumerate(strs):
        if not p1 and s.isdigit():
            p1 = i
        if p1 and not s.isdigit():
            p2 = i
            break
    return strs[:p1].upper(), int(strs[p1:p2]), idx
            
def solution(files):
    criteria = [extract(f, i) for i, f in enumerate(files)]
    criteria.sort()
    return [files[v[-1]] for v in criteria]