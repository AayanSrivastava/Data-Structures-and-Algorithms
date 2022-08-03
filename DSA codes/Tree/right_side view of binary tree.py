from collections import deque
class Solution:
    def rightSideView(self, root):
        ans=[]
        if root==None:
            return ans
        
        queue=deque([root])
        
        while queue:
            n=len(queue)
            level=[]
            
            for i in range(n):
                node=queue.popleft()
                if node.left!=None:
                    queue.append(node.left)
                if node.right!=None:
                    queue.append(node.right)
                level.append(node.val)
            ans.append(level[-1])
        return ans


# LEFT VIEW OF BINARY TREE 
def solve(root,level,ds):
    if root==None:
        return
    if len(ds)==level:
        ds.append(root.data)
    solve(root.left,level+1,ds)
    solve(root.right,level+1,ds)
def LeftView(root):
    ds=[]
    solve(root,0,ds)
    return ds