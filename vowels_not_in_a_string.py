n=input()
n=list(n)
l=['a','e','i','o','u']
p=len(l)
cnt=0
for i in n:
    if i in l:
        l.remove(i)
        cnt+=1
if p==cnt:
    print(0)
else:
    print(*l)