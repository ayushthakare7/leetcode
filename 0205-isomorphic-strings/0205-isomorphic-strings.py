class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        map_stot = {}
        map_ttos = {}
        n = len(s)
        m = len(t)

        if m!=n:
            return False
        else:
            for i in range(n):
                if s[i] in map_stot:
                    if t[i] != map_stot[s[i]]:
                        return False
                

                else:
                    map_stot[s[i]]=t[i]

            
                if t[i] in map_ttos:
                    if s[i] != map_ttos[t[i]]:
                        return False
                

                else:
                    map_ttos[t[i]]=s[i]
            return True


            

       



        