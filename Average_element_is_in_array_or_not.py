n=int(input())
l=list(map(int,input().split()))
p=sum(l)
i=p//n
if i<n:
    print('True')
else:
    print('False')