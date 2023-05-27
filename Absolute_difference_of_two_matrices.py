n=int(input())
mat1=[list(map(int,input().split())) for i in range(n)]
mat2=[list(map(int,input().split())) for i in range(n)]
l=[]
for i in range(n):
    a=[]
    for j in range(n):
        a.append(abs(mat1[i][j]-mat2[i][j]))
    l.append(a)
for i in l:
    print(*i)