r,c=map(int,input().split())
mat=[list(map(int,input().split())) for i in range(r)]
cnt=0
for i in range(r):
    for j in range(c):
        cnt+=mat[i][j]
print(cnt)