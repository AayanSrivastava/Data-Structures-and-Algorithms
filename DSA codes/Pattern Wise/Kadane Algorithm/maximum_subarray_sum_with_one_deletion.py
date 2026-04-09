class Solution:
    def maximumSum(self, arr):
        nodelete = arr[0]
        onedelete = 0
        result = arr[0]
        for i in range(1,len(arr)):
            onedelete = max(onedelete + arr[i], nodelete)
            nodelete = max(nodelete+arr[i], arr[i])

            result = max(result, nodelete, onedelete)
        
        return result