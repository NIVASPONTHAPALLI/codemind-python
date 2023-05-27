a,b=map(int,input().split())
l1=list(map(int,input().split()))
l2=list(map(int,input().split()))
l3=set(l1)
l4=set(l2)
l5=len(l3)
l6=len(l4)
l7=l5+l6
cnt=0
for i in l3:
    if i in l4:
        cnt+=1
for i in l4:
    if i in l3:
        cnt+=1
if cnt==0:
    print(l7)
else:
    print(l7-cnt)
    