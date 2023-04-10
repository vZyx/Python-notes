
class Node:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BinaryTree:
    def __init__(self, value):
        self.root = Node(value)

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

    def successor_queries(self, deque):
        traversal, answers = [], []

        def process(current):
            if not current or not deque:
                return

            if deque[0] < current.val:  # Don't go left if it doesn't help
                process(current.left)

            if deque and traversal and traversal[-1] == deque[0]:
                answers.append((deque[0], current.val))
                deque.popleft()

            traversal.append(current.val)  # normal traversal adding

            # Observe >= not just >: If target equal the cur data
            #       and we have right, then successor on right
            # Trace the root (e.g. 50)
            if deque and deque[0] >= current.val:
                process(current.right)

        process(self.root)
        return answers



if __name__ == '__main__':

    tree = BinaryTree(50)
    lst = [20, 70, 15, 45, 60, 73, 35]
    tree.insert(lst)

    lst.append(50)
    lst = sorted(lst)

    import collections
    nodes_queue = collections.deque()

    for val in lst:
        nodes_queue.append(val)

    print(tree.successor_queries(nodes_queue))
    # [(15, 20), (20, 35), (35, 45), (45, 50),
    # (50, 60), (60, 70), (70, 73)]
