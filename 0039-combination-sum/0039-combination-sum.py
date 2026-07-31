class Solution:
    def solve(self,index,total,subset,nums, target,result):
        if total == target :
            result.append(subset.copy())
            return
        elif total > target :
            return
        if index>=len(nums):
            return    
        Sum = total + nums[index]
        subset.append(nums[index])
        self.solve(index, Sum,subset,nums, target,result)
        Sum = total
        subset.pop()
        self.solve(index+1,Sum,subset,nums, target,result)

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        self.solve(0,0,[],candidates,target,result)
        return result
    