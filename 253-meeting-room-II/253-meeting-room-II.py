from heapq import heappop, heappush
from queue import PriorityQueue
from typing import List


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:

        intervals = sorted(intervals)
        ends = []

        for interval in intervals:
            start = interval[0]
            temp = []
            while ends:
                if start >= -ends[0]:  # negative because I want to use built in min heap as max heap
                    # extend room that ends the latest to end even later
                    heappop(ends)
                    heappush(ends, -interval[1])
                    break
                else:
                    temp.append(heappop(ends))
            else:
                heappush(ends, -interval[1])  # add new room
            for item in temp:
                heappush(ends, item)
        return len(ends)


driver = Solution()
print(driver.minMeetingRooms(
    [[7, 10], [2, 4], [7, 10], [2, 4], [7, 10], [2, 4]]))
