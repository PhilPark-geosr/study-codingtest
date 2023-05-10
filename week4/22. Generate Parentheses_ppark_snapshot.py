from typing import List, Deque

#시간초과풀이
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        import collections
        # check well-formed parentheses
        def convert(array):
            result = ""
            for num in array:
                if num ==1:
                    result+="("
                else:
                    result+=")"
            return result
        def check(array:List) -> bool:
            temp = []
            for i in range(len(array)-1, -1, -1):
                # print(temp)
                if len(temp) ==0:
                    if array[i] ==1:
                        return False
                    else:
                        # elem = array.pop()
                        temp.append(-1)
                else:
                    if array[i] ==1:
                        # array.pop()
                        temp.pop()
                    else:
                        # elem = array.pop()
                        temp.append(-1)

            if len(temp) ==0:
                return True
            else:
                return False
        import itertools
        # 경우의 수 생성
        baselist = []
        for _ in range(n):
            baselist.append(1)
            baselist.append(-1)
        # print(baselist)
        caselist = list(map(list, itertools.permutations(baselist, 2*n)))
        # print(caselist)
        answer = set()
        for case in caselist:
            
            if check(case) == True:
                answer.add(convert(case))
        return list(answer)