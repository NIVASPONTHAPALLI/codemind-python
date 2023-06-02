n=input().lower()
s=set(n)
l=[]
for i in s:
    if i!=" ":
        l.append(i)
print(len(l))