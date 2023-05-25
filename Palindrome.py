n=int(input())
cnt=n
temp=0
while n:
    r=n%10
    temp=(temp*10)+r
    n=n//10
if temp==cnt:
    print(True)
else:
    print(False)