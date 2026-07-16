class Solution:
    def rob(self, nums: List[int]) -> int:
        prev = nums[0]
        prev2 = 0
        n = len(nums)
        for index in range(1,n):
            if index > 1:
                pick = nums[index] + prev2
            else :
                pick = nums[index]
            not_pick = 0 + prev
            curr = max(pick, not_pick)
            prev2 = prev
            prev = curr
        return prev
        
        