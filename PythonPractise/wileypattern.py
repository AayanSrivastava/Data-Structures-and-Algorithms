n=2*5
x=2
z=2
a=4
for i in range(1,n):
    if i<=5:
        for j in range(1,i):
            print(" ",end="")
        print(i,end="")
    else:
        for p in range(1,a):
            print(" ",end="")
        a-=1
        print(i-x,end="")
        x+=2

    o=3
    if i<=5:
        for l in range(0,n-i*2):
            print(" ",end="")
        if i==5:
            print("")
        else:
            print(i)
    else:
        for k in range(1,i-(i-z)):
            print(" ",end="")
        o+=1
        print(i-z)
        z+=2