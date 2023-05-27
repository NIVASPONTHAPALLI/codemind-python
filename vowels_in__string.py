n=input()
n=list(n)
l=[]
l1=[]
s='aeiouAEIOU'
for i in n:
    if i in s:
  #i=="a" or i=="e" or i=="i" or i=="o" or i=="u" or i=="A" or i=="E" or i=="I" or i=="O" or i=="U":
        l.append(i)
for k in l:
    if k not in l1:
        l1.append(k)
print(*l1)