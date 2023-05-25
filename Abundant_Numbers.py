n=int(input())
cnt=0
for i in range(1,n):
    if n%i==0:
        cnt+=i
if cnt>n:
    print("True")
else:
    print("False")