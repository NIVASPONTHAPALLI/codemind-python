n=input()
n=list(n)
s=['a','e','i','o','u']
s1=['A','E','I','O','U']
for i in n:
    if i in s:
        s.remove(i)
    elif i in s1:
        s1.remove(i)
if len(s)==0 or len(s1)==0:
    print(True)
else:
    print(False)