# iterative

# def delete(stack):
#     c=0
#     st=[]
#     for i in stack:
#         c+=1
#         if c!=(len(stack)//2)+1:
#             st.append(i)
#     return st

# s=[1,2,3,4,5]
# print(delete(s))

# recursive
def delete(stack,k):
    if k==0:
        stack.pop()
        return
    v=stack.pop()
    delete(stack,k-1)
    stack.append(v)
    return stack

s=[1,2,3,4,5,6,7]
print(delete(s,(len(s)//2)))
