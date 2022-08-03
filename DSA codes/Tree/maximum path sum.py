class Solution:
    r=float('-inf')
    def height(self,root):
        if root==None:
            return 0
        
        leftsum=max(0,self.height(root.left))
        rightsum=max(0,self.height(root.right))
        self.r=max(self.r,root.val+leftsum+rightsum)
        return root.val+max(leftsum,rightsum)
    
    def maxPathSum(self, root):
        self.height(root)
        return self.r