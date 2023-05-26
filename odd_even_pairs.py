n=int(input())
lst=list(map(int,input().split()))
l1=[]
l2=[]
l3=[]
for i in range(n):
    if lst[i]%2==0:
        l2.append(lst[i])
    else:
        l1.append(lst[i])
if len(l1)<len(l2):
    for i in range(len(l1)):
        l3.append(l1[i])
        l3.append(l2[i])
    l=len(l1)
    for j in range(l,len(l2)):
        l3.append(l2[j])
else:
    for i in range(len(l2)):
        l3.append(l1[i])
        l3.append(l2[i])
    k=len(l2)
    for j in range(k,len(l1)):
        l3.append(l1[j])
if n%2!=0:
    l3.append(0)
print(*l3)