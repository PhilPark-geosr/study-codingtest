def solution(user_id, banned_id):
    import itertools
    import collections
    # 전체 경우의 수 구하기
    n = len(banned_id) 
    caselist = list(map(list, itertools.permutations(user_id, n)))

    
    def valid(standard:str, target:str):
        # print(target)
        # standard 변환
        q = collections.deque()

        if len(standard) != len(target):
            return False
        for s in standard:
            q.append(s)

        for t in target:
            if t == q[0] or q[0] =="*":
                q.popleft()
            else:
                continue
        if len(q) ==0:
            return True
        else:
            return False

    
    def check(user_id, banned_id):
        # user_dic 생성
        # print(user_id, banned_id)
        user_dic = collections.defaultdict(int)
        # for user in user_id:
        #     user_dic[user] = False #사용안함처리

        # 순회하면서 확인
        check_count = 0
        for ban in banned_id:
            # print('ban', ban)
            for user in user_id:
                if user_dic[user] ==True:
                    continue

                if valid(ban, user) == True:
                    # print('user_id', user)
                    user_dic[user] +=1
                    check_count+=1
                    break
                else:
                    continue

        # print(user_dic)
        if check_count == n:
            return True
        else:
            return False




    count = 0
    result = []
    for case in caselist:
        # print(case)
        if check(case, banned_id) ==True:
            if set(case) not in result:
                result.append(set(case))

                # print("성공한케이스", case)
                count+=1
            
    
    return count



user_id = ["frodo", "fradi", "crodo", "abc123", "frodoc"]
banned_id =["fr*d*", "*rodo", "******", "******"]

answer = solution(user_id, banned_id)
print(answer)
