def countTriplets(self, n, sum, arr):
    arr.sort()
    cnt=0
    for i in range(n-2):
        j, k = i+1, n-1
        while j<k:
            total = arr[i]+arr[j]+arr[k]
            if total < sum:
                cnt+=k-j    # all elements before k will be smaller
                j+=1
            else:
                k-=1
    return cnt