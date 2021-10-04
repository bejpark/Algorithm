def solution(new_id):
    answer = ''
    remove_str='~!@#$%^&*()=+[{}]:?,<>/'
    #1
    id_list=list(new_id.lower())
    #2
    i=0 #for 내에서 pop사용 시 idx가 하나씩 밀리는 문제 발생. while사용해서 idx를 직접 제어
    while(i<len(id_list)):
        if id_list[i] in remove_str:
            id_list.pop(i)
        else:
            i+=1
    #3
    i=0
    while(i<len(id_list)-1):
        if id_list[i] =='.':
            if id_list[i+1]=='.':
                id_list.pop(i+1)
            else:
                i+=1
        else:
            i+=1
    #4
    if id_list[0]=='.':
        id_list.pop(0)
    if len(id_list)>1 and id_list[-1]=='.':
        id_list.pop()
    #5
    if len(id_list)==0:
        id_list.append('a')
    #6
    while(len(id_list)>15):
        id_list.pop()
    if len(id_list)>1 and id_list[-1]=='.':
        id_list.pop()
    #7
    while(len(id_list)<3):
        id_list.append(id_list[-1])
    answer=''.join(id_list)
    return answer
