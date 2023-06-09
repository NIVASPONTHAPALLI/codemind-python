def square(n):
    p=n**0.5
    if n%p==0:
        return True
    else:
        return False
n=int(input())
l=list(map(int,input().split()))
cnt=0
for i in l:
    if square(i):
        cnt+=i
print(cnt)