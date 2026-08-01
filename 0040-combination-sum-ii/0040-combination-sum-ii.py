class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        candidates.sort()
        def solve(subset,total,index):
            if total==0:
                result.append(subset.copy())
                return
            if total <0 :
                return
            if index >= len(candidates):
                return
            for i in range(index,len(candidates)):
                if i > index and candidates[i] == candidates[i-1]:
                    continue
                subset.append(candidates[i])
                Sum = total - candidates[i]
                solve(subset,Sum, i+1)
                subset.pop()
        solve([],target, 0)
        return result


                
        