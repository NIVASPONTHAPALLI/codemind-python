n=(int(input()))
t=n
cnt=0
c=0
l=0
i=1
while n!=0:
    p=n%10
    cnt=cnt*10+p
    c+=1
    n=n//10
for i in range(1,c+1,1):
    m=cnt%10
    l=l+m**i
    cnt=cnt//10
if t==l:
    print(True)
else:
    print(False)