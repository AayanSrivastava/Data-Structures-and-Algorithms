class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def solve(self,root,a):
        if root==None:
            return
        
        a.append(root.val)
        self.solve(root.left,a)
        self.solve(root.right,a)
        
    def preorderTraversal(self, root):
        a=[]
        self.solve(root,a)
        return a
    
l=Solution()
# print(l.preorderTraversal(root))