from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root):
        ans=[]
        
        if root==None:
            return ans
        
        queue=deque([root])
        
        while queue:
            
            n=len(queue)
            level=[]
            
            for i in range(n):
                
                node=queue.popleft()
                
                if node.left!=None: queue.append(node.left)
                if node.right!=None: queue.append(node.right)
                    
                level.append(node.val)
                
            ans.append(level)
        return ans
    
l=Solution()
root=[1,2,3,4,5]
print(l.levelOrder(root))