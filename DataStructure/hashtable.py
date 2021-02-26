hash_table=list([0 for i in range(10)])

def hash_func(key):
    return key%5

data1='Andy'
data2='Dave'
data3='Trump'
##ord() 문자의 아스키코드 리턴
print(ord(data1[0]),ord(data2[0]),ord(data3[0]))
print(hash_func(ord(data1[0])))


def storage_data(data,value):
    key=ord(data[0])
    hash_address=hash_func(key)
    hash_table[hash_address]=value

storage_data('Andy','01022222222')
storage_data('Dave','0101010101')
storage_data('Trump','0101111111')

def get_data(data):
    key=ord(data[0])
    hash_address=hash_func(key)
    return hash_table[hash_address]

print(get_data('And'))
