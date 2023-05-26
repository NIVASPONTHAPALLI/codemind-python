n=int(input())
lst=list(map(int,input().split()))
p=int(input())
l=[]
for i in range(n):
    if i<p:
        l.append(lst[i])
print(sum(l))