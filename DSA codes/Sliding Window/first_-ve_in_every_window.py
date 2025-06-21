''''When the window slides (i.e., you do i += 1), 
you're removing the leftmost element from the window.
If that element happens to be the first negative number stored in your deque,
it's no longer part of the current window, so:'''

from collections import deque
class Solution:
    def firstNegInt(self, arr, k): 
        i = 0
        q = deque()
        ans = []
        for j in range(len(arr)):
            if arr[j]<0:
                q.append(j)
            
            if j-i+1 > k:
                if q and q[0] == i:
                    q.popleft()
                i+=1
            
            if j-i+1==k:
                ans.append(arr[q[0]] if q else 0)
        
        return ans

class Solution:
    def firstNegInt(self, arr, k): 
        i = 0
        ans = []
        for j in range(len(arr)):
            flag = False
            
            if j-i+1 > k:
                i+=1
            
            if j-i+1==k:
                for num in arr[i:j+1]:
                    if num<0:
                        ans.append(num)
                        flag = True
                        break
                if not flag:
                    ans.append(0)
        
        return ans