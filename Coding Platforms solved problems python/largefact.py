n=int(input())
f=1
for i in range(1,n+1):
    f=f*i
f=str(f)
print(f)
for i in range(len(f)):
    if f[i]!='0':
        c=i
print("c=",c)
t=f.count('0',c-1,len(f))
print(t)