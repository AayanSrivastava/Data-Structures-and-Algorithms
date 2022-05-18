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
    
class Solution:
    def isValid(self, s: str) -> bool:
        st=stack()
        for i in s:
            if (i=='(' or i=='{' or i=='['):
                st.push(i)
            else:
                if not st.empty():
                    if ((i==')' and st.peek()=='(') or
                        (i=='}' and st.peek()=='{') or
                        (i==']' and st.peek()=='[')):
                        st.pop()
                    else:
                        return False
                else:
                    return False
        if st.empty():
            return True
        else:
            return False
obj=Solution()
print(obj.isValid("()"))