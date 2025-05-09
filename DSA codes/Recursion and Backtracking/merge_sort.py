class Solution: # Divide and merge
    def mergeSort(self,arr, low, high):
        if low>=high:
            return
        mid = (low + high)//2
        self.mergeSort(arr, low, mid)
        self.mergeSort(arr, mid+1, high)

        left = low
        right = mid+1   

        temp_array = []
        while left <= mid and right <= high:
            if arr[left] < arr[right]:
                temp_array.append(arr[left])
                left+=1
            else:
                temp_array.append(arr[right])
                right+=1
            
        while left <= mid:
            temp_array.append(arr[left])
            left+=1
        while right <= high:
            temp_array.append(arr[right])
            right+=1
        
        for i in range(low,high+1):
            arr[i] = temp_array[i-low]


if __name__ == "__main__":
    obj = Solution()
    arr = [4,6,3,2,8,7,1]
    obj.mergeSort(arr,0, len(arr)-1)
    print(arr)