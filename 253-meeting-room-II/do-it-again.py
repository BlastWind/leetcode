from heapq import heappop, heappush
from queue import PriorityQueue
from typing import List


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        # enlist all end times into priority queue ()
        
        pq = []
        res = 0
        intervals = sorted(intervals)
        # traverse through all rooms:  
        for (start, end) in intervals:
            if len(pq) == 0: 
                pq = [-end]
                res += 1
                continue
            temp = []
            for _ in range(len(pq)): 
                longestMeetingRoom = -heappop(pq)
                if longestMeetingRoom <= start:
                    heappush(pq, -end)
                    break
                else: 
                    temp.append(-longestMeetingRoom)
            else: 
                # did not utilize an existing meeting room
                heappush(pq, -end)
                res += 1
            for t in temp: 
                heappush(pq, t)
        return res

driver = Solution()
print(driver.minMeetingRooms(
    [[7, 10], [2, 4]]))
