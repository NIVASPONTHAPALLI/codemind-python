n=int(input())
l=list(map(int,input().split()))
k=int(input())
cnt=0
for i in range(len(l)):
    if l[i]==k:
        cnt=i
        print(cnt)
        break
if cnt==0:
    print('-1')