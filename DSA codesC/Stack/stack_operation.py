from collections import deque

class stack:
    def __init__(self):
        self.container=deque()

    def push(self,val):
        self.container.append(val)

    def pop(self):
        self.container.pop()

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
s.push(1)
s.push(3)
s.push(5)
print(s.size())
print(s.is_empty())
print(s.display())