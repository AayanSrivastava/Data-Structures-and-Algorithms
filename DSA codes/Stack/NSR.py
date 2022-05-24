# class stack:
#     def __init__(self):
#         self.container=[]

#     def push(self,val):
#         self.container.append(val)

#     def pop(self):
#         return self.container.pop()

#     def top(self):
#         if self.container:
#             return self.container[-1]
#         else:
#             return None

#     def is_empty(self):
#         if self.container:
#             return len(self.container)==0
#         else:
#             return None
    
#     def size(self):
#         return len(self.container)
    
#     def display(self):
#         return self.container 

# s=[1,3,2,4]
# a=[]
# st=stack()
# for i in range(len(s)-1,-1,-1):  #next smaller to right
# # for i in range(len(s)):  #next smaller to left
#     if st.size()==0:
#         a.append(-1)
#     elif st.size()>0 and st.top()<s[i]:
#         a.append(st.top())
#     elif st.size()>0 and st.top()>=s[i]:
#         while st.size()>0 and st.top()>=s[i]:
#             st.pop()
#         if st.size()==0:
#             a.append(-1)
#         else:
#             a.append(st.top())
#     st.push(s[i])
# print(a[::-1])

#NEXT SMALLER TO RIGHT INDEX


class stack:
    def __init__(self):
        self.container=[]

    def push(self,val,x):
        self.container.append((val,x))

    def pop(self):
        return self.container.pop()

    def top(self):
        if self.container:
            return self.container[-1]
        else:
            return None

    def is_empty(self):
        if self.container:
            return len(self.container)==0
        else:
            return None
    
    def size(self):
        return len(self.container)
    
    def display(self):
        return self.container 

s=[2,1,5,6,2,3]
a=[]
st=stack()
for i in range(len(s)-1,-1,-1):  #next smaller to right
# for i in range(len(s)):   next smalller to left
    if st.size()==0:
        a.append(-1)
    elif st.size()>0 and st.top()[0]<s[i]:
        a.append(st.top()[1])
    elif st.size()>0 and st.top()[0]>=s[i]:
        while st.size()>0 and st.top()[0]>=s[i]:
            st.pop()
        if st.size()==0:
            a.append(-1)
        else:
            a.append(st.top()[1])
    st.push(s[i],i)
print(a[::-1])