r,c=map(int,input().split())
mat=[list(map(int,input().split())) for i in range(r)]
l1=[]
for i in range(c):
    cnt=0
    for j in range(r):
        cnt=cnt+mat[j][i]
    l1.append(cnt)
print(*l1)