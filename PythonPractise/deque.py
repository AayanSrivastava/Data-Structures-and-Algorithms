from collections import deque
def deq(q):
    # q.append(1)
    # q.appendleft(1)

    # q.pop()
    # q.popleft()

    # q.rotate(1)
    q.rotate(-1)
    return q

q=deque([1,2,3,4])
print(deq(q))