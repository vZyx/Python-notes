class Node:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        self.height = 0  # 0 for leaf

    def ch_height(self, node):  # child height
        if not node:
            return -1  # -1 for null
        return node.height  # 0 for leaf

    def update_height(self):  # call in end of insert function
        return 1 + max(self.ch_height(self.left), self.ch_height(self.right))

    def balance_factor(self):
        return self.ch_height(self.left) - self.ch_height(self.right)

    def is_leaf(self):
        return not self.left and not self.right


class AVLTree:
    def __init__(self, value):
        self.root = Node(value)

    def _right_rotation(self, Q):
        print("right_rotation", Q.val)
        P = Q.left
        Q.left = P.right
        P.right = Q
        Q.update_height()
        P.update_height()
        return P

    def _left_rotation(self, P):
        print("left_rotation", P.val)
        Q = P.right
        P.right = Q.left
        Q.left = P
        P.update_height()
        Q.update_height()
        return Q

    def balance(self, node):
        if node.balance_factor() == 2:  # Left
            if node.left.balance_factor == -1:  # Left Right
                node.left = self._left_rotation(node.left)  # To Left Left

            node = self._right_rotation(node)  # Balance Left Left
        elif node.balance_factor == -2:
            if node.right.balance_factor == 1:
                node.right = self._right_rotation(node.right)

            node = self._left_rotation(node)

        return node

    def insert(self, val):
        def process(current, val):
            if val < current.val:
                if not current.left:
                    current.left = Node(val)
                else:
                    # change left. update left as it might be balanced
                    current.left = process(current.left, val)
            elif val > current.val:
                if not current.right:
                    current.right = Node(val)
                else:
                    current.right = process(current.right, val)
            # Elise - already exists

            current.update_height()
            return self.balance(current)

        if not isinstance(val, list):
            val = [val]
        for item in val:
            process(self.root, item)

    def inorder(self, current):
        def process(current):
            if not current:
                return
            process(current.left)
            lst.append(current.val)
            process(current.right)

        lst = []
        process(current)
        return lst

    def lower_bound(self, val):
        def process(current, val):
            if not current:
                return None

            if val <= current.val:
                # This branch MUST have the lower bound

                # Can we find a righter lower bound?
                ans = process(current.left, val)
                if ans is not None:
                    return ans
                return current.val  # nothing tighter

            # Let's see in the right tree
            return process(current.right, val)

        return process(self.root, val)


def test():
    lst = [2, 10, 5, 20, 15, 50, 70, 13, 40 ]

    tree = AVLTree(lst[0])

    for val in lst[1:]:
        tree.insert(lst)


    lst = sorted(lst)

    for idx, val in enumerate(lst):
        assert val == tree.lower_bound(val)

    for idx, val in enumerate(lst[:-1]):
        assert lst[idx+1] == tree.lower_bound(val+1)


if __name__ == '__main__':
    test()
