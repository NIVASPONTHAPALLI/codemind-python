s=input().split()
l3=[]
l4=[]
for i in s:
    l1=min(i)
    l2=max(i)
    l3.append(ord(l1))
    l4.append(ord(l2))
print(sum(l4)-sum(l3))