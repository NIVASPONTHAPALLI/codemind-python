def p(i):
    if i<2:
        return False
    for j in range(2,int(i/2)+1):
        if i%j==0:
            return False
    return True

n=int(input())
l=list(map(int,input().split()))
cnt=0
cnt1=0
for i in l:
    if p(i):
        cnt+=i
        cnt1+=1
p1=cnt/cnt1
print("%.2f"%p1)