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

width=[]
area=[]
s=[1,2,3,4,5]
a=[]
st=stack()
for i in range(len(s)):   #next smaller to left
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


b=[]
st1 = stack()
for i in range(len(s)-1,-1,-1):  #next smaller to right
# for i in range(len(s)):   next smalller to left
    if st1.size()==0:
        b.append(len(s))
    elif st1.size()>0 and st1.top()[0]<s[i]:
        b.append(st1.top()[1])
    elif st1.size()>0 and st1.top()[0]>=s[i]:
        while st1.size()>0 and st1.top()[0]>=s[i]:
            st1.pop()
        if st1.size()==0:
            b.append(len(s))
        else:
            b.append(st1.top()[1])
    st1.push(s[i],i)
b=b[::-1]

for i in range(len(s)):
    width.append(a[i]-b[i]-1)

for i in range(len(s)):
    area.append(width[i]*s[i])

print(a)
print(b)
print(width)
print(area)
print(max(area))


# FUNCTION FOR MAXIMUM AREA

# def getMaxArea(self,histogram):
#         heights=histogram
#         a=stack()
#         b=stack()
#         c=stack()
#         st = stack()
#         st1 = stack()
#         width=stack()
#         area=stack()
        
#         #next smaller to left
        
#         for i in range(len(heights)):
#             if st.size()==0:
#                 a.push1(-1)
#             elif st.size()>0 and st.top()[0]<heights[i]:
#                 a.push1(st.top()[1])
#             elif st.size()>0 and st.top()[0]>=heights[i]:
#                 while st.size()>0 and st.top()[0]>=heights[i]:
#                     st.pop()
#                 if st.size()==0:
#                     a.push1(-1)
#                 else:
#                     a.push1(st.top()[1])
#             st.push(heights[i],i)
            
#         #next smaller to right
        
#         for i in range(len(heights)-1,-1,-1):
#             if st1.size()==0:
#                 b.push1(len(heights))
#             elif st1.size()>0 and st1.top()[0]<heights[i]:
#                 b.push1(st1.top()[1])
#             elif st1.size()>0 and st1.top()[0]>=heights[i]:
#                 while st1.size()>0 and st1.top()[0]>=heights[i]:
#                     st1.pop()
#                 if st1.size()==0:
#                     b.push1(len(heights))
#                 else:
#                     b.push1(st1.top()[1])
#             st1.push(heights[i],i)            
        
        
#         for i in range(len(heights)):
#             c.push1(b.pop())
        
#         a=a.display()
#         c=c.display()
        
        
#         for i in range(len(heights)):
#             width.push1(c[i]-a[i]-1)
            
#         width=width.display()
        
#         for i in range(len(heights)):
#             area.push1(width[i]*heights[i])
        
#         area=area.display()
        
#         area.sort()
#         return area[-1]