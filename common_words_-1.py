n=input()
p=input()
n=n.lower()
p=p.lower()
p1=n.split()
p2=p.split()
cnt=0
for i in p1:
    if i in p2:
        cnt+=1
print(cnt)