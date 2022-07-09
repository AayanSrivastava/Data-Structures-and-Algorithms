def subset(s,s1):
    a=[]
    if len(s)==0:
        a.append(s1)
        return
    
    op1=s1
    op2=s1
    op2.append(s[0])
    s.pop()
    subset(s,op1)
    subset(s,op2)
    return

s="abc"
s=list(s)
s1=[]
print(subset(s,s1))