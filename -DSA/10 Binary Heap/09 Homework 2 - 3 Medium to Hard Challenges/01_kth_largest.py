import heapq


class KthLargestProcessor:
    def __init__(self, k):
        self.k = k
        self.minHeap = []

    def next(self, number):
        if len(self.minHeap) < self.k:
            heapq.heappush(self.minHeap, number)
        elif number > self.minHeap[0]:	# top
            heapq.heappop(self.minHeap)
            heapq.heappush(self.minHeap, number)

        return self.minHeap[0]


if __name__ == "__main__":
    lst = [2, 17, 22, 10, 8, 37, 14,
           19, 7, 6, 5, 12, 25, 30]

    k = 4
    processor = KthLargestProcessor(k)

    for idx, val in enumerate(lst):
        ans = processor.next(val)
        print(idx, ans)

        right_answer = heapq.nlargest(k, lst[:idx+1])
        assert ans == right_answer[-1]

"""
0 2
1 2
2 2
3 2
4 8
5 10
6 14
7 17
8 17
9 17
10 17
11 17
12 19
13 22
"""
