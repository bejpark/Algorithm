def multiple(num):
    return_value=1
    for index in range(1,num+1):
        return_value =return_value*index
    return return_value

def multiple_recursive(num):
    if num<=1:
        return num
    return num*multiple(num-1)

print(multiple_recursive(5))


import random
data=random.sample(range(100),0)

def sum_list(data):
    if len(data)<=1:
        return data[0]
    return data[0] + sum_list(data[1:])

def palindrome(data):
    if len(data)<=1:
        return True
    if(data[0]==data[-1]):
        return palindrome(data[1:-1])
    else:
        return False

print(palindrome('level'))



#정수를 1,2,3합 조합으로 나타내는 방법의 수
def func(data):
    if data ==1:
        return 1
    elif data==2:
        return 2
    elif data==3:
        return 4
    else:
        return func(data-1)+func(data-2)+func(data-3)

print(func(5))
