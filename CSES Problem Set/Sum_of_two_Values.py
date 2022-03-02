n,x=map(int,input().split())
a=[]
t=0
y=0
num=list(map(int,input().split()))
for i in range(n):
    l=i
    k=n-1
    while(l<k):
        tot=num[l]+num[k]
        if tot==x:
            t=l+1
            y=k+1
            l+=1
            k-=1
        elif tot<x:
            l+=1
        else:
            k-=1
if t==0 and y==0:
    print("IMPOSSIBLE")
else:
    print(t,y)