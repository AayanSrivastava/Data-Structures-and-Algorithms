'''update maxi only when window sum is greater than maxi,
dont update when window sum and maxi is equal, it will update wrong index'''

class Solution:
    def findMaxAverage(self, arr, n, k):
        i = 0
        window_sum=0
        maxi = float('-inf')
        index = 0
        for j in range(len(arr)):
            window_sum+=arr[j]

            if j - i + 1 > k:
                window_sum-=arr[i]
                i+=1
            
            if j-i+1 == k:
                if window_sum>maxi:
                    maxi = window_sum
                    index = i
        
        return index