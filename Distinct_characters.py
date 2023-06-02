n=list(input().lower())
l=[]
for i in n:
    if n.count(i)==1 and i!=" ":
        l.append(i)
l1=sorted(l)
for i in l1:
    print(i,end="")