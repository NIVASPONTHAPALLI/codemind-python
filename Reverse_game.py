n=int(input())
l=list(map(int,input().split()))
cnt1=[]
for i in l:
    cnt=0
    while i!=0:
        p=i%10
        cnt=(cnt*10)+p
        i=i//10
    cnt1.append(cnt)
print(*cnt1)