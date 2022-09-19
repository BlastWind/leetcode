class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        dp = [0] * 128
        for c in s:
            dp[ord(c)] = 1 + max(dp[ord(c) - k: ord(c) + k + 1])
        return max(dp)

a = Solution()
print(a.longestIdealString("azaza", 25))
