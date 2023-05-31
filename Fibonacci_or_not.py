n=int(input())
n1=0
n2=1
cnt=2
l=[]
if n<0:
    print(False)
elif n==1:
    print(True)
else:
    while cnt<n:
        n3=n1+n2
        l.append(n3)
        cnt+=1
        n1=n2
        n2=n3
for i in l:
    if i==n:
        print(True)
        break
else:
    print(False)