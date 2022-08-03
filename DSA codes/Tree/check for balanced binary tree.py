class Solution:
    def dfs(self,root):
        if root==None:
            return 0
        
        lh=self.dfs(root.left)
        if lh==-1:
            return -1
        rh=self.dfs(root.right)
        if rh==-1:
            return -1
        if abs(rh-lh)>1:
            return -1
        return 1+max(lh,rh)

    def isBalanced(self,root):
        return self.dfs(root)!=-1