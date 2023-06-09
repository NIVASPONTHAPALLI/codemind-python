for i in range(int(input())):
    n=int(input())
    l2=[]
    l=list(map(int,input().split()))
    p=len(l)//2
    p1=len(l)-1
    for i in range(len(l)):
        if i<p:
            j=p1-i
            l2.append(l[j])
            l2.append(l[i])
    if n%2!=0:
        f=n//2
        l2.append(l[f])
    print(*l2)