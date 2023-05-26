def p(i):
    if i<2:
        return False
    for j in range(2,int(i/2)+1):
        if i%j==0:
            return False
    return True

n=int(input())
l=list(map(int,input().split()))
p1=int(input())
cnt=0
for i in l:
    if p(i):
        if i<=p1:
            cnt+=1
print(cnt)