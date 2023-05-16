def solution(board, moves):
    # dic 만들기
    dic = dict()
    n = len(board)
    for i in range(1, n+1): #o(n^2)
        #i 열 추출
        line=[]
        for j in range(n-1, -1, -1):
            if board[j][i-1] ==0:
                break
            else:
                line.append(board[j][i-1])
        # dic에 추가
        dic[i] = line
        
    # 카운트하기
    stack = []
    count = 0
    for move in moves:
        if len(dic[move]) ==0:
            continue # 비어있는데 뽑을때 그냥 스킵
        else:
            elem = dic[move].pop()
            if len(stack) !=0:
                if elem == stack[-1]:
                    count+=1
                    stack.pop()
                else:
                    stack.append(elem)
            else:  #스택에 원소 없을때 
                stack.append(elem)
                
    return 2*count