class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
def constructMaximumBinaryTree(self, nums):
    if not nums:
        return None
    a=nums.index(max(nums))
    root=TreeNode(nums[a])
    
    root.left=self.constructMaximumBinaryTree(nums[:a])
    root.right=self.constructMaximumBinaryTree(nums[a+1:])
    
    return root