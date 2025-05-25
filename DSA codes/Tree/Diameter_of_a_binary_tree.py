class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def solve(self, root, diameter):
        if root == None:
            return 0
        
        lh = self.solve(root.left, diameter)
        rh = self.solve(root.right, diameter)
        diameter[0] = max(diameter[0], lh+rh)
        return 1 + max(lh, rh) 
        
    def diameterOfBinaryTree(self, root) -> int:
        diameter = [0]
        self.solve(root, diameter)
        return diameter[0]
    
if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)

    obj = Solution()
    print(obj.diameterOfBinaryTree(root))