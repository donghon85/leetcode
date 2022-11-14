from sortedcontainers import SortedList


class MedianFinder:

    def __init__(self):
        self.stack = SortedList()

    def addNum(self, num: int) -> None:
        self.stack.add(num)

    def findMedian(self) -> float:
        n = len(self.stack)
        share = n // 2
        if n % 2 == 0:  # even
            return (self.stack[share] + self.stack[share - 1]) / 2
        else:  # odd
            return self.stack[share]

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()