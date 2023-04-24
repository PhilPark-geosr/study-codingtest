def solution(str1, str2):
    import collections
    
    # 소문자 아스키 코드 생성
    min_idx = ord('a')
    max_idx = ord('z')
    
    # 다중집합 생성
    def make_set(word):
        result = []
        for i in range(len(word)-1):
            s1 = word[i].lower()
            s2 = word[i+1].lower()
            
            if min_idx <= ord(s1) <=max_idx and min_idx <= ord(s2) <=max_idx:
                result.append(s1+s2)
        return result
    
    # 두 집합 비교
    def intersect_len(A,B):
        # make dic
        dic = collections.defaultdict(int)
        for i in range(len(A)):
            dic[A[i]] +=1
        result =[]
        for j in range(len(B)):
            if dic[B[j]] >0:
                dic[B[j]] -=1
                result.append(B[j])
                
        # print(result)
        return len(result)
        
    
    A = make_set(str1)
    B = make_set(str2)
    # print(A, B)
    if len(A) ==0 and len(B)==0:
        return 65536
    
    len_inter = intersect_len(A,B)
    len_union = (len(A) + len(B)) - len_inter
    # 자카드 유사도
    answer = int((len_inter/len_union)*65536)
    return answer