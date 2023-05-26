n=int(input())
l=list(map(int,input().split()))
cnt=0
for i in range(n-1):
    if l[i]<l[i+1]:
        cnt+=1
        break
if cnt==1:
    print("no")
else:
    print("yes")