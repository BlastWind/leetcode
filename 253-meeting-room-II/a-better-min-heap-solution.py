# Breaking news: When we're looking for a room to extends:
# If even the room with the earliest end time can't extend, then we create a new one

# No need to use a max heap and do a bunch of complicated temp = [] pushing

from heapq import heappop, heappush, heapreplace
from typing import List


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:

        intervals = sorted(intervals)
        ends = []

        for interval in intervals:
            start, end = interval
            if ends and start >= ends[0]:
                heapreplace(ends, end)
            else:
                heappush(ends, end)
        return len(ends)


driver = Solution()
print(driver.minMeetingRooms(
    [[7, 10], [2, 4], [7, 10], [2, 4], [7, 10], [2, 4]]))
