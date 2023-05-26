def primes(i):
    if i<2:
        return False
    for j in range(2,int(i/2)+1):
        if i%j==0:
            return False
    return True

n=int(input())
l=list(map(int,input().split()))
p=int(input())
cnt=0
for i in l:
    if primes(i):
        if i>=p:
            cnt+=1
print(cnt)