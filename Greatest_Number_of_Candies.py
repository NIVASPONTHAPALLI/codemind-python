n=int(input())
l=list(map(int,input().split()))
k=int(input())
l1=max(l)
l3=[]
for i in l:
    temp=k
    l2=i+temp-l1
    if l2>=0:
        l3.append(True)
    else:
        l3.append(False)
print(*l3)