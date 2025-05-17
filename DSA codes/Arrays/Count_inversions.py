class Solution: # Divide and merge
    def mergeSort(self,arr, low, high):
        if low>=high:
            return 0
        mid = (low + high)//2
        inv_left=self.mergeSort(arr, low, mid)
        inv_right=self.mergeSort(arr, mid+1, high)
        inv_merge=self.merge(arr, low, mid, high)

        return inv_left + inv_right + inv_merge
    
    def merge(self, arr, low, mid, high):
        left = low
        right = mid+1   

        cnt = 0
        temp_array = []
        while left <= mid and right <= high:
            if arr[left] <= arr[right]:
                temp_array.append(arr[left])
                left+=1
            else:
                temp_array.append(arr[right])
                cnt+=mid-left+1
                right+=1
            
        while left <= mid:
            temp_array.append(arr[left])
            left+=1
        while right <= high:
            temp_array.append(arr[right])
            right+=1
        
        for i in range(low,high+1):
            arr[i] = temp_array[i-low]

        return cnt
    def inversionCount(self, arr):
        return self.mergeSort(arr,0, len(arr)-1)
if __name__ == "__main__":
    obj = Solution()
    arr = [4,6,3,2,8,7,1]
    print(obj.mergeSort(arr,0, len(arr)-1))