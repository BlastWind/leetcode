from collections import defaultdict
from heapq import heappop, heappush
from typing import List


class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        # Brute force 1
        buildings = sorted(buildings)

        rightBorder = max(i for [_, i, _] in buildings)
        leftBorder = min(i for [i, _, _] in buildings)
        res = [0] * (rightBorder -leftBorder + 1)
        for (left,right, height) in buildings: 
            # examine all of the heights at this building
            for i in range(left, right):
                res[i-leftBorder] = max(res[i-leftBorder], height)

        prev = -1
        ret = []
        for i, num in enumerate(res): 
            if num != prev: 
                ret.append([i+ leftBorder, num])
            prev = num
        return ret

    def getSkyline2(self, buildings: List[List[int]]) -> List[List[int]]:
        # Collect and sort the unique positions of all the edges.
        positions = sorted(
            list(set([x for building in buildings for x in building[:2]])))

        # 'answer' for skyline key points
        answer = []

        # For each position, draw an imaginary vertical line.
        for position in positions:
            # current max height.
            max_height = 0

            # Iterate over all the buildings:
            for left, right, height in buildings:
                # Update 'max_height' if necessary.
                if left <= position < right:
                    max_height = max(max_height, height)

            # If its the first key point or the height changes,
            # we add [position, max_height] to 'answer'.
            if not answer or max_height != answer[-1][1]:
                answer.append([position, max_height])

        # Return 'answer' as the skyline.
        return answer

    def getSkyline3(self, buildings: List[List[int]]) -> List[List[int]]:
        # Collect and sort the unique positions of all the edges.
        buildings = sorted(buildings)
        leftToRightHeight = defaultdict(list)
        for left, right, height in buildings:
            leftToRightHeight[left].append([right, height])
        positions = list(set([x for building in buildings for x in building[:2]]))
        # {2: [9, 10], 3: [7, 15], 5: [12, 12]  }
        pq = []
        ans = []
        for pos in positions: 
            if pos in leftToRightHeight:
                for right, height in leftToRightHeight[pos]:
                    heappush(pq, (-height, right))
            while pq and pq[0][1] <= pos: 
                # tallest element is no longer in valid range
                heappop(pq)
            tallest = -pq[0][0] if pq else 0
            if not ans or tallest != ans[-1][1]:
                ans.append([pos, tallest])
        return ans

driver = Solution()
# expect [[0, 3], [5, 0]]
print(driver.getSkyline3([[2, 9, 10], [9, 12, 15]]))
