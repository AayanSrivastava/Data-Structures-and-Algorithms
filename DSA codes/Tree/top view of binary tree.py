from collections import defaultdict,deque
class Solution:
    def topView(self,root):
        mapper=dict()
        q= deque([(root,0)])
        while q:
            node,pos=q.popleft()
            if node==None:
                continue
            if pos not in mapper:
                mapper[pos]=node.data
            q.append((node.left,pos-1))
            q.append((node.right,pos+1))

        output=[]
        for i in sorted(mapper):
            output.append(mapper[i])
        return output