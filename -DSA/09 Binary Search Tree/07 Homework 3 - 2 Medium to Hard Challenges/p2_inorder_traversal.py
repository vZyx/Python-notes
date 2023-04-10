class Node:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BinaryTree:
    def __init__(self, value):
        self.root = Node(value)

    def level_order_traversal(self):
        import collections
        nodes_queue = collections.deque()
        nodes_queue.append(self.root)

        level = 0
        traversal = collections.deque()

        while nodes_queue:
            sz = len(nodes_queue)
            for step in range(sz):
                cur = nodes_queue.popleft()

                traversal.append(cur.val)

                if cur.left:
                    nodes_queue.append(cur.left)
                if cur.right:
                    nodes_queue.append(cur.right)
            level += 1

        return traversal

    def insert(self, val):
        def process(current, val):
            if val < current.val:
                if not current.left:
                    current.left = Node(val)
                else:
                    process(current.left, val)
            elif val > current.val:
                if not current.right:
                    current.right = Node(val)
                else:
                    process(current.right, val)
            # Elise - already exists

        if not isinstance(val, list):
            val = [val]
        for item in val:
            process(self.root, item)

    '''
    Again, we can use the [mn, mx] idea
    Just do the normal level order traversal
    link the node to a parent if it is a valid range
    Trace and verify
    '''
    def get_tree_from_traversal(self, nodes_deque):
        def next_between(nodes_deque, mn, mx):
            return nodes_deque and mn < nodes_deque[0] < mx

        import collections
        nodes_queue = collections.deque()

        tree = BinaryTree(nodes_deque.popleft())
        nodes_queue.append([tree.root, float('-inf'), float('inf')])

        while nodes_queue:
            cur, mn, mx = nodes_queue.popleft()

            if next_between(nodes_deque, mn, cur.val):
                cur.left = Node(nodes_deque.popleft())
                nodes_queue.append([cur.left, mn, cur.val])

            if next_between(nodes_deque, cur.val, mx):
                cur.right = Node(nodes_deque.popleft())
                nodes_queue.append([cur.right, cur.val, mx])

        return tree


def test1():
    tree = BinaryTree(50)
    tree.insert([20, 70, 15, 45, 60, 73, 35])

    deq1 = tree.level_order_traversal()
    tree2 = tree.get_tree_from_traversal(deq1.copy())
    deq2 = tree2.level_order_traversal()

    assert deq1 == deq2


def test2():
    tree = BinaryTree(50)
    tree.insert([20, 60, 15, 45, 70,
                 35, 73, 14, 16, 36, 58])

    deq1 = tree.level_order_traversal()
    tree2 = tree.get_tree_from_traversal(deq1.copy())
    deq2 = tree2.level_order_traversal()

    assert deq1 == deq2


if __name__ == '__main__':
    test1()
    test2()
