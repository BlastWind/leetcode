from collections import defaultdict
from heapq import heappush, heappushpop
from itertools import groupby
from typing import List


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        # keep min heap with k elements, value that determines ranking is the frequency
        pq = []
        freq = defaultdict(int)
        used = set()
        for word in words:
            freq[word] += 1
            if pq: 
                prevFreq, wordd = pq[0]
                pq[0] = (freq[wordd], wordd)
            if word in used:
                continue
            if len(pq) < k:
                heappush(pq, (freq[word], word))
                used.add(word)
            else:
                _, poppedWord = heappushpop(pq, (freq[word], word))
                used.add(word)
                used.remove(poppedWord)
            # print(pq, freq)

        # Descending frequency
        refined = [(freq[word], word) for oldFreq, word in pq]
        arr = sorted(refined, key=lambda x: x[0], reverse=True)
        # groupBy same frequency
        splits = groupby(arr, key=lambda x: x[0])
        # lexicographically ascending

        return [word for f, grouper in splits for _, word in sorted(list(grouper))]

        # return [word for _, word in sorted(pq)]
print(Solution().topKFrequent(["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], 2))