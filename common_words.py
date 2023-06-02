s1=input().lower().split()
s2=input().lower().split()
l=[]
for i in s2:
    if i in s1:
        l.append(i)
print(*l)