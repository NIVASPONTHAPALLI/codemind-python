n=input()
p=list(n)
c='QWERTYUIOPLKJHGFDSAZXCVBNM'
cnt=0
for i in p:
    if i in c:
        cnt+=1
print(cnt)