class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        count = 0
        original = s[1:]

        while count != len(s):
            s =  original + s[0]
            original = s[1:]
            count = count + 1
            if s == goal :
                return True
            
        return False 
            

        