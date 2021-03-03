def binary_search(data,search):
    if len(data)==1 and search==data[0]:
        return True
    if len(data)==1 and search!=data[0]:
        return False
    if len(data)==0:
        return False

    mid = len(data)//2
    if search == data[mid]:
        return True
    else:
        if search>data[mid]:
            return binary_search(data[mid:],search)
        else:
            return binary_search(data[:mid],search)

import random
data_list=random.sample(range(100),10)
data_list.sort()
print(data_list)
print(binary_search(data_list,100))
print(binary_search(data_list,data_list[2]))
