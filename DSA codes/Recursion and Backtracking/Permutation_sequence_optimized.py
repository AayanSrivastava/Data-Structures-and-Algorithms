class Solution:
    def permutation_seq(self, n, k):
        fact = 1
        numbers = []
        for i in range(1,n):
            fact= fact * i
            numbers.append(i)
        numbers.append(n)

        ans = ""
        k = k-1
        while True:
            ans+= str(numbers[k//fact])
            del numbers[k//fact]
            if len(numbers) == 0:
                break

            k = k % fact
            fact = fact//len(numbers)
        return ans

if __name__ == "__main__":
    obj = Solution()
    n = 4
    k = 3
    print(obj.permutation_seq(n,k))