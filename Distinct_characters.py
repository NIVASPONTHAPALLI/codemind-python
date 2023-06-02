n=input().lower()
s=set(n)
l=[]
for i in s:
    if i!=" ":
        l.append(i)
l1=sorted(l)
for i in l1:
    print(i,end="")