n=int(input())
x=list(map(int,input().split()))
lis=[]
c=0
for i in x:
    if x.count(i)==i and i not in lis:
        lis.append(i)
        c+=1
if c==0:
    print(-1)
else:
    avg=(sum(lis)/len(lis))
    print("%.2f"%avg)