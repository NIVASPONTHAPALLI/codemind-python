for i in range(int(input())):
    m,n=map(int,input().split())
    ar=list(map(int,input().split()))
    ar1=list(map(int,input().split()))
    l=[]
    l=ar+ar1
    l.sort()
    print(*l)