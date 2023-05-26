import math
def primes(n):
    if n<2:
        return False
    for i in range(2,int(math.sqrt(n))+1):
        if n%i==0:
            return False
    return True

lower = int(input())
upper = int(input())
cnt=0
for i in range(lower,upper+1):
    if primes(i):
        cnt+=1
print(cnt)