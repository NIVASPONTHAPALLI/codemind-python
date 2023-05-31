n=int(input())
l=list(map(int,input().split()))
l1=[]
for i  in l:
    l1.append(len(str(i)))
l3=[]
l2=max(l1)
for i in l:
    if len(str(i))==l2:
        l3.append(i)
print(*l3)