class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        result = []
        nums = [1,2,3,4,5,6,7,8,9]

        def solve(subset, index, total, k):
            # Found a valid combination
            if k == 0 and total == n:
                result.append(subset.copy())
                return

            # Invalid state
            if index >= len(nums):
                return
            if k < 0:
                return
            if total > n:
                return

            # Include current number
            subset.append(nums[index])
            solve(subset, index + 1, total + nums[index], k - 1)
            subset.pop()

            # Exclude current number
            solve(subset, index + 1, total, k)

        solve([], 0, 0, k)
        return result