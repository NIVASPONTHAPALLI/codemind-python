s1=list(input().lower())
s2=list(input().lower())
l=[]
for i in s1:
    if i not in s2 and i not in l and i!=" ":
        l.append(i)
for j in s2:
    if j not in s1 and j not in l and j!=" ":
        l.append(j)

print(len(l)-1)