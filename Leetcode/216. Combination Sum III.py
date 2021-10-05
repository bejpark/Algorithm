from itertools import combinations
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        num=0
        result=[]
        arr=[]
        nn=n
        for i in range(1,k+1):
            num+=i
        if num>n: #만들 수 없을 때
            return None
        
        if nn>10:
            nn=9
    
        for i in range(1,nn+1):
            arr.append(i)
        for comb in combinations(arr,k):
            if sum(comb)==n:
                result.append(list(comb))
                
    
        return result
        
