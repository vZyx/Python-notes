
class PriorityQueue:
    def __init__(self):
        self.array = []
        self.value = []
        self.size = 0

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
        if child_pos == 0 or self.array[par_pos] > self.array[child_pos]:
            return
        # swap
        self.array[child_pos], self.array[par_pos] = self.array[par_pos], self.array[child_pos]
        self.value[child_pos], self.value[par_pos] = self.value[par_pos], self.value[child_pos]
        self._heapify_up(par_pos)

    def _heapify_down(self, parent_pos): 	# O(logn)
        child_pos = self._left(parent_pos)
        right_child = self._right(parent_pos)

        if child_pos == -1: # no children
            return
        # is right bigger than left?
        if right_child != -1 and self.array[right_child] > self.array[child_pos]:
            child_pos = right_child

        if self.array[parent_pos] < self.array[child_pos]:
            self.array[parent_pos], self.array[child_pos] = self.array[child_pos], self.array[parent_pos]
            self.value[parent_pos], self.value[child_pos] = self.value[child_pos], self.value[parent_pos]
            self._heapify_down(child_pos)

    ########

    def enqueue(self, value, priority):
        if self.size + 1 >= len(self.array):
            self.array.append(None)
            self.value.append(None)

        self.array[self.size] = priority
        self.value[self.size] = value
        self.size += 1
        self._heapify_up(self.size - 1)

    def top(self):
        assert not self.empty()
        return self.value[0]

    def empty(self):
        return self.size == 0

    def dequeue(self):
        assert not self.empty()
        self.size -= 1
        result = self.value[0]
        self.array[0] = self.array[self.size]
        self.value[0] = self.value[self.size]
        self._heapify_down(0)
        return result


if __name__ == "__main__":

    tasks = PriorityQueue()

    tasks.enqueue(1131, 1)
    tasks.enqueue(3111, 3)
    tasks.enqueue(2211, 2)
    tasks.enqueue(3161, 3)
    tasks.enqueue(7761, 7)

    print(tasks.dequeue())
    print(tasks.dequeue())

    tasks.enqueue(1535, 1)
    tasks.enqueue(2815, 2)
    tasks.enqueue(3845, 3)
    tasks.enqueue(3145, 3)

    while not tasks.empty():
        print(tasks.dequeue(), end = ' ')


"""
7761
3111
3145 3161 3845 2815 2211 1131 1535 

Notice the heap during a heapify-down operation takes an element from bottom
and get it at root then push down.
This means if 2 elements are of same priority, their position in the tree can change randomly
hence we can't guarantee same priority elements to be in the same input order.
For further details: https://stackoverflow.com/questions/19336881/why-isnt-heapsort-stable

    "Stable sort algorithms sort elements such that
        order of repeating elements in the input
            is preserved in the output.

        So sorting 1 5 2 5 (assume 1 5A 2 5B) should be 1 2 5A 5B
            If the algorithm guarantee that = Stable sort algorithms
    "

Heap sort with its heapify-down will not guarantee that
Heap sort is unstable algorithm


 """
