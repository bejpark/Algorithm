#해결못함..
class Solution:
    def stoneGameVI(self, aliceValues: List[int], bobValues: List[int]) -> int:
        #각 value 간 차이가 큰 돌부터 빼내야함
        gap_a=[]
        a_score=0
        b_score=0
        canpick=[True for i in range(len(aliceValues))]
        for i in range(len(aliceValues)):
            gap_a.append((abs(aliceValues[i]-bobValues[i]),i))
        gap_a = sorted(gap_a,key= lambda x:x[0],reverse=True)
        
        a_idx=0
        b_idx=0
        print(gap_a)

        for i in range(len(gap_a)):
            x1,x2=gap_a[i]
            if i%2==0:
                a_score+=aliceValues[x2]
            else:
                b_score+=bobValues[x2]


        print(a_score,b_score)
        if a_score==b_score:
            return 0
        elif a_score>b_score:
            return 1
        else:
            return -1
