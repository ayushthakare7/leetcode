class Solution:
    
    def climbStairs(self, n: int) -> int:

        if n<=2:
            return n
        
        prev2, prev = 1,2

        for i in range(3,n+1):
            curr = prev + prev2
            prev2 = prev
            prev = curr
        return prev 
        
        

        