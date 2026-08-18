class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        i = 0
        zeros = 0
        maxi = 0

        for j in range(len(nums)):
            if nums[j] == 0:
                zeros += 1

            # CHANGED: shrink window while zeros > k
            while zeros > k:
                if nums[i] == 0:
                    zeros -= 1
                i += 1

            maxi = max(maxi, j - i + 1)

        return maxi