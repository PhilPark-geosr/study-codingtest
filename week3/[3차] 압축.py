def solution(msg):
    import collections
    # make q
    q = collections.deque()
    for char in msg: #O(n)
        q.append(char)
    # make a index dic
    dic = dict()
    min_idx = ord('A')
    # max_idx = ord('Z')
    # A ~ Z까지 색인번호 추가
    for i in range(1, 27):
        dic[chr(min_idx+i-1)] = i

    largest_idx = 26
    answer = []
    while q:
        # print(q)
        w = q.popleft()
        c= ""
        for i in range(len(q)):
            if w + q[0] in dic:
                w = w+ q[0]
                q.popleft()
            else:
                c = q[0]
                break
        # print(w+c)
        # 단어출력
        answer.append(dic[w]) #O(1)
        # 단어추가
        dic[w+c] = largest_idx+1
        largest_idx = largest_idx+1
        
    return answer