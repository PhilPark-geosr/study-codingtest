def solution(files):
 
    # Head , Number, Tail 구분하는 함수
    def pre_process(word): #O(len(word))
        # print(word)
        min_ord = ord('0')
        max_ord = ord('9')
        head = ""
        number = ""
        tail = ""
        for w in word:
            # print(w)
            if  min_ord <= ord(w) <=max_ord and len(tail)==0:
                number +=w
            else:
                if len(number) ==0:
                    head += w
                else:
                    tail += w

        return head, number, tail
            
    # pre-process O(n*max(len(word))) --> O(100*n) 워스트케이스
    tmp = []
    for file in files:
        tmp.append(pre_process(file))

    # sort O(nlogn)
    tmp.sort(key = lambda x : (x[0].lower(), x[1].zfill(5))) # zfill : 자리수 맞춰서 비교하기 위함
  
    # ex : tmp = [('img', '1', '.png'), ('IMG', '01', '.GIF'), ('img', '02', '.png'), ('img', '2', '.JPG'), ('img', '10', '.png'), ('img', '12', '.png')]
    # 결과 출력
    result = []
    for elem in tmp: #O(3*n) 이유 : join함수가 elem길이(3)에 비례
        result.append("".join(elem))

    return result
