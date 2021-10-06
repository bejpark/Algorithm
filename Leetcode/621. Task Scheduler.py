from collections import Counter
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        cnt = Counter(tasks)
        str_lst=list(cnt.keys())
        val_lst=list(cnt.values())
        mxval = max(val_lst)
        dupcnt=-1 #문자가 같은 수 만큼 있을 때
        for i in val_lst:
            if i==mxval:
                dupcnt+=1
                
    
        #가장 많은 문자를 처음에 두고 cooldown period 마다 실행하도록 한다.
        #중간에 어떤 형태로 다른 문자들이 와도 idle이건 상관없이 가장 많은 문자의 배치는 고정해야한다.
        #(cooldown period 보다 늘여서 배치해야할 경우는 없음)
        print(dict(cnt))
        #A x x A x x A x x A 에서 x의 수에 대한 표현식 : (max(val_list)-1)*n
        #ABCDEABCDFABCD-ABCD
        if len(tasks)-(1+n)*mxval+n-dupcnt>0:
            print("11")
            return len(tasks)
        else:
            print("22")
            return (1+n)*mxval-n+dupcnt
        
        
        max(val_list)*(n+1)
        
        
        
