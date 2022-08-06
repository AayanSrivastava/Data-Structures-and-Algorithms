class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# METHOD-1 O(N)
class Solution:
    inomap=None
    post=None
    def get_tree(self,poststart,postend,instart,inend):
        ino_ind=inomap[post[postend]]
        l=ino_ind-instart
        r=inend-ino_ind
        root= TreeNode(post[postend])
        root.left=self.get_tree(poststart,poststart+l-1,instart,ino_ind-1) if l else None
        root.right=self.get_tree(poststart+l,postend-1,ino_ind+1,inend) if r else None
        return root
    
    def buildTree(self, inorder, postorder):
        global inomap,post
        n=len(postorder)
        post=postorder
        inomap={el:i for i,el in enumerate(inorder)}
        return self.get_tree(0,n-1,0,n-1)

# METHOD-2 O(N^2)
class Solution1:
    def buildTree(self,inorder, postorder):
        if not inorder or not postorder:
            return None
        root = TreeNode(postorder.pop())
        ind = inorder.index(root.val)
        root.right = self.buildTree(inorder[ind+1:], postorder)
        root.left = self.buildTree(inorder[:ind], postorder)
        return root
    