from collections import Counter
n=int(input())
ar=list(map(int,input().split()))
arr1=Counter(ar)
cnt=0
for i in arr1.keys():
    if i==arr1[i]:
        cnt+=1
print(cnt)