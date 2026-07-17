class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        def helper(arr):
            prev = arr[0]
            prev2 = 0

            for i in range(1, len(arr)):
                pick = arr[i]
                if i > 1:
                    pick += prev2

                not_pick = prev
                curr = max(pick, not_pick)

                prev2 = prev
                prev = curr

            return prev

        return max(helper(nums[:-1]), helper(nums[1:]))