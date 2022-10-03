from collections import defaultdict


class Solution:
    def equalFrequency(self, word: str) -> bool:
        # word = "abcdee", letterToCount = {'a': 1, 'b': 1, 'c': 1, 'd': 1, 'e': 2}
        letterToCount = defaultdict(int)
        for c in word: 
            letterToCount[c] += 1

        # word = "abcdee", countFreq = {1: 4, 2: 1}
        countFreq = defaultdict(int)
        for f in letterToCount.values():
            countFreq[f] += 1

        if len(countFreq) > 2: return False
        if len(countFreq) == 1: return next(iter(countFreq)) == 1 or countFreq[next(iter(countFreq))] == 1

        # Only 2 different frequencies of count left


        # newCountFreq is countFreq after deleting the character with max freq (this would -1 the max freq and +1 the second freq)
        # if countFreq = {1: 4, 2: 1}, newCountFreq = {1: 5}
        i = iter(countFreq)
        k1, k2 = next(i), next(i)
        v1, v2 = countFreq[k1], countFreq[k2]
        maxK, minK = max(k1, k2), min(k1, k2)
        if (v1 == 1 and k1 == 1) or (v2 == 1 and k2 == 1): return True
        newCountFreq = defaultdict(int)
        newCountFreq[minK] = countFreq[minK]
        newCountFreq[maxK - 1] += 1
        if countFreq[maxK] - 1 > 0: 
            newCountFreq[maxK] += countFreq[maxK] - 1

        return len(newCountFreq) == 1
a = Solution()
# print(a.equalFrequency("aaabbccc"))
print(a.equalFrequency("aa"))
# print(a.equalFrequency("abc"))
# print(a.equalFrequency("aab"))
# print(a.equalFrequency("aaaac"))
# print(a.equalFrequency("abcdee"))
# print(a.equalFrequency("lxll"))
# print(a.equalFrequency("aaffggg"))
# print(a.equalFrequency("aggfe"))
# print(a.equalFrequency("abssjfj"))