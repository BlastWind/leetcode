# With a list of sorted meeting start and end times
# We can have one pointer at beginning of start times, one at beginning at ends times
# Iterate through start times, if current start time >= current end time, we can fit room (add 0, update end pointer)
# If start time < current end time, add 1, keep moving

# Is the current end time the tightest one used?
# Technically, no, draw the meeting time diagram for intervals [[1, 5], [4, 7], [7, 9]].
# For intervals[2] ([7, 9]), it will actually use the meeting that ended at 5 (intervals[0])
# Instead of intervals[2]'s end time, 7, which is a tighter bound

# But, this doesn't matter. If there are extra gap between 5 and 7 that a meeting could've utilized
# For a later meeting start time, like 8, it can just match the closer meeting time

# The only way it would matter if there is some meeting that can match the current end time but can't
# match the tightest end time. But, such a meeting must've came between current end time and the tighest
# end time, which means it started before the current meeting and thus would've matched away the
# current end time. Thus, there is no meeting that can match the current end time but can't match the tighest end time

from typing import List


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        starts = sorted([start for start, _ in intervals])
        ends = sorted([end for _, end in intervals])
        res = 0
        endPtr = 0
        for start in starts: 
            if start >= ends[endPtr]: # extends meeting
                endPtr += 1
            else: 
                res += 1            
        return res


driver = Solution()
print(driver.minMeetingRooms(
    [[7, 10], [2, 4], [7, 10], [2, 4], [7, 10], [2, 4]]))
