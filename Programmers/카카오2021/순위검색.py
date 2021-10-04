"""
def solution(info, query):
    answer = []
    for search in query:
        ans_num = 0 #result에 들어갈 수(조건에 일치하는 사람 수)
        search_list=search.split() #1,3,5 은 and, 나머지(0,2,4,6,7)이 값임
        
        #print(search_list)
        for str in info:
            str_list=str.split()
            x = 0 #비교하는 점수, 4개 다 같은경우 4점으로 일치
            
            for i,j in enumerate([0,2,4,6]): #i는 1부터5, j는 0,2,4,6
                if str_list[i]==search_list[j] or search_list[j]=='-':
                    x+=1
                else:
                    break
    
            if x==4 and int(str_list[4])>=int(search_list[7]): #4개 일치하고 점수도 일치할 때
                ans_num+=1
                
        answer.append(ans_num)
                    
    return answer
"""
def solution(info, query):
    answer = []
    str_list=[]
    for str in info:
        str_list.append(str.split())
    
    for search in query:
        ans_num = 0 #result에 들어갈 수(조건에 일치하는 사람 수)
        search_list=search.split() #1,3,5 은 and, 나머지(0,2,4,6,7)이 값임

        for str in str_list:
            x = 0

            for i,j in enumerate([0,2,4,6]): #i는 0부터4, j는 0,2,4,6
                if str[i][0]!=search_list[j][0] and search_list[j]!='-':
                    x=1
                    break
    
            if x==0 and int(str[4])>=int(search_list[7]): #4개 일치하고 점수도 일치할 때
                ans_num+=1
                
        answer.append(ans_num)
                    
    return answer

#효율성 실패
