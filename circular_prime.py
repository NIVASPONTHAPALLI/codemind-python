import math
def prime(m):
    if m<2:
        return False
    for i in range(2,int(math.sqrt(m))+1):
        if m%i==0:
            return False
    return True
n=int(input())
t1=n
temp=0
while n!=0:
    p=n%10
    temp=(temp*10)+p
    n=n//10
if prime(t1):
    if prime(temp):
        print('circular prime')
    else:
        print('prime but not a circular prime')
else:
    print('not prime')