def solution(queue1, queue2):
    import collections
    # 두 큐 합 계산
    # 만약 정수가 아니면 -1 리턴
    if (sum(queue1) + sum(queue2))%2 != 0:
        return -1
    target = int((sum(queue1) + sum(queue2))/2)
    sum1 = sum(queue1)
    sum2 = sum(queue2)
    
    queue1 = collections.deque(queue1)
    queue2 = collections.deque(queue2)
    n = len(queue1)
    if sum1 == sum2: #미리 같아버리면 0리턴
        return 0

    def make_same_sum(q1, q2, target, sum1, sum2):
        # 누가 더 큰지 계산
        def cal_diff(q1,q2, target, sum1, sum2):
            diff = sum1 - target #빼줘야 할만큼 계산
            temp_sum = 0
            count = 0 # 몇번 더했는지 횟수

            for _ in range(len(q1)):
                elem = q1.popleft()
                temp_sum += elem
                q2.append(elem)
                count +=1
                if temp_sum >= diff: #정확하게 딱 덜어낼수 있으면 종료
                    break
                else:
                    continue
            sum2+=temp_sum # 작은곳에다 더해주기 이러면 sum2가 커짐
            sum1-=temp_sum
            # print(sum1, sum2)
            return sum1, sum2, count
        if sum1 > sum2:
            sum1, sum2, count = cal_diff(q1, q2, target, sum1, sum2)
            
        elif sum1 < sum2:
            q1,q2 = q2, q1
            sum1, sum2 = sum2, sum1
            sum1, sum2, count = cal_diff(q1, q2, target, sum1, sum2)
        else: #같으면
            sum1, sum2, count = cal_diff(q1, q2, target, sum1, sum2)
        return q1, q2, sum1, sum2, count
    
    q1, q2, sum1, sum2, count = make_same_sum(queue1,queue2, target, sum1, sum2)
   
    # print(q1, q2, sum1, sum2, count)
    answer = count

    while sum1 != target:
        q1, q2, sum1, sum2, count = make_same_sum(q1,q2, target, sum1, sum2)
        answer += count

        # 이 부분이 핵심!
        if answer > 4*n:
            return -1
    return answer

    
    # print(answer)
queue1 = [1, 1]
queue2 = [1, 5]

res=solution(queue1, queue2)
print(res)
    # 값을 덜어낼 큐 선택

