r,c=map(int,input().split())
mat=[list(map(int,input().split())) for i in range(r)]

cnt=0
for i in range(c):
    lst=[]
    for j in range(r):
        lst.append(mat[j][i])
    temp=sorted(lst)
    if lst==temp:
        cnt+=1
    elif temp==lst[::-1]:
        cnt+=1
print(cnt)