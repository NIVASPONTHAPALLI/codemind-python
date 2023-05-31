n=int(input())
l=list(map(str,input().split()))
l1=[]
for i in l:
  l1.append(len(i))
cnt=0
for i in l1:
    if i%2==0:
        cnt+=1
print(cnt)