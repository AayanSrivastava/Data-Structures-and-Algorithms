from collections import deque
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def createNode(self,data):
        return TreeNode(data)
    
    def insert(self,node,data):
        if node is None:
           return self.createNode(data)
        if data < node.val:
            node.left=self.insert(node.left,data)
        else:
            node.right=self.insert(node.right,data)
        return node

    def levelOrder(self, root):
        ans=[]
        
        if root==None:
            return ans
        
        queue=deque([root])
        
        while queue:
            level=[]
            node=queue.pop()
            if node.left!=None:
                queue.append(node.left)
            if node.right!=None:
                queue.append(node.right)
            level.append(node.val)
                
            ans.append(level)
        return ans
        
    
l=Solution()
root=l.createNode(0)
l.insert(root,1)
l.insert(root,2)
l.insert(root,3)
l.insert(root,4)
l.insert(root,5)
l.insert(root,6)
l.insert(root,7)
print(l.levelOrder(root.right))