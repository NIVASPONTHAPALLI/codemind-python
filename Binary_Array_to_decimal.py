n=int(input())
l=list(map(int,input().split()))
s=0
le=len(l)
for i in range(le):
    le=le-1
    s=s+(l[i]*2**le)
print(s)
    