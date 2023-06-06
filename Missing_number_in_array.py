for i in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    cnt=0
    for i in range(1,n+1):
        cnt+=i
    l1=sum(l)
    print(cnt-l1)