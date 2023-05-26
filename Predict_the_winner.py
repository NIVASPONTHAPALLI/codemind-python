n=int(input())
l=list(map(int,input().split()))
cnt=0
lst=[]
l2=[]
for i in range(n-1):
    if l[i] not in l2:
        lst.append(l[i])
        l2.append(l[i+1])
p=abs(sum(lst)-sum(l2))
if p%4!=0:
    print("Y")
else:
    print("X")