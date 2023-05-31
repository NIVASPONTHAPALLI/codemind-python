a,b=map(int,input().split())
l=[]
if a>b:
    for i in range(1,a):
        if a%i==0 and b%i==0:
            l.append(i)
else:
    for j in range(1,b):
        if a%j==0 and b%j==0:
            l.append(j)
print(max(l))