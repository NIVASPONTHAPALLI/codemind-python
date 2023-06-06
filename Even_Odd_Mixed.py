n=int(input())
n1=len(str(n))
cnt,cnt1=0,0
while n!=0:
    p=n%10
    n=n//10
    if p%2==0:
        cnt+=1
    else:
        cnt1+=1
if cnt==n1:
    print('Even')
elif cnt1==n1:
    print('Odd')
else:
    print('Mixed')