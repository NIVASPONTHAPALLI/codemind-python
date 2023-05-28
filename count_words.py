def count(n):
    n=list(n)
    s='aeiouAEIOU'
    for i in n:
        if n[0] in s:
            if n[-1] not in s:
                return True
    return False

n=input()
l=n.split()
cnt=0
for i in l:
    if count(i):
        cnt+=1
print(cnt)