def rev(stack,k):
    st=[]
    if k==0:
        return

    v=stack.pop()
    rev(stack,k-1)
    insert(stack,v)
    return stack

def insert(stack,t):
    if (len(stack) ==0):
        stack.append(t)
        return
    
    val=stack.pop()
    insert(stack,t)
    stack.append(val)
    return

s=[1,2,3,4,5]
print(rev(s,len(s)))