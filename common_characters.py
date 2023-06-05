s1=list(input().lower())
s2=list(input().lower())
l=[]
if s1<s2:
    s1,s2=s2,s1
for i in s1:
    if i in s2 and i not in l and i!=" ":
        l.append(i)
l.sort()
if len(l)==0:
    print('-1')
else:
    for i in l:
        print(i,end="")