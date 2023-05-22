n=int(input())
arr=list(map(int,input().split()))
l=[]
for j in arr:
    if j%2==1:
        l.append(j)
for i in arr:
    if i%2==0:
        l.append(i)
print(*l)