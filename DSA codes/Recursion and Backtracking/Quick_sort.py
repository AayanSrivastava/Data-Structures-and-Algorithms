class Solution: # Divide and conquer
    def quickSort(self,arr, low, high):
        if low < high:
            pivot = self.partition(arr, low, high)
            self.quickSort(arr, low, pivot-1)
            self.quickSort(arr, pivot+1, high)

    def partition(self, arr, low, high):
        pivot = arr[low]
        i = low
        j = high

        while i < j:
            while arr[i] <= pivot and i <= high-1:
                i+=1
            while arr[j] > pivot and j >= low+1:
                j-=1
            if i<j:
                arr[i], arr[j] = arr[j], arr[i]
        
        arr[low], arr[j] = arr[j], arr[low]
        return j


if __name__ == "__main__":
    l = Solution()
    arr = [2,5,4,7,9,1,6,3,4,8,5,3,0]
    l.quickSort(arr, 0, len(arr)-1)
    print(arr)