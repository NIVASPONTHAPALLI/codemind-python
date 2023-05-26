n=int(input())
l=list(map(int,input().split()))
l1=0
for i in range(n):
    if l.count(l[i])==1:
        if l1<l[i]:
            l1=l[i]
if l1==0:
    print("-1")
else:
    print(l1)