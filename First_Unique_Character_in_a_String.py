n=input().lower()
x=[]
for i in n:
    if n.count(i)==1:
        print(n.index(i))
        x.append(i)
        break
if len(x)==0:
    print("-1")