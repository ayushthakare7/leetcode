from typing import List

class Solution:
    def maxSum(self, nums1: List[int], nums2: List[int]) -> int:
        MOD = 10**9 + 7

        i = 0
        j = 0
        n = len(nums1)
        m = len(nums2)

        sum1 = 0
        sum2 = 0
        ans = 0

        while i < n and j < m:
            if nums1[i] < nums2[j]:
                sum1 += nums1[i]
                i += 1

            elif nums1[i] > nums2[j]:
                sum2 += nums2[j]
                j += 1

            else:
                sum1 += nums1[i]
                sum2 += nums2[j]
                ans += max(sum1, sum2)

                sum1 = 0
                sum2 = 0

                i += 1
                j += 1

        while i < n:
            sum1 += nums1[i]
            i += 1

        while j < m:
            sum2 += nums2[j]
            j += 1

        ans += max(sum1, sum2)

        return ans % MOD