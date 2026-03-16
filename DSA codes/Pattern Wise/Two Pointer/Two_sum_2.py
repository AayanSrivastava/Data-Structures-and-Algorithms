# data is sorted

def twoSum(numbers, target):
        numbers.sort()
        ans = []
        i, j = 0, len(numbers)-1
        while i<j:
            if numbers[i]+numbers[j] == target:
                ans.append(i+1)
                ans.append(j+1)
                break
            elif numbers[i]+numbers[j] > target:
                j-=1
            else:
                i+=1
        return ans

numbers = [2,4]
target = 6
print(twoSum(numbers, target))