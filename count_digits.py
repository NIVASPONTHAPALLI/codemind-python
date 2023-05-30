n=int(input())
l=list(map(int,input().split()))
l1=[]
for i in l:
    i=abs(i)
    v=str(i)
    l1.append(len(v))
#    cnt=0
 #   cnt1=0
  #  while i!=0:
   #     p=i%10
    #    cnt=(cnt*10)+p
     #   cnt1+=1
      #  i=i//10
   
print(*l1)
        