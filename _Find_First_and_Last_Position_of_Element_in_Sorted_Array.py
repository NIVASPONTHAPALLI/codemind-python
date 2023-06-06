n=int(input())
l=list(map(int,input().split()))
k=int(input())
l1=[]
for i in range(len(l)):
    if int(l[i])==k:
        l1.append(i)
if len(l1)==0:
    print('-1','-1')
else:
    print(l1[0],l1[-1],end=" ")