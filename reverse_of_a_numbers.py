n=int(input())
temp=0
while n!=0:
    p=n%10
    temp=(temp*10)+p
    n=n//10
print(temp)