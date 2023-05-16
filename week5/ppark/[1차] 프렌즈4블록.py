def solution(m, n, board):
    # dic 만들기(lineq별로)
    dic = dict()
    for i in range(n): #o(n^2)
        #i 열 추출
        line=[]
        for j in range(m-1, -1, -1):
            # print(board[j])
            line.append(board[j][i])
        # dic에 추가
        dic[i+1] = line
    # print(dic)
    # 제거하기
    remove_set = set()
    count = 0
    while True:
        # remove set에 있는것들 제거
        remove_list = list(remove_set)
        # print(remove_list, dic)
        for elem in remove_list:
            a, b = elem
            # print(a,b)
            dic[a][b] =0
            count+=1
        for elem in remove_list:
            a, _ = elem # 라인만 추출
            dic[a].remove(0) 
            dic[a].append("None")

        remove_set = set()
        for i in range(1, n):
            for j in range(0, m-1):
                if dic[i][j] == dic[i][j+1] and dic[i][j+1] == dic[i+1][j+1] \
                and dic[i][j] == dic[i+1][j]\
                and dic[i][j] != "None" and dic[i][j+1] != "None"\
                and dic[i+1][j] != "None" and dic[i+1][j+1] != "None":
                    remove_set.add((i,j))
                    remove_set.add((i,j+1))
                    remove_set.add((i+1,j))
                    remove_set.add((i+1,j+1))
                else:
                    continue
       
        if len(remove_set) == 0:
            break
    # print(dic)
    return count
                