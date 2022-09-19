# Taken from optimzed
# Here's the insight to the two -1: 
# The problem is easier if grouping starts from beginning
# So, just reverse it.
class Solution:
    def licenseKeyFormatting(self, S, K):
        S = S.replace("-", "").upper()[::-1]
        return '-'.join(S[i:i+K] for i in range(0, len(S), K))[::-1]


driver = Solution()
print(driver.licenseKeyFormatting("2-5g-3-J",
                                  2))
