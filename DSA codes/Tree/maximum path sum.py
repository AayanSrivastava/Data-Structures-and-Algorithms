class Solution:
    maxi = float('-inf')
    def solve(self, root):
        if root == None:
            return 0
        leftsum = max(0, self.solve(root.left))
        rightsum = max(0, self.solve(root.right))
        self.maxi = max(self.maxi, leftsum + rightsum + root.val)
        return max(leftsum, rightsum) + root.val

    def maxPathSum(self, root) -> int:
        self.solve(root)
        return self.maxi