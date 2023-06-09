n=int(input())
l=[]
for i in range(n):
    p=int(input())
    l.append(p)
k=int(input())
cnt=0
for i in l:
    if i<=k:
        cnt+=1
    else:
        e=i-k
        po=e*2
        cnt+=2
print(cnt)