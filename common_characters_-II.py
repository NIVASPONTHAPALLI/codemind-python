s1=list(input().lower())
s2=list(input().lower())
l=[]
c=0
if len(s1)<len(s2):
    s1,s2=s2,s1
for i in s1:
    if i in s2 and i not in l and i!=" ":
        l.append(i)
        c+=1

print(c)