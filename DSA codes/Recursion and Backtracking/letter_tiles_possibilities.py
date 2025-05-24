from collections import Counter
class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        count = Counter(tiles)
        return self.backtrack(count)

    def backtrack(self,count):
        tot = 0
        for c in count:
            if count[c]==0:
                continue
            tot+=1
            count[c]-=1
            tot+=self.backtrack(count)
            count[c]+=1
        return tot

if __name__ == "__main__":
    obj = Solution()
    tiles = "AAB"
    print(obj.numTilePossibilities(tiles))