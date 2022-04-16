class stack:
    def __init__(self):
        self.container=[]

    def push(self,val):
        self.container.append(val)

    def pop(self):
        return self.container.pop()
    
    def display(self):
        return self.container

class Solution:
    def reverse(self, x: int) -> int:
        s=stack()
        s1=stack()
        x=str(x)
        for i in x:
            s.push(i)
        for i in range(len(x)):
            s1.push(s.pop())
        return ''.join(s1.display())

obj=Solution()
print(obj.reverse(-123))