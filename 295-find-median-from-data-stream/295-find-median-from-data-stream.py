class MedianFinder:

    def __init__(self):
        self.arr = []

    def addNum(self, num: int) -> None:
        # binary search for first index whose value > num
        # insert num directly before this index
        if len(self.arr) == 0 or num >= self.arr[len(self.arr)-1]:
            self.arr.append(num)
            return
        lo, hi = 0, len(self.arr) - 1
        while lo < hi:
            mid = (lo + hi) // 2
            if self.arr[mid] < num:
                lo = mid + 1
            else:
                hi = mid
        self.arr = self.arr[:lo] + [num] + self.arr[lo:]

    def findMedian(self) -> float:
        
        if len(self.arr) == 1: return self.arr[0]
        if len(self.arr) % 2 == 1: 
            return self.arr[len(self.arr) // 2]
        return (self.arr[len(self.arr) // 2] + self.arr[len(self.arr) // 2 - 1]) / 2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()

obj = MedianFinder()
obj.addNum(1)
obj.addNum(2)
obj.addNum(30)

print(obj.findMedian())