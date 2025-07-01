from collections import defaultdict
def twotypesNumbers(arr):
    maxi = 0
    i = 0
    count = defaultdict(int)
    for j in range(len(arr)):
        count[arr[j]]+=1
        
        if len(count)>2:
            count[arr[i]]-=1
            if count[arr[i]]==0:
                del count[arr[i]]
            i+=1
            
        if len(count)<=2:
            maxi = max(maxi, j-i+1)
    
    return maxi

def totalFruit(self, fruits) -> int:
        maxi = 0
        for i in range(len(fruits)):
            set1 = set()
            for j in range(i, len(fruits)):
                set1.add(fruits[j])
                if len(set1)<=2:
                    maxi = max(maxi, j-i+1)
                else:
                    break
        return maxi