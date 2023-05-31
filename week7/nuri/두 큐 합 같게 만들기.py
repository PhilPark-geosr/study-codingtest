from collections import deque

def solution(queue1, queue2):
    sum_q1 = sum(queue1)
    total = sum_q1 + sum(queue2)
    target = total // 2
    if total % 2 != 0: return -1
    if sum_q1 == target: return 0
    
    cnt = 0
    q1, q2 = deque(queue1), deque(queue2)
    while cnt < len(queue1) * 3 and q1 and q2:
        cnt += 1  
        if sum_q1 > target:
            q2.append(q1.popleft())
            sum_q1 -= q2[-1]
        else:
            q1.append(q2.popleft())
            sum_q1 += q1[-1]
        if sum_q1 == target: return cnt  
    
    return -1