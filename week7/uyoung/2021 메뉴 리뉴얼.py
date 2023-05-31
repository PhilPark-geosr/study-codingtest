from itertools import combinations
from collections import defaultdict
def solution(orders, course):
    answer = []
    for courseN in course:
        dic = defaultdict(int)
        for order in orders:
            if len(order) < courseN:
                continue
            order = list(combinations(list(order), courseN))
            for orderStr in order:
                orderStr = list(orderStr)
                orderStr.sort()
                dic["".join(orderStr)] += 1
        
        if dic:
            dic = dict(sorted(dic.items(), key=lambda item: item[1], reverse=True))
            dic_keys, dic_values = list(dic.keys()), list(dic.values())
            if dic_values[0] == 1:
                continue
            for key, value in zip(dic_keys, dic_values):
                if value == dic_values[0]:
                    answer.append(key)
                else:
                    break
    answer.sort()
    return answer