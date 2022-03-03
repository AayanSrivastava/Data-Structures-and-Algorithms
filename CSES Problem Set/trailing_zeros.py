n=int(input())
f=1
s=0
c=0
for i in range(1,n+1):
    f*=i
while(s==0):
    s=f%10
    f=f//10
    c+=1
print(c-1)