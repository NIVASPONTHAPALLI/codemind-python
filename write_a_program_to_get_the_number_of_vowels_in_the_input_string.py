n=input()
n=list(n)
s=['a','e','i','o','u']
s1=['A','E','I','O','U']
cnt=0
for i in n:
    if i in s:
        cnt+=1
    elif i in s1:
        cnt+=1
print(cnt)
