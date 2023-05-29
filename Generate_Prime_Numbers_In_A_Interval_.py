import math
def prime(m):
    if m<2:
        return False
    for i in range(2,int(math.sqrt(m))+1):
        if m%i==0:
            return False
    return True

n=int(input())
e=int(input())
for i in range(n,e+1):
    if prime(i):
        print(i)