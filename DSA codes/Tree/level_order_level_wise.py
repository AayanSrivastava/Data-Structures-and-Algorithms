from collections import deque
class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def levelOrder(root):
    # ans=[]
    # if root==None:
    #     return ans

    queue=deque([None,root])
    while True:
        node=queue.pop()
        if node:
            print(node.val)
            if node.left!=None:
                queue.appendleft(node.left)
            if node.right!=None:
                queue.appendleft(node.right)
        else:
            print("-------")
            if queue:
                queue.appendleft(None)
            else:
                break

root= TreeNode(1, TreeNode(2, TreeNode(3), TreeNode(4)), TreeNode(4, TreeNode(5), TreeNode(6)))
print(levelOrder(root))