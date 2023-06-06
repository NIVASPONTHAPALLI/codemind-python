import math
def prime(n):
    if n<2:
        return False
    for i in range(2,int(math.sqrt(n))+1):
        if n%i==0:
            return False
    return True
n=int(input())
c=[]
for i in range(1,n+1):
    if n%i==0:
        c.append(i)
cv=0
for i in c:
    if prime(i)==False:
        cv+=1
print(cv)