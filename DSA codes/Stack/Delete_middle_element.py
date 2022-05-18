class stack:
    def __init__(self):
        self.container=[]

    def push(self,val):
        self.container.append(val)

    def pop(self):
        return self.container.pop()

    def peek(self):
        if self.container:
            return self.container[-1]
        else:
            return None

    def empty(self):
        if self.container:
            return len(self.container)==0
        else:
            return None
    
    def size(self):
        return len(self.container)
    
    def display(self):
        return self.container

s=[1,2,3,4,5]
c=0
N=5    
st=stack()
st1=stack()
for i in s:
    st.push(i)
for i in s:
    c+=1
    st1.push(st.pop())
    if c==N//2:
        st.pop()
        break
for i in st1.container:
    st.push(i)
print(st.display())