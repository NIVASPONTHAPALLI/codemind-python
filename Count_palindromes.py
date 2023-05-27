n=int(input())
l=list(map(int,input().split()))
cnt1=0
for i in l:
    l=i
    cnt=0
    while i!=0:
        p=i%10
        cnt=(cnt*10)+p
        i=i//10
    if l==cnt:
        cnt1+=1
print(cnt1)
