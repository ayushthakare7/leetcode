class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        i = 0
        j = 0
        maxi = 0
        length = 0
        remain = k

        while j < len(nums):
            if nums[j] == 1:
                j = j + 1
            else:
                if remain != 0:
                    remain -= 1
                    j = j + 1
                else:
                    # CHANGED: Don't reset i = j.
                    # Move i until we remove the previous 0.
                    while nums[i] == 1:       # CHANGED
                        i += 1                 # CHANGED

                    i += 1                     # CHANGED: Remove that 0
                    remain += 1                 # CHANGED: We now have 1 flip available

            length = j - i                     # CHANGED: Calculate window length here
            maxi = max(maxi, length)           # CHANGED: Update maximum every iteration

        return maxi