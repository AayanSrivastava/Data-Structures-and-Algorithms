class Solution:
    def series(self, n):
        for i in range(n):
            print(self.print_fib(i), end=" ")
        return n
    
    def print_fib(self, n): 
        if n <= 1:
            return n
        return self.print_fib(n - 1) + self.print_fib(n - 2)

if __name__ == "__main__":
    n = 5
    obj = Solution()
    result = obj.series(n)
    print(result)