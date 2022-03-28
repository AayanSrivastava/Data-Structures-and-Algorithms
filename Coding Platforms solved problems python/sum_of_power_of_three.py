n=int(input())
a=[]
s=0
t=n
while(n>0):
    a.append(n%3)
    n//=3
a.reverse()
for i in range(len(a)):
    if a[i]!=2:
        s+=a[i]*pow(3,len(a)-1-i)
print(s==t)

# Second Method

# while(n>0):
#     if n%3==2:
#         return False
#     n//=3
# return True