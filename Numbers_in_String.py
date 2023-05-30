n=input()
n=list(n)
s='123456789'
cnt=0
for i in n:
    if i in s:
        cnt+=int(i)
print(cnt)