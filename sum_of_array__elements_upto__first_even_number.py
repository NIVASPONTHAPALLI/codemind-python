n=int(input())
lst=list(map(int,input().split()))
l=[]
for i in range(n):
    if lst[i]%2==0:
        break
    else:
        l.append(lst[i])
print(sum(l))