a=[2,1,4,3]
stack=[]
for i in a:
    if stack and stack[-1]<=i:
        stack.pop()
        stack.append(i)
    else:
        stack.append(i)
print(stack)