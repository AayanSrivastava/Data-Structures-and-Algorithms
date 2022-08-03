from collections import deque
class Solution:
    def zigZagTraversal(self, root):
        ans=[]
        if root==None:
            return ans
            
        queue=deque([root])
        even_level=False
        
        while queue:
            n=len(queue)
            level=[]
            
            for i in range(n):
                node=queue.popleft()
                level.append(node.data)
                
                if node.left!=None:
                    queue.append(node.left)
                if node.right!=None:
                    queue.append(node.right)
            
            if even_level:
                ans.extend(level[::-1])
            else:
                ans.extend(level)
                
            even_level=not even_level
        return ans