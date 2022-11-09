class StockSpanner:

    def __init__(self):
        self.stack = [[inf, 0]]

    def next(self, price: int) -> int:
        idx = self.stack[-1][1] + 1

        while price >= self.stack[-1][0]:
            self.stack.pop(-1)

        span = idx - self.stack[-1][1]

        self.stack.append([price, idx])

        return span
# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)