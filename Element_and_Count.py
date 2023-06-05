n=int(input())
l=list(map(int,input().split()))
cnt=[]
cnt1=[]
for i in l:
    if i not in cnt:
        cnt.append(i)
        cnt1.append(l.count(i))
cn=[]
for i in range(len(cnt)):
    print(cnt[i],cnt1[i],end=" ")