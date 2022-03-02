n=int(input())
l=list(map(int,input().split()))
c=0
for i in range(n-1):
    f=0
    for j in range(n-1-i):
        if l[j]>l[j+1]:
            c+=1
            t=l[j]
            l[j]=l[j+1]
            l[j+1]=t
            f=1
    if f==0:
        break
print(c)
