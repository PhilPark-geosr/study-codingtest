def solution(n, t, m, p):
    # n진수 생성기
    resdic = ['0','1','2','3','4','5','6','7','8','9','A', 'B', 'C', 'D', 'E','F']
    
    def dfs(v, n):
        if v==0:
            return
        else:
            div, res = divmod(v,n)
            dfs(div, n)
            result.append(str(resdic[res]))
    ## 숫자 만들기
    numberlist = ['0']
    number = 1
    cnt = 1
    while cnt < m*t: #O(m*t) < O(10^5)
        # print(number)
        result = []
        dfs(number, n)
        # result = ''.join(result)
        # print(result)
        cnt += len(result)
        numberlist  = numberlist + result 
        number+=1

    # print(numberlist)
    
    answer = ""
    for i in range(t): #O(t) < O(10^3)
        
        answer +=numberlist[m*i+p-1]
    # print(answer)


    return answer