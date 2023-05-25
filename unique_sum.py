n=int(input())
lst=list(map(int,input().split()))
l=[]
for i in range(n):
    if lst[i] not in l:
        l.append(lst[i])
print(sum(l))