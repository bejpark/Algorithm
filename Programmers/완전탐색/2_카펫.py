def solution(brown, yellow): 
    answer = []
    for i in range(1,yellow+1):
        if yellow%i==0:
            x,y = i,int(yellow/i)
            print(x,y)
            if(x>y): #곱 조합 짝들이 반복되는 부분부터 제외
                break
            else: 
                if 2*x+2*y+4==brown:
                    answer=[y+2,x+2]
                    break
    return answer

#brown,yellow는 무조건 조합해서 맞아떨어지는 구조이므로 약수 2개의 조합으로 구하면됨
#내부 x*y 라면 외부 테두리는 (x+2)*(y+2)-x*y / 2(x+1)+2(y+1) = 2x+2y+4


