

class Solution:
    def largestPalindromic(self, num: str) -> str:
        # build frequency count
        freq = [0] * 10
        for i in num:
            freq[int(i)] += 1

        prefix = ""

        for i in range(9, 0, -1):
            count = freq[i]
            prefix += str(i) * (count // 2)
            freq[i] = count % 2

        if len(prefix) > 0:  # Can only append non-leading zeroes
            zeroCount = freq[0]
            prefix += str(0) * (zeroCount // 2)
            freq[0] = zeroCount % 2

        # How to find the highest index with value > 0? Probably just for loop
        for i in range(9, -1, -1):
            count = freq[i]
            if count >= 1:
                return prefix + str(i) + ''.join(list(reversed(prefix)))

        return prefix + ''.join(list(reversed(prefix)))


a = Solution()
print(a.largestPalindromic("00000"))
# sandwich pairs off as much as possible
