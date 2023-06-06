def palin(n):
    n=str(n)
    n1=n[::-1]
    if n==n1:
        return True
    return False
 #   while n!=0:
  #      p=n%10
   #     c=(c+10)*p
    #    n=n//10
    #if temp==c:
     #   return True
    #else:
     #   return False
n=int(input())
p=int(input())
for i in range(n,p+1):
    if palin(i)==True:
        print(i,end=" ")