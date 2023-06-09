n=int(input())
l=list(map(int,input().split()))
n1=int(input())
l1=list(map(int,input().split()))
l2=[]
for i in l:
    if i in l1:
        l2.append(i)
if l==l2:
    print(True)
else:
    print(False)