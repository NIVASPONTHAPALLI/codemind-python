import math
def prime(n):
    if n<2:
        return False
    for i in range(2,int(math.sqrt(n))+1):
        if n%i==0:
            return False
    return True
for i in range(int(input())):
    n=int(input())
    s=len(str(n))
    c=0
    cv=0
    for i in range(n,-1,-1):
        if prime(i)==True:
            c=i
            break
    for j in range(n,n+100):
        if prime(j)==True:
            cv=j
            break
    p=abs(n-cv)
    p1=abs(n-c)
    if p<p1:
        print(cv)
    else:
        print(c)