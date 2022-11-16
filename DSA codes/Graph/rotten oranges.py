from collections import deque
q=deque()
q.append([[1,2],0])
x=q.pop()
print(x)
row,col=x[0]
time=x[1]
print(row,col,time)