import math
def prime(n):
    if n<2:
        return False
    for i in range(2,int(math.sqrt(n))+1):
        if n%i==0:
            return False
    return True
    
n=int(input())
a=list(map(int,input().split()))
min1=a.index(min(a))
max1=a.index(max(a))
cnr=0
if min1<max1:
    for i in range(min1,max1+1):
        if prime(a[i]):
            cnr+=1
else:
    for i in range(max1,min1+1):
        if prime(a[i]):
            cnr+=1
print(cnr)