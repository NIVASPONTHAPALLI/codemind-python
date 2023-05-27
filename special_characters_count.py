n=input()
p=list(n)
c='qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'
cnt=0
for i in p:
    i=i.strip()
    if i not in c:
        cnt+=1
print(cnt)