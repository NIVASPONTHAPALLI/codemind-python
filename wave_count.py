n=int(input())
l=list(map(int,input().split()))
cnt=0
for i in range(1,n-1,2):
    if l[i-1]<l[i] and l[i]>l[i-1] :
        cnt+=1
    else:
        print("-1")
        cnt=0
        break
if cnt!=0:
    print(cnt)