class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        dict = {}
        i = 0
        
        while i < len(s):
            if s[i] in dict:
                dict[s[i]] += 1
            else:
                dict[s[i]] = 1
            i += 1

        j = 0
        while j < len(t):
            if t[j] in dict:
                dict[t[j]] -= 1
            else:
                return False
            j += 1

        for a in dict:
            if dict[a] == 0:
                continue
            else:
                return False

        return True