def maxcones(l,n):
    result=0
    cnt=0
    for i in range (n):
        if l[i]==0:
            cnt=0
        else:
            cnt+=1
            result=max(result,cnt)
    return result

n=int(input())
l=list(map(int,input().split()))
n=len(l)
print(maxcones(l,n))
