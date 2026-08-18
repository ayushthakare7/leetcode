class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        i = 0
        zeros = 0
        maxi = 0

        for j in range(len(nums)):
            zeros += nums[j] == 0

            while zeros > k:
                zeros -= nums[i] == 0
                i += 1

            maxi = max(maxi, j - i + 1)

        return maxi