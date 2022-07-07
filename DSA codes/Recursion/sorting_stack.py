def sort(stack):
    if(len(stack)==1):
        return
    
    t = stack[-1]
    stack.pop()
    sort(stack)
    insert(stack,t)
    return stack

def insert(stack,t):
    if (len(stack)==0 or stack[-1]<=t):
        stack.append(t)
        return
    
    val=stack[-1]
    stack.pop()
    insert(stack,t)
    stack.append(val)
    return

arr=[3,5,2,7,1,6]
print(sort(arr))