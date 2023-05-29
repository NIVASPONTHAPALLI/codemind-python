def small(n):
    l=[]
    for i in n:
        l.append(i)
    l1=max(l)
    l2=min(l)
    return l2,l1

n=input().split()
for i in n:
    p=small(i)
    print(*p,end=" ")