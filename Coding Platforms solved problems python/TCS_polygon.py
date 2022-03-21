n=int(input())
l=[]
m=[]
for i in range(n):
    a,b=map(int,input().split())
    l.append(a)
    m.append(b)

def poly(a,b,n):
    area=0.0
    j=n-1
    for i in range(n):
        area+=(a[j]+a[i])*(b[j]-b[i])
        j=i
    return int(abs(area/2.0))

print(poly(l,m,n))