n=int(input())
l=list(map(int,input().split()))
cnt=0
cnt1=0
for i in range(n):
    if i%2==0:
        cnt+=l[i]
      
    else:
        cnt1+=l[i]
p=abs(cnt-cnt1)
if p==0:
    print("YES")
else:
    print("NO")