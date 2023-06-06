import math
def prime(n):
    if n<2:
        return False
    for i in range(2,int(math.sqrt(n))+1):
        if n%i==0:
            return False
    return True
n=int(input())
s=len(str(n))
if prime(n)!=True:
    print('Not Mega Prime')
  
else:
    c=0
    while n!=0:
        p=n%10
        n=n//10
        if prime(p)==True:
            c+=1
        else:
            print('Not Mega Prime')
            break
    if c==s:
        print('Mega Prime')