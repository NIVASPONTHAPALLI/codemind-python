a,b=map(int,input().split())
l=list(map(int,input().split()))
cnt=0
for i in l:
    if i%b!=0:
        cnt+=1
print(cnt)