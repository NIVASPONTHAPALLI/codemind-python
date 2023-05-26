n=int(input())
lst=list(map(int,input().split()))
l=[]
cnt=0
for i in range(n):
    if lst[i] not  in l:
        l.append(lst[i])
for j in range(len(l)):
    if l[j]%2==0:
        cnt+=l[j]
print(cnt)