# def mins(stack):
#     st=[]
#     st.append(stack[-1])
#     for i in stack:
#         if st[-1]>=i:
#             st.append(i)
#     return st[-1]

# s=[5,4,7,2,5,9,6]
# print(mins(s))

# Recursive

# def getmin(stack):
#     if len(stack)==1:
#         return
#     v=stack.pop()
#     rmin(stack)

# def rmin(stack):
#     st=[]
#     st.append(stack[-1])
#     return st

# stack=[5,4,7,3,9,1,2]
# print(rmin(stack))