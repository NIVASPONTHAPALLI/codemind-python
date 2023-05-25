import math
n=int(input())
p=math.sqrt(n)
if (int)(p+0.5)**2==n:
    print(True)
else:
    print(False)