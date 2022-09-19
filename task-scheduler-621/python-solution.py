from heapq import heappop, heappush
from typing import List
# Intuition
# after each cycle, we will always be in shape to immediately execute the most frequent task
# if NO TASKS are cleared out, obviously, at the start of the next cycle, we will be in shape to execute the most frequent task
# if front task was cleared out, this means that the most frequent task is cleared out, but this means that in fact all tasks are cleared out
# if low freq task was cleared out, we still wait it out


class Solution:
	def leastInterval(self, tasks: List[str], n: int) -> int:
		freqTable = dict()
		for task in tasks:
			freqTable[task] = freqTable.get(task, 0) + 1
		count = 0
		pq = list()  # min heap
		for freq in freqTable.values():
			heappush(pq, -freq)

		while pq:
			temp = []
			for _ in range(n+1):  # elements per cycle is wait time + 1
				if pq:
					temp.append(heappop(pq))
			for freq in temp:
				if freq + 1 < 0:
					heappush(pq, freq + 1)
			count += len(temp) if not pq else n + 1
		return count

a = Solution()
print(a.leastInterval(["A","A","A","B","B","B"], 0))