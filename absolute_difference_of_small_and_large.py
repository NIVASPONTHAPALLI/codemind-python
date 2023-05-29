def small(n):
    l=[]
    for i in n:
        l.append(ord(i))
    l1=max(l)
    l2=min(l)
    l3=abs(l1-l2)
    return l3

n=input().split()
for i in n:
    p=small(i)
    print(p,end=" ")