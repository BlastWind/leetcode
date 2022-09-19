from typing import List


class Solution:
    def candy(self, ratings: List[int]) -> int:
        # sort descending and enlist indices along with sorted value
        # init arr to [1, ..., 1]
        # from minimum to maximum, if value is neighbors are greater, add 1 to the neighbors
        res = [1] * len(ratings)
        for _, i in sorted([(r, i) for i, r in enumerate(ratings)]):
            if i+1 < len(ratings) and ratings[i] < ratings[i+1] and res[i] >= res[i+1]:
                res[i+1] = res[i] + 1
            if i-1 >= 0 and ratings[i] < ratings[i-1] and res[i] >= res[i-1]:
                res[i-1] = res[i] + 1

        return sum(res)

    def candy2(self, ratings) -> int:
        up = 1
        down = 0
        rat = 1
        peak = 0

        for i in range(1, len(ratings)):

            if ratings[i] > ratings[i-1]:
                up += 1
                down = 0
                rat += up
                peak = up

            elif ratings[i] == ratings[i-1]:
                down = 0
                peak = 0
                up = 1
                rat += 1

            else:
                down += 1
                up = 1
                rat += down
                if peak <= down:
                    rat += 1

        return rat


driver = Solution()
print(driver.candy2([1, 2, 5, 4, 3, 2, 1, 2, 6, 5]))
