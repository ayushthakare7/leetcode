class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        result =[]
        count = 0
        for char in s:
            if char == "(" :
                count+=1
            if char =="(" and count>1:
                result.append(char)
                

            if char ==")":
                count-=1
                if count>0:
                    result.append(char)
               
        return "".join(result)

                
            
            


        