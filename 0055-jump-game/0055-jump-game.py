class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        i=0
        max_index = 0
        
        while i<=max_index:
            max_index = max(max_index, i + nums[i])
            i = i+1
            if max_index>=len(nums)-1:
                return True 
            
        return False
            

        