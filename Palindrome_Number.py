for i in range(int(input())):
    n=int(input())
    temp=n
    n1=0
    while n!=0:
        p=n%10
        n1=(n1*10)+p
        n//=10
    if temp==n1:
        print(True)
    else:
        print(False)