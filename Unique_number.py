n1=int(input())
n1=str(n1)
n=list(n1)
l=[]
for i in n:
    if i not in l:
        l.append(i)
if len(l)==len(n):
    print("Unique Number")
else:
    print("Not Unique Number")