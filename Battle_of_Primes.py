import math
def prime(n):
    if n<2:
        return False
    for i in range(2,int(math.sqrt(n))+1):
        if n%i==0:
            return False
    return True
n1=int(input())
n2=int(input())
n3=n1+n2
l=0
for i in range(n3+1,n3+100):
    if prime(i)==True:
        l=i
        break
print(l-n3)