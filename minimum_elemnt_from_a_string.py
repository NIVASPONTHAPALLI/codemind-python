n=list(input())
n.sort()
s='abcdefghijklmnopqrstvuwxyz'
s1='ABCDEFGHIJKLMNOPQRSTVUXWYZ'
for i in range(len(s)):
    if s[i] in n:
        print(s[i])
        break
    elif s1[i] in n:
        print(s1[i])
        break