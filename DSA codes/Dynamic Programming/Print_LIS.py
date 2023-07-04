def LISTracePrint(arr,n):
        dp=[1]*n
        hashh=[0]*n
        maxi=1
        lastindex=0
        for i in range(n):
            hashh[i]=i
            for prev in range(i):
                if arr[prev]<arr[i] and 1+dp[prev]>dp[i]:
                    dp[i]=1+dp[prev]
                    hashh[i]=prev
            if dp[i]>maxi:
                maxi=dp[i]
                lastindex=i
        
        temp=[]
        temp.append(arr[lastindex])
        while hashh[lastindex]!=lastindex:
            lastindex=hashh[lastindex]
            temp.append(arr[lastindex])
        return temp[::-1]
arr=[5,4,11,1,16,8]
print(LISTracePrint(arr,6))