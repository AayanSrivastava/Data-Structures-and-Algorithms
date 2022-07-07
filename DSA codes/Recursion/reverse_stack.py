def rev(stack):
    st=[]
    if(len(stack)==0):
        return

    st.append(stack.pop())
    rev(stack)
    return st

s=[1,2,3,4,5]
print(rev(s))