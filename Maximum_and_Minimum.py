n=int(input())
l=list(map(int,input().split()))
cnt,cn=[],0
for i in l:
    if l.count(i)==i and i not in cnt:
        cnt.append(i)
        cn+=1
if cn==0:
    print('-1')
else:
    a=min(cnt)
    b=max(cnt)
    print(a,b,end=" ")