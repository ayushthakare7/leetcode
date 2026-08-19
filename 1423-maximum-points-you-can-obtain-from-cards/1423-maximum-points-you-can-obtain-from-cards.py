class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        left_sum = 0
        right_sum = 0
        maxi = 0

        for i in range(k):
            left_sum += cardPoints[i]

        maxi = left_sum

        for i in range(k - 1, -1, -1):
            left_sum -= cardPoints[i]
            right_sum += cardPoints[len(cardPoints) - (k - i)]

            maxi = max(maxi, left_sum + right_sum)

        return maxi