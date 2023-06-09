n=int(input())
l=list(map(int,input().split()))
lw=[]
n=len(l)//2
for i in range(n,len(l)):
    lw.append(l[i])
lp=lw[::-1]
for j in range(0,n):
    lp.append(l[j])
print(*lp)