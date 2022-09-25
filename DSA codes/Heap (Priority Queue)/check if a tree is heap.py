class Solution:
    #Your Function Should return True/False
    def maxorder(self,root):
        if root.left==None and root.right==None:
            return True
        
        if root.right==None:
            return root.data>root.left.data
        
        else:
            return root.data>root.left.data and root.data>root.right.data and self.maxorder(root.left) and self.maxorder(root.right)
        
    def isCBT(self,root,i,nodecount):
        if root==None:
            return True
        if i>=nodecount:
            return False

        return self.isCBT(root.left,2*i+1,nodecount) and self.isCBT(root.right,2*i+2,nodecount)
            
    def count(self,root):
        if root is None:
            return 0
        return (1+self.count(root.left) + self.count(root.right))
    
    def isHeap(self, root):
        nodecount=self.count(root)
        return self.isCBT(root,0,nodecount) and self.maxorder(root)