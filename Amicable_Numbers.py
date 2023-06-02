n=int(input())
p=int(input())
cnt=0
cnt1=0
for i in range(1,n):
    if n%i==0:
        cnt+=i
for j in range(1,p):
    if p%j==0:
        cnt1+=j
if n==cnt1 and p==cnt:
    print('Amicable')
else:
    print('Not Amicable')