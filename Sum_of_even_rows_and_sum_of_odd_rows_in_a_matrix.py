r,c=map(int,input().split())
mat=[list(map(int,input().split())) for i in range(r)]
cnt=0
cnt1=0
for i in range(r):
    for j in range(c):
        if i%2==0:
            cnt+=mat[i][j]
        else:
            cnt1+=mat[i][j]
print(cnt,cnt1)