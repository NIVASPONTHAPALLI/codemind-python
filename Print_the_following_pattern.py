n=int(input())
i=0
for i in range(n):
    for j in range(i+1,n+1):
        print(j,end=" ")
    print()