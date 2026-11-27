import heapq


class RunningMedian:
    def __init__(self):
        self.low = []
        self.high = []

    def add_num(self, num: int) -> None:
        heapq.heappush(self.low, -num)
        if self.low and self.high and (-self.low[0] > self.high[0]):
            heapq.heappush(self.high, -heapq.heappop(self.low))
        if len(self.low) > len(self.high) + 1:
            heapq.heappush(self.high, -heapq.heappop(self.low))
        elif len(self.high) > len(self.low):
            heapq.heappush(self.low, -heapq.heappop(self.high))

    def get_median(self) -> float:
        if len(self.low) > len(self.high):
            return float(-self.low[0])
        return (-self.low[0] + self.high[0]) / 2.0


if __name__ == "__main__":
    stream = [5, 15, 1, 3, 2, 8, 7, 9, 10, 6, 11, 4]
    rm = RunningMedian()
    for val in stream:
        rm.add_num(val)
        print(f"Added {val:2d} -> Median: {rm.get_median():.1f}")