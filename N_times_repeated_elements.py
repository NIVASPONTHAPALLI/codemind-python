from collections import Counter
n=int(input())
arr=map(int,input().split())
p=int(input())
l=Counter(arr)
l1=[]
for i in l.keys():
    if l[i]==p:
        l1.append(i)
if len(l1)==0:
    print("-1")
else:
    print(*l1)