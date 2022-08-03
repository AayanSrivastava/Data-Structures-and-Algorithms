r=0
def height(self,root):
    if root==None:
        return 0
    lh=self.height(root.left)
    rh=self.height(root.right)
    self.r=max(self.r,lh+rh)
    
    return 1+ max(lh,rh)

def diameterOfBinaryTree(self, root):
    self.height(root)
    return self.r