n=int(input())
l=list(map(int,input().split()))
cnt=0
for i in range(1,len(l)-1):
    if l[i-1]+l[i]==l[i+1]:
        cnt+=1
    else:
        cnt=0
        break
if cnt==0:
    print("no")
else:
    print("yes")