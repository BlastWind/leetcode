from bisect import insort_left
from cgitb import small
from collections import OrderedDict
from operator import index, indexOf
from typing import Dict, List, Tuple


class Solution:
    FAIL = 0

    def oddEvenJumps(self, arr: List[int]) -> int:
        # records end jump result. -1 for unset, 0 for fail, 1 for success
        memo = [[-1, -1] for _ in range(len(arr))]
        memo[-1][0] = 1
        memo[-1][1] = 1
        dic: Dict[int, int] = {}
        for i, ele in reversed(list(enumerate(arr))):
            if not ele in dic:
                dic[ele] = i
        traversedCounter = {ele: 0 for ele in arr}
        # map between i and the index of the ith largest jump in orig array
        ithLargestToIndInOrig = [i[0] for i in sorted(
            enumerate(arr), key=lambda x: x[1])]
        indInOrgToIthLargest = [0] * len(arr)
        for i, ele in enumerate(ithLargestToIndInOrig):
            indInOrgToIthLargest[ele] = i
        # also need a ithLargestToIndIn
        J = len(arr)
        for i, jump in reversed(list(enumerate(arr))):
            # odd, find the right section
            ind = dic[jump]
            iterated = traversedCounter[jump]
            if iterated >= 1:  # on at least the second time "jump" appeared in the orig arr
                if iterated % 2 == 1:
                    # taking the largest jump's even jump result
                    memo[i][0] = memo[ind][1]
                    memo[i][1] = memo[ind][0]
                else:
                    memo[i][0] = memo[ind][0]
                    memo[i][1] = memo[ind][1]
                traversedCounter[jump] += 1
                continue
            for j in range(indInOrgToIthLargest[ind]+1, J):
                if ithLargestToIndInOrig[j] > i:
                    memo[i][0] = memo[ithLargestToIndInOrig[j]][1]
                    break
                j += 1
            if memo[i][0] == -1:
                memo[i][0] = 0

            for j in range(indInOrgToIthLargest[ind]-1, -1, -1):
                if ithLargestToIndInOrig[j] > i:
                    # j is index in sorted arr, how to get the index in the original array?
                    while arr[ithLargestToIndInOrig[j]] == arr[ithLargestToIndInOrig[j-1]] and ithLargestToIndInOrig[j-1] > i:
                        j -= 1
                    memo[i][1] = memo[ithLargestToIndInOrig[j]][0]
                    break
                j -= 1
            if memo[i][1] == -1:
                memo[i][1] = 0
            traversedCounter[jump] += 1
        # if odd jump results in success, count it
        return len(list(filter(lambda x: x[0] > 0, memo)))
driver = Solution()
print(driver.oddEvenJumps([2, 3, 1, 1, 4, 2, 3, 1, 1, 4]))