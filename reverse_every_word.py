n=input()
s=n.split()[::1]
l=[]
for i in s:
    l.append(i[::-1])
print(*l)
