def solution(orders, course):
    import collections
    import heapq
    graph = collections.defaultdict(int)

    menulist = []
    for order in orders:
        temp = []
        for s in order:
            temp.append(s)
        menulist.append(temp)
    # print(menulist)
    
    def make_caselist(k, menu):
        n = len(menu)
        caselist = []
        def dfs(v, result, k):
            # print(f'dfs{v, result}')
            if len(result)==k:
                caselist.append(result)
            else:
                for i in range(v+1, n):
                    dfs(i, result+menu[i], k)
        dfs(-1, "", k)
        return caselist
    
    answer = set()
    for num in course:
        caselist = set()
        for menu in menulist:
            temp = make_caselist(num, menu)
            # print(temp)
            caselist = caselist|set(temp)
        # print(caselist)
        
        coursecandidate = []
        for case in caselist:
            count=0
            for order in orders:
                m = 0
                for elem in case:
                    if elem in order:
                        m+=1
                if m == num:
                    count+=1
            if count>=2:
                
                heapq.heappush(coursecandidate,(-count, case))
                # coursecandidate.append((count, case))

        most_order= []
        max_count = 0
        while coursecandidate:
            if len(most_order) ==0:
                count, case = heapq.heappop(coursecandidate)
                count=-count
                max_count = count
                answer.add("".join(sorted(case)))
                most_order.append("".join(case))
            else:
                count, case = heapq.heappop(coursecandidate)
                count=-count
                if count < max_count:
                    break
                else:
                    answer.add("".join(sorted(case)))
                    most_order.append("".join(case))
        # print(most_order)
        # /print(coursecandidate)
        
    answer = list(answer)
    answer.sort()
    return answer