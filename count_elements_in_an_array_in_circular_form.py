n=int(input())
a=list(map(int,input().split()))
cnt=0
for i in range(1,len(a)-1):
    if (a[i-1]%2==0 and a[i+1]%2==1):
        cnt+=1
    elif (a[i-1]%2==1 and a[i+1]%2==0):
        cnt+=1
if (a[n-1]%2==0 and a[1]%2==1):
    cnt+=1
elif (a[n-1]%2==1 and a[1]%2==0):
    cnt+=1
if (a[n-2]%2==0 and a[0]%2==1):
    cnt+=1
elif (a[n-2]%2==1 and a[0]%2==0):
    cnt+=1

print(cnt)
    