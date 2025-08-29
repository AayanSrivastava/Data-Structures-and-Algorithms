def subArrayExists(self,arr):
    cursum = 0
    seen = set()
    for i in arr:
        cursum+=i
        if cursum == 0 or cursum in seen:
            return True
        seen.add(cursum)
    return False

# 2nd
def subArrayExists(self,arr):
    cnt = 0
    cursum = 0
    prefixsum = {0 : 1}
    for i in arr:
        cursum+=i
        cnt+=prefixsum.get(cursum, 0)
        prefixsum[cursum] = prefixsum.get(cursum, 0)+1
    return cnt
