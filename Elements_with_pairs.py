n=int(input())
li=list(map(int,input().split()))
l=[]
for i in range(n):
    l.append(li[i])
    if n%2!=0:
        if i==' ':
            l.append('0')
        elif i==n-1:
            l.append('0')
print(*l)

