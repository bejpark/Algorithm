import itertools

def solution(numbers):
    num=[i for i in numbers]
    prime=set()
    for i in num: #한 자리수 소수들
        if isPrime(int(i)):
            prime.add(int(i))
    
    for i in range(2,len(numbers)+1): #2개 이상 (순열)
        nPr=itertools.permutations(num,i)
        for i in nPr:
            n=int(''.join(i))
            if isPrime(n):
                prime.add(n)
 
    return len(prime)



def isPrime(n):
    if n==0:
        return False
    if n !=1:
        for i in range(2,n):
            if n%i==0:
                return False
    else:
        return False
    return True
