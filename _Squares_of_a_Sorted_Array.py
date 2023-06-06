n=int(input())
l=list(map(int,input().split()))
l1=[]
for i in range(len(l)):
    n1=int(l[i])
    n2=n1*n1
    l1.append(n2)
l1.sort()
print(*l1)