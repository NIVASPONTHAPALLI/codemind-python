n=int(input())
lst=list(map(int,input().split()))
l=[]
for i in range(n):
    if lst[i] not in l:
        l.append(lst[i])
    else:
        l.remove(lst[i])
if len(l)==0:
    print("-1")
else:
    print(*l)