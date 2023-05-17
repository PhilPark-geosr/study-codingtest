import re
from collections import deque
def solution(files):
    answer = []
    files_split = []
    for f in files:
        files_split.append(re.split('(\d+)', f))
    
    files_split = deque(sorted(files_split, key=lambda x:x[0].lower()))
    
    temp = []
    print(files_split)
    while files_split:
        cur = files_split.popleft()
        if not temp or temp[-1][0].lower() == cur[0].lower():
            temp.append(cur)
        else:
            temp = sorted(temp, key=lambda x:int(x[1]))
            for t in temp:
                answer.append("".join(t))
            temp = [cur]
    
    if temp:
        temp = sorted(temp, key=lambda x:int(x[1]))
        for t in temp:
                answer.append("".join(t))
        
    return answer