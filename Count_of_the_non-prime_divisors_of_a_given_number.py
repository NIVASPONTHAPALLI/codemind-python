import math
def prime(m):
    if m<2:
        return False
    for i in range(2,int(math.sqrt(m))+1):
        if m%i==0:
            return False
    return True
n=int(input())
l=[]
l2=[]
for i in range(1,n+1):
    if n%i==0:
        l.append(i)
for j in l:
    if prime(j):
        l2.append(j)
for k in l2:
    if k in l:
        l.remove(k)
print(len(l))