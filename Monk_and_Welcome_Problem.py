n=int(input())
l1=list(map(int,input().split()))
l2=list(map(int,input().split()))
l=[]
for i in range(n):
    cnt=0
    for j in range(n):
        if i==j:
            cnt+=l1[i]+l2[j]
    l.append(cnt)
print(*l)