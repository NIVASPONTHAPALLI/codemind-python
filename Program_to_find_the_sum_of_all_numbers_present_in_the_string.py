n=input()
n=list(n)
s='123456789'
l=''
for i in n:
    if i in s:
        l+=i
n1=int(l)
n2=list(map(int,str(n1)))
cnt=0
for i in n2:
    cnt+=i
print(cnt)

