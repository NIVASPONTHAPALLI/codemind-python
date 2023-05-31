n=int(input())
l=list(map(int,input().split()))
l1=[]
for i  in l:
    l1.append(len(str(i)))
cnt=0
l2=min(l1)
for i in l:
    if len(str(i))==l2:
        cnt+=1
print(cnt)