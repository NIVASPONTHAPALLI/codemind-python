from collections import Counter
n=int(input())
arr=list(map(int,input().split()))
l=Counter(arr)
l1=[]
for i in l.keys():
    if i==l[i]:
        l1.append(i)
if len(l1)==0:
    print("-1")
else:
    print(*l1)