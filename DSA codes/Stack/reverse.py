from collections import deque

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

    def is_empty(self):
        if self.container:
            return len(self.container)==0
        else:
            return None
    
    def size(self):
        return len(self.container)
    
    def display(self):
        return self.container

s=stack()
s1=''
st="Done"
for i in st:
    s.push(i)
for i in range(s.size()):
    s1+=s.pop()
# print(''.join(s1.display()))
print(s1)