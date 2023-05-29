n=int(input())
l=list(map(int,input().split()))
cnt=1
for i in l:
    cnt*=i
l2=[]
for j in range(n):
    l1=cnt//l[j]
    l2.append(l1)
print(*l2)
    