n=int(input())
temp=n
if n<0:
    n=n*-1
n1=0
while n!=0:
    p=n%10
    n1=(n1*10)+p
    n=n//10
if temp>0:
    print(n1)
else:
    print(-n1)