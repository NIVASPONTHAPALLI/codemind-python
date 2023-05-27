def vowel(i):
    if i==s:
        return True
    return False
n=input()
n=list(n)
s=input()
for i in n:
    if vowel(i):
        print(True)
        print(n.index(s))
        break
else:
    print(False)