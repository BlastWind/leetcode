class Solution:
    def countSpecialNumbers(self, n: int) -> int:
        dp = [[[[-1 for i in range(2)] for i in range(2)]
               for i in range(1 << 10)] for i in range(10)]

        def fun(i, leading_zeros, tight, memo):
            if i == len(str(n)):
                if leading_zeros == 1:
                    return 0
                return 1
            if dp[i][memo][tight][leading_zeros] != -1:
                print(memo, tight, dp[i][memo][tight][leading_zeros])
                return dp[i][memo][tight][leading_zeros]
            end = 9
            if tight == 1:
                end = int(str(n)[i])
            ans = 0
            for j in range(end+1):
                if j == 0:
                    if leading_zeros == 1:
                        ans += fun(i+1, 1, tight & (j == end), memo)
                    else:
                        if memo & (1 << j) == 0:
                            ans += fun(i+1, 0, tight & (j == end),
                                       memo | (1 << j))
                else:
                    if memo & (1 << j) == 0:
                        ans += fun(i+1, 0, tight & (j == end), memo | (1 << j))
            dp[i][memo][tight][leading_zeros] = ans
            return ans
        return fun(0, 1, 1, 0)


driver = Solution()
print(driver.countSpecialNumbers(4002))
a = set()
