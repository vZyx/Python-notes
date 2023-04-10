class Node:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BinaryTree:
    def __init__(self, value):
        self.root = Node(value)

    def add(self, values_lst, direction_lst):
        assert len(values_lst) == len(direction_lst)

        current = self.root
        # iterate on the path, all necessary nodes
        for i, val in enumerate(values_lst):
            if direction_lst[i] == 'L':
                if not current.left:
                    current.left = Node(values_lst[i])
                else:
                    assert current.left.val == values_lst[i]
                current = current.left
            else:
                if not current.right:
                    current.right = Node(values_lst[i])
                else:
                    assert current.right.val == values_lst[i]
                current = current.right

    #######################################

    def level_order_traversal_normal(self):
        import collections
        nodes_queue = collections.deque()
        nodes_queue.append(self.root)
        level = 0

        while nodes_queue:
            print(f'\nLevel {level}: ', end='')
            sz = len(nodes_queue)
            for step in range(sz):
                cur = nodes_queue.popleft()

                print(cur.val, end=' ')

                if cur.left:
                    nodes_queue.append(cur.left)
                if cur.right:
                    nodes_queue.append(cur.right)
            level += 1

    def level_order_traversal_sorted(self):
        import heapq
        # we must use 2 seperate heaps.
        # You can't keep inserting in the active heap as data is sorted
        nodes_heap_cur = [(self.root.val, self.root)]
        nodes_heap_next = []
        level = 0

        while nodes_heap_cur:
            print(f'\nLevel {level}: ', end='')
            while nodes_heap_cur:
                val, cur = heapq.heappop(nodes_heap_cur)

                print(val, end=' ')

                if cur.left:
                    heapq.heappush(nodes_heap_next, (cur.left.val, cur.left))
                if cur.right:
                    heapq.heappush(nodes_heap_next, (cur.right.val, cur.right))
            level += 1
            nodes_heap_cur, nodes_heap_next = nodes_heap_next, nodes_heap_cur


if __name__ == '__main__':
    tree = BinaryTree(1)
    tree.add([20, 50, 8], ['L', 'L', 'L'])
    tree.add([20, 50, 17], ['L', 'L', 'R'])
    tree.add([20, 40, 10], ['L', 'R', 'L'])
    tree.add([20, 40, 11], ['L', 'R', 'R'])

    tree.add([90, 60, 88], ['R', 'L', 'L'])
    tree.add([90, 60, 13], ['R', 'L', 'R'])
    tree.add([90, 7, 95], ['R', 'R', 'L'])
    tree.add([90, 7, 15], ['R', 'R', 'R'])

    #tree.level_order_traversal_normal()
    tree.level_order_traversal_sorted()

"""
Normal:
Level 0: 1 
Level 1: 20 90 
Level 2: 50 40 60 7 
Level 3: 8 17 10 11 88 13 95 15 

Sorted per level
Level 0: 1 
Level 1: 20 90 
Level 2: 7 40 50 60 
Level 3: 8 10 11 13 15 17 88 95 
"""

