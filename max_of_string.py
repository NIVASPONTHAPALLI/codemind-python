n=input()
p=list(n)
l=[]
for i in p:
    l.append(ord(i))
w=max(l)
print(chr(w))