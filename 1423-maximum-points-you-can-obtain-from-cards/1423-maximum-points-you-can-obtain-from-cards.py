class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        i = 0
        j = k - 1
        total = 0

        while i < k:
            total += cardPoints[i]
            i += 1

        maxi = total

        i = k - 1
        j = 1

        while j <= k:
            total -= cardPoints[i]
            total += cardPoints[-j]

            maxi = max(maxi, total)

            i -= 1
            j += 1

        return maxi