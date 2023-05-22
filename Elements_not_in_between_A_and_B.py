n=int(input())
arr=list(map(int,input().split()))
a,b=map(int,input().split())
l=[]

for i in range(0,len(arr)):
    if arr[i]<a or arr[i]>b:
        l.append(arr[i])
if len(l)==0:
    print("-1")
else:
    print(*l)
    