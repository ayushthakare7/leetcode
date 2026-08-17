class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 0
        maxi = 0
        dict = {}

        while right < len(s):
            if s[right] in dict:
                left = max(left, dict[s[right]] + 1)

            dict[s[right]] = right

            right = right + 1

            maxi = max(maxi, right - left)

        return maxi