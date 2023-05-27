n=input()
s=n.split()[::1]
p=len(s)
l=[]
for i in range(p):
    if i%2==0:
        k=s[i]
        o=k[::-1]
        l.append(o)
    else:
        l.append(s[i])
print(*l)
