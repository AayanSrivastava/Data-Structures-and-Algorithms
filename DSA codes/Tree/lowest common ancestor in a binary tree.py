class Solution:
    def solve(self,root,a,ans,n1,n2):
        if root==None:
            return None
        # a.append(root.data)
        if root.value==n1 or root.value==n2:
            return root
        if root.left:
            self.solve(root.left,a,ans,n1,n2)
        else:
            self.solve(root.right,a,ans,n1,n2)
        
    def lca(self,root, n1, n2):
        a=[]
        ans=[]
        return self.solve(root,a,ans,n1,n2)

# 2nd METHOD

# def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
#         if root==None or root==p or root==q:
#             return root
        
#         left=self.lowestCommonAncestor(root.left,p,q)
#         right=self.lowestCommonAncestor(root.right,p,q)
        
#         if left==None:
#             return right
        
#         if right==None:
#             return left
        
#         else:
#             return root