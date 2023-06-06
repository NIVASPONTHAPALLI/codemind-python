n=int(input())
l=list(map(int,input().split()))
max=0
s=0
for i in range(len(l)):
    p=l.count(l[i])
    if p>max:
        max=p
        s=l[i]
print(s)