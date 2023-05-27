def vowel(i):
    l1=0
    for j in i:
        if j in s:
            l1+=1
    return l1
n=input()
p=n.split()
s='aeiouAEIOU'
l=[]
for i in p:
    p=vowel(i)
    l.append(p)
print(*l)