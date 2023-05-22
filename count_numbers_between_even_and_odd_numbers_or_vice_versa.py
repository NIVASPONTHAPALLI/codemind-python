n=int(input())
arr=list(map(int,input().split()))
cnt=0
for i in range(1,len(arr)-1):
    if (arr[i-1]%2==0 and arr[i+1]%2==1):
        cnt=cnt+1
    elif (arr[i-1]%2==1 and arr[i+1]%2==0):
        cnt=cnt+1
print(cnt)