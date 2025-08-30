def getLeastFrequentDigit(n: int) -> int:
        freq = {}
        for i in str(n):
            if i in freq:
                freq[i]+=1
            else:
                freq[i]=1
        ans = 0
        mini = float('inf')
        for k,v in sorted(freq.items()):
            if freq[k]<mini:
                mini = freq[k]
                ans = int(k)
        return ans

n = 2
print(getLeastFrequentDigit(n))