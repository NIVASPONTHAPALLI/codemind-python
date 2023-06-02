s=input().lower()
s1=list(s)
for i in s1:
    if s1.count(i)==1:
        print(i)
        break
else:
    print('-1')