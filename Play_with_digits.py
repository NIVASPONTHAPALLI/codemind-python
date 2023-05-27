n=int(input())
l=list(map(int,input().split()))
s=0
for i in l:
    while i!=0:
        p=i%10
        s+=p
        i=i//10
print(s)