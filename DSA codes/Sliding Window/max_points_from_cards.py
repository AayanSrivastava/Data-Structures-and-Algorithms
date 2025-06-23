class Solution:
    def maxScore(self, cardPoints, k):
        leftsum = 0
        rightsum = 0
        maxsum = 0
        n = len(cardPoints)
        for j in range(k):
            leftsum+=cardPoints[j]
            maxsum = leftsum

        rindex = n - 1
        for i in range(k-1,-1,-1):
            leftsum-=cardPoints[i]
            rightsum+=cardPoints[rindex]
            rindex-=1

            maxsum = max(maxsum, leftsum+rightsum)

        return maxsum