n=int(input())
temp=n
l=list(map(int,input().split()))
#if n%2!=0:
 #   p1=n//2+1
#else:
 #   p1=n//2
p1=n//2
for i in range(p1):
    n=n-1
    j=n
    print(l[i],l[j],end=" ")
if temp%2!=0:
    print(l[p1],'0',end=" ")