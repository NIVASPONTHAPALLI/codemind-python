n=int(input())
l=list(map(int,input().split()))
s=set(l)
p=list(s)
p.sort()

if l==p:
    print("yes")
else:
    print("no")