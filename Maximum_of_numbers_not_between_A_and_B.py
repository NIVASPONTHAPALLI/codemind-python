n=int(input())
l1=list(map(int,input().split()))
a,b=map(int,input().split())
l2=[]
for i in range(len(l1)):
    if a>l1[i] or b<l1[i]:
        l2.append(l1[i])
if len(l2)==0:
    print("-1")
else:
    print(max(l2))
