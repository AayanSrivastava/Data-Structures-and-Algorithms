from collections import defaultdict, deque
class Solution:
    def bottomView(self, root):
        q=[]
        mapper=defaultdict(list)
        q.append([root,0])
        while q:
            node,pos=q.pop(0)
            if node==None:
                continue
            mapper[pos].append(node.data)
            q.append((node.left,pos-1))
            q.append((node.right,pos+1))

        output=[]
        for i in sorted(mapper):
            output.append(mapper[i][-1])
        return output

#optimised by using dict
class Solution:
    def bottomView(self, root):
        q=[]
        mapper=dict()
        q= deque([(root,0)])
        while q:
            node,pos=q.popleft()
            if node==None:
                continue
            mapper[pos]= node.data
            q.append((node.left,pos-1))
            q.append((node.right,pos+1))

        output=[]
        for i in sorted(mapper):
            output.append(mapper[i])
        return output
        