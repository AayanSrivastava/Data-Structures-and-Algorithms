class Solution:
    def tleft(self,root,ans):
        if root==None or (root.left==None and root.right==None):
            return
        ans.append(root.data)
        
        if root.left:
            self.tleft(root.left,ans)
        else:
            self.tleft(root.right,ans)
        
    def tleaf(self,root,ans):
        if root==None:
            return
        if root.left==None and root.right==None:
            ans.append(root.data)
            return
        
        self.tleaf(root.left,ans)    
        self.tleaf(root.right,ans)    
        
    def tright(self,root,ans):
        if root==None or (root.left==None and root.right==None):
            return
        
        if root.right:
            self.tright(root.right,ans)
        else:
            self.tright(root.left,ans)
        ans.append(root.data)
            
    def printBoundaryView(self, root):
        ans=[]
        if root==None:
            return ans
        ans.append(root.data)
        
        self.tleft(root.left,ans)
        self.tleaf(root.left,ans)
        self.tleaf(root.right,ans)
        self.tright(root.right,ans)
        return ans