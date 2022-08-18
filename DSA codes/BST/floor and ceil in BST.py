class Node:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None
    
def insert(root,key):
    if root==None:
        return Node(key)
    elif root.val>key:
        root.left=insert(root.left,key)
    else:
        root.right=insert(root.right,key)
    return root

def inorder(root):
    if root==None:
        return
    inorder(root.left)
    print(root.val)
    inorder(root.right)

root=insert(None,5)
insert(root,4)
insert(root,7)
insert(root,2)
insert(root,9)
inorder(root)