class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# METHOD-1 O(N)
class Solution:
    inomap=None
    pre=None
    def get_tree(self,prestart,preend,instart,inend):
        ino_ind=inomap[pre[prestart]]
        l=ino_ind-instart
        r=inend-ino_ind
        root= TreeNode(pre[prestart])
        root.left=self.get_tree(prestart+1,prestart+l,instart,ino_ind-1) if l else None
        root.right=self.get_tree(prestart+l+1,preend,ino_ind+1,inend) if r else None
        return root
    
    def buildTree(self, preorder,inorder):
        global inomap,pre
        n=len(preorder)
        pre=preorder
        inomap={el:i for i,el in enumerate(inorder)}
        return self.get_tree(0,n-1,0,n-1)

# METHOD-2 O(N^2)
class Solution1:
    def buildTree(self, preorder,inorder):
        if inorder:
            ind = inorder.index(preorder.pop(0))
            root = TreeNode(inorder[ind])
            root.left = self.buildTree(preorder, inorder[0:ind])
            root.right = self.buildTree(preorder, inorder[ind+1:])
            return root