def fun(n):
    x=list(n)
    l=[]
    for i in range(0,len(n)):
        if x[i] not in 'aeiouAEIOU':
            l.append(x[i])
            x[i]='*'
    p=sorted(l)
    j=0
    for i in range(len(x)):
        if x[i]=='*':
            x[i]=p[j]
            j+=1
    return ''.join(x)

n=input().split()
for i in n:
    print(fun(i),end=" ")
