import math
def is_prime(n):
    if n<2:
        return False
    sq=int(math.sqrt(n))
    for i in range(2,sq+1):
        if n%i==0:
            return False
    return True
cnt=0
n=int(input())
p=int(input())
for i in range(n,p+1):
    if is_prime(i):
        cnt+=1
print(cnt)