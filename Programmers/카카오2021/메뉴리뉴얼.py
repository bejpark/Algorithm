from itertools import combinations
from collections import Counter
def solution(orders, course):
    answer = []
    for c in course:
        comb=[]
        for order in orders:
            comb += list(map("".join,combinations(sorted(list(order)),c)))
        result_list = Counter(comb)
        if len(result_list)>0:
            max_val=max(result_list.values())
            if max_val>=2:
                answer +=[key for key,values in result_list.items() if values==max_val]
    answer.sort()
    return answer
