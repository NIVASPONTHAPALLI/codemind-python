n=int(input())
arr=list(map(int,input().split()))
cnt=0
l=[]
for i in range(0,n):
    if arr[i] not in l:
        l.append(arr[i])
   
for j in range(len(l)):
    if l[j]%2==0:
        cnt+=1
print(cnt)
