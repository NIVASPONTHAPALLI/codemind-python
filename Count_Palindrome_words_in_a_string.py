def fun(i):
    p=i[::-1]
    if p==i:
        return True
    else:
        return False


s=input()
k=s.lower()
cnt=0
l=list(k.split())
for i in l:
    if fun(i)==True:
        cnt+=1
print(cnt)