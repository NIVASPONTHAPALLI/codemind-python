n=int(input())
lst=list(map(int,input().split()))
a,b=map(int,input().split())
l=[]
cnt=0
for i in lst:
    if i>=a and i<=b:
        l.append(i)
        cnt+=1
if cnt==0:
    print("-1")
else:
    print(max(l))