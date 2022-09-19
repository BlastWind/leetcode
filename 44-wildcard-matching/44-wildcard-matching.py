from typing import List
import sys 
sys.setrecursionlimit(2000)
class Solution:
    def __init__(self) -> None:
        self.iterations = 0
    def isMatch(self, s: str, p: str) -> bool:
        # the ith pattern and the jth input is true if EITHER
        #   the (i-1)th pattern is True AND the characters s[j] and p[i] match (or question mark)
        #   p[i] is an asterisk and the characters the (j-1)th problem is true
        dp = [[False] * (len(s)+1) for _ in range(len(p)+1)]
        dp[0] = [False] * (len(s) + 1)
        for i in range(len(p) + 1):
            dp[i][0] = True if i == 0 else dp[i-1][0] and p[i-1] == '*'       
        for i, curP in enumerate(p, 1):
            for j, curS in enumerate(s, 1):
                if curP == '*':
                    # last used asterisk or smaller match True
                    dp[i][j] = dp[i][j-1] or dp[i-1][j]
                else: 
                    dp[i][j] = dp[i-1][j-1] and (curP == '?' or curP == curS)
        # for line in reversed(dp):
        #     print(line)
        return dp[len(dp)-1][len(dp[0])-1]


class Solution2:
    def isMatch(self, s: str, p: str) -> bool:
        s_len, p_len = len(s), len(p)
        s_idx = p_idx = 0
        star_idx = s_tmp_idx = -1

        while s_idx < s_len:
            # If the pattern caracter = string character
            # or pattern character = '?'
            if p_idx < p_len and p[p_idx] in ['?', s[s_idx]]:
                s_idx += 1
                p_idx += 1

            # If pattern character = '*'
            elif p_idx < p_len and p[p_idx] == '*':
                # Check the situation
                # when '*' matches no characters
                star_idx = p_idx
                s_tmp_idx = s_idx
                p_idx += 1

            # If pattern character != string character
            # or pattern is used up
            # and there was no '*' character in pattern
            elif star_idx == -1:
                return False

            # If pattern character != string character
            # or pattern is used up
            # and there was '*' character in pattern before
            else:
                # Backtrack: check the situation
                # when '*' matches one more character
                p_idx = star_idx + 1
                s_idx = s_tmp_idx + 1
                s_tmp_idx = s_idx

        # The remaining characters in the pattern should all be '*' characters
        return all(p[i] == '*' for i in range(p_idx, p_len))

driver = Solution2()
print(driver.isMatch("abcabczzzde",
      "*abc???de*"))

