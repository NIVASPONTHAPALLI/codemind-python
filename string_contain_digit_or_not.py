s=list(input())
sq='1234567890'
cn=0
for i in s:
    if i in sq:
        cn+=1
if cn>0:
    print("Contains {} digit".format(cn))
else:
    print("Doesn't contain digit")