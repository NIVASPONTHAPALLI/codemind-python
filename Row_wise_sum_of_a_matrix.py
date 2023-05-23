r,c=map(int,input().split())
mat=[list(map(int,input().split())) for i in range(r)]
l1=[]
for i in range(r):
    cnt=0
    for j in range(c):
        cnt=cnt+mat[i][j]
    l1.append(cnt)
print(*l1)