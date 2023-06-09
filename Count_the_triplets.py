for i in range(int(input())):
    n=int(input())
    lst=list(map(int,input().split()))
    cnt=0
    for i in range(len(lst)):
        k=lst[i]
        for j in range(i+1,len(lst)):
            d=k+lst[j]
            if d in lst:
                cnt+=1
    if cnt==0:
        print('-1')
    else:
        print(cnt)
            