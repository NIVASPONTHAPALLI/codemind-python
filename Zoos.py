n=list(input())
l=[]
lp=[]
for i in n:
    if i=='z':
        l.append(i)
    else:
        lp.append(i)
p=len(l)
p1=len(lp)/2
if p==p1:
    print('Yes')
else:
    print("No")