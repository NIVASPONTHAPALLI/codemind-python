n=int(input())
l=list(map(int,input().split()))
cnt=0
for i in range(1,n-2):
    if l[i-1]<l[i] and l[i]>l[i+1]:
        continue
    elif l[i-1]>l[i] and l[i]<l[i+1]:
        continue
    else:
        cnt=1
        break
if cnt==1:                                                
    print("no")
else:
    print("yes")