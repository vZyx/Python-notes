class Node:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BinaryTree:
    def __init__(self, value):
        self.root = Node(value)

    def preorder(self):
        import collections
        nodes_deque = collections.deque()

        def process(current):
            if not current:
                return

            nodes_deque.append(current.val)
            process(current.left)
            process(current.right)

        process(self.root)
        return nodes_deque

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
    One more time, we can keep the [mn, mx] execlusive range per node
    this clearly can tell us where the node should ne

    easy and direct O(n)!
    '''

    def get_tree_from_preorder(self, nodes_deque):  # O(n)
        def process(nodes_deque, mn, mx):
            def next_between(nodes_deque, mn, mx):
                if not nodes_deque:
                    return False
                return mn < nodes_deque[0] < mx

            if not nodes_deque:
                return None

            node = Node(nodes_deque.popleft())

            # if next node are my left, they must respect my min/max range
            if next_between(nodes_deque, mn, node.val):
                node.left = process(nodes_deque, mn, node.val)

            if next_between(nodes_deque, node.val, mx):
                node.right = process(nodes_deque, node.val, mx)

            return node

        tree = BinaryTree(None)
        tree.root = process(nodes_deque, float('-inf'), float('inf'))
        return tree


def test1():
    tree = BinaryTree(50)
    tree.insert([20, 70, 15, 45, 60, 73, 35])

    deq1 = tree.preorder()
    tree2 = tree.get_tree_from_preorder(deq1.copy())
    deq2 = tree2.preorder()

    assert deq1 == deq2


def test2():
    tree = BinaryTree(50)
    tree.insert([20, 60, 15, 45, 70,
                 35, 73, 14, 16, 36, 58])

    deq1 = tree.preorder()
    tree2 = tree.get_tree_from_preorder(deq1.copy())
    deq2 = tree2.preorder()

    assert deq1 == deq2


if __name__ == '__main__':
    test1()
    test2()
