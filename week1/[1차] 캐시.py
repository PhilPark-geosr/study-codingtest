def solution(cacheSize, cities):
    import collections
    
    
    # Exception Handling
    if cacheSize == 0:
        time = len(cities)*5
        return time
    
    # if len(cacheSize) > 0:
    time = 0
    q = collections.deque()
    for i in range(len(cities)):
        if len(q) < cacheSize:
            if len(q) ==0:
                time+=5
            else:
                if cities[i].lower() in q:
                    time+=1
                else:
                    time+=5
            q.append(cities[i].lower())
        else:
            # 캐시안에 있는지 검증
            flag = False
            for k in range(len(q)):
                if cities[i].lower() == q[k]:
                    flag = True
                    q.remove(cities[i].lower())
                    # break
            if flag == True: # 캐시안에서 처리되었으면
                time+=1
            else:
                time+=5
                q.popleft() # 가장 오래된 캐시 지움
            q.append(cities[i].lower())
                
    return time