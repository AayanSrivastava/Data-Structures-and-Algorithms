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

def floor(root,key):
    ans=-1
    while root:
        if root.val==key:
            ans=root.val
            return ans
        elif key>root.val:
            ans=root.val
            root=root.right
        else:
            root=root.left
    return ans

def ceil(root,key):
    ans=-1
    while root:
        if root.val==key:
            ans=root.val
            return ans
        if key>root.val:
            root=root.right
        else:
            ans=root.val
            root=root.left
        return ans

def inorder(root):
    if root==None:
        return
    inorder(root.left)
    print(root.val)
    inorder(root.right)

# root=Node(5)
root=insert(None,5)
insert(root,4)
insert(root,7)
insert(root,2)
insert(root,9)
inorder(root)