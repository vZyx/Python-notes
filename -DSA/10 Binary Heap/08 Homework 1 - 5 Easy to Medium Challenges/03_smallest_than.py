
class MinHeap:
    def __init__(self, lst):
        self.array = lst
        self.size = len(lst)

        self._heapify()

    def _heapify(self):
        # Iterate from the first NON-leaf node
        for i in range(self.size//2 -1, -1, -1):
            self._heapify_down(i)

    def _left(self, node):
        p = 2 * node + 1
        if p >= self.size:
            return -1
        return p

    def _right(self, node):
        p = 2 * node + 2
        return -1 if p >= self.size else p

    def _parent(self, node):
        return -1 if node == 0 else (node - 1) // 2

    def _heapify_up(self, child_pos):  # stop when parent is smaller or no parent
        par_pos = self._parent(child_pos)
        if child_pos == 0 or self.array[par_pos] < self.array[child_pos]:
            return
        # swap
        self.array[child_pos], self.array[par_pos] = self.array[par_pos], self.array[child_pos]
        self._heapify_up(par_pos)

    def push(self, key):
        if self.size + 1 >= len(self.array):
            self.array.append(None)

        self.array[self.size] = key
        self.size += 1
        self._heapify_up(self.size - 1)

    def top(self):
        assert not self.empty()
        return self.array[0]

    def empty(self):
        return self.size == 0

    ########

    def _heapify_down(self, parent_pos): 	# O(logn)
        child_pos = self._left(parent_pos)
        right_child = self._right(parent_pos)

        if child_pos == -1: # no children
            return
        # is right smaller than left?
        if right_child != -1 and self.array[right_child] < self.array[child_pos]:
            child_pos = right_child

        if self.array[parent_pos] > self.array[child_pos]:
            self.array[parent_pos], self.array[child_pos] = self.array[child_pos], self.array[parent_pos]
            self._heapify_down(child_pos)

    def pop(self):  # remove the minimum element
        assert not self.empty()
        self.size -= 1
        result = self.array[0]
        self.array[0] = self.array[self.size]
        self._heapify_down(0)
        return result

    ########

    def smallest_than(self, value):
        lst = []

        def process(parent_pos):
            if parent_pos == -1 or self.array[parent_pos] >= value:
                return  # all this subtree is useless

            lst.append(self.array[parent_pos])

            process(self._left(parent_pos))
            process(self._right(parent_pos))

        process(0)
        return lst


if __name__ == "__main__":

    lst = [2, 17, 22, 10, 8, 37, 14,
           19, 7, 6, 5, 12, 25, 30]
    minHeap = MinHeap(lst)

    print(minHeap.smallest_than(10))
    # [2, 5, 7, 6, 8]


