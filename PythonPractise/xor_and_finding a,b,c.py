try:
    t=int(input())
    while t:
        l=[]
        x,y=map(int,input().split(" "))
        z=x^y
        if (x%2 and y%2):
            b=2
            c=y^b
            a=x^b
        if (y%2 and z%2):
            b=2
            c=z^b
            a=y^b
        if (z%2 and x%2):
            b=2
            c=x^b
            a=z^b
        l.append(a)
        l.append(b)
        l.append(c)
        l.sort()
        for i in l:
            print(i,end=" ")
        t-=1
except:
    pass