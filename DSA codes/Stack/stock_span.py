# a=[100,80,60,70,65,75,80]

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

s=[100,80,60,70,65,75,80]
a=[]
st=stack()
# for i in range(len(s)-1,-1,-1):  #next greater to right
for i in range(len(s)):   #next greater to left
    if st.size()==0:
        a.append(-1)
    elif st.size()>0 and st.top()[0]>s[i]:
        a.append(i-st.top()[1])
    elif st.size()>0 and st.top()[0]<=s[i]:
        while st.size()>0 and st.top()[0]<=s[i]:
            st.pop()
        if st.size()==0:
            a.append(-1)
        else:
            a.append(i-st.top()[1])
    st.push(s[i],i)
print(a)