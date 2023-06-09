a,b,c=map(int,input().split())
d,e,f=map(int,input().split())
cnt=0
cnt1=0
if a>d:
    cnt+=1
if a<d:
    cnt1+=1
if b>e:
    cnt+=1
if b<e:
    cnt1+=1
if c>f:
    cnt+=1
if c<f:
    cnt1+=1
print(cnt,cnt1)