visited=[]
min_val=9999

def can_switch(str1,str2):
    n=0
    for idx,val in enumerate(str1):
        if val!=str2[idx]:
            n+=1
    if n==1:
    #if len(set(list(str1)+list(str2)))==len(str1)+1: #한 글자만 다를 때 변환가능
        return True
    else:
        return False

def dfs(begin,target,words):
    global min_val
    if begin==target:
        min_val=min(min_val,len(visited))
        return
        
    for str in words:
        if str not in visited:
            if can_switch(begin,str):
                visited.append(str)
                dfs(str,target,words)
                visited.pop()
    return
                

def solution(begin, target, words):
    answer = 0
    
    if target not in words: #최초 예외(아무것도 못할 때)
        answer=0
    else:
        dfs(begin,target,words)
        answer=min_val
    return answer
