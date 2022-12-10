# s='yyyaaaann'
# h={}
# for i in s:
#     if i in h:
#         h[i]+=1
#     else:
#         h[i]=1
# print(sorted(h.items(),key=lambda kv:(kv[1],kv[0]),reverse=True))

n=2*5
x=2
z=2
for i in range(1,n):
    for j in range(1,i):
        print(" ",end="")
    if i<=5:
        print(i,end="")
    else:
        print(i-x,end="")
        x+=2

    a=3
    if i<=5:
        for l in range(0,n-i*2):
            print(" ",end="")
        print(i)
    else:
        for k in range(0,a):
            print(" ",end="")
        a-=1
        print(i-z)
        z+=2