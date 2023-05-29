n=int(input())
l=list(map(int,input().split()))
l1=[]
for i in l:
    if i not in l1:
        l1.append(i)
if len(l1)<=3:
    print(l1[-1])
else:
    print(l1[2])