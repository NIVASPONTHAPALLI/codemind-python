import math
def prime(n):
    if n<2:
        return False
    for i in range(2,int(math.sqrt(n))+1):
        if n%i==0:
            return False
    return True
def palin(n):
    n=str(n)
    n1=n[::-1]
    if n==n1:
        return True
    return False
n=int(input())
n=n+1
while n:
    if prime(n)==True and palin(n)==True:
        print(n)
        break
    n=n+1