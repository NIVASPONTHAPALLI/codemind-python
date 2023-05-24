r,c=map(int,input().split())
mat=[list(map(int,input().split())) for i in range(r)]
cnt=0

for i in range(0,r):
    for j in range(0,r):
        if i==j:
            cnt+=mat[i][j]
        elif ((i+j)==(r-1)):
            cnt+=mat[i][j]
#for i in range(r):
   # for j in range(c):
    #    if (i==0 and j==cnt1) or (i==cnt1 and j==0):
     #       cnt+=mat[i][j]
print(cnt)