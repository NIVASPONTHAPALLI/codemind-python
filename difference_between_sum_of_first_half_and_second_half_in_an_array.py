n=int(input())
lst=list(map(int,input().split()))
l1=[]
p=n//2
for i in range(p):
    l1.append(lst[i])
l2=sum(l1)
l=[]
for i in range(p,n):
    l.append(lst[i])
l3=sum(l)
print(abs(l2-l3))