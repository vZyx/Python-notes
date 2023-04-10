class Node:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        self.height = 0     # 0 for leaf
        self.count = 1      # Number of nodes in this-subtree

    def ch_height(self, node):  # child height
        if not node:
            return -1  # -1 for null
        return node.height  # 0 for leaf

    def ch_count(self, node):
        if not node:
            return 0
        return node.count

    def update_height(self):  # call in end of insert function
        self.height = 1 + max(self.ch_height(self.left), self.ch_height(self.right))
        self.count = 1 + self.ch_count(self.left) + self.ch_count(self.right)    # update how many nodes in this sub-tree

    def balance_factor(self):
        return self.ch_height(self.left) - self.ch_height(self.right)

    def is_leaf(self):
        return not self.left and not self.right


class AVLTree:
    def __init__(self, value):
        self.root = Node(value)

    def _right_rotation(self, Q):
        P = Q.left
        Q.left = P.right
        P.right = Q
        Q.update_height()
        P.update_height()
        return P

    def _left_rotation(self, P):
        Q = P.right
        P.right = Q.left
        Q.left = P
        P.update_height()
        Q.update_height()
        return Q

    def balance(self, node):
        if node.balance_factor() == 2:  # Left
            if node.left.balance_factor() == -1:  # Left Right
                node.left = self._left_rotation(node.left)  # To Left Left

            node = self._right_rotation(node)  # Balance Left Left

        elif node.balance_factor() == -2:
            if node.right.balance_factor() == 1:
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
            # Else - already exists

            current.update_height()
            current = self.balance(current)
            return current

        if not isinstance(val, list):
            val = [val]
        for item in val:
            # Update the root: it could change
            self.root = process(self.root, item)

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

    # Return the number of nodes that are > target
    # For efficiency, we maintain count variable in each node
    def upper_bound_count(self, val):
        def process(current, val):
            if not current:
                return 0

            if val < current.val:
                # If I will go to left then: root + right-subtree are > target
                sum = 1 + current.ch_count(current.right)
                return sum + process(current.left, val)

            return process(current.right, val)

        return process(self.root, val)



def count_inversions():
    lst = [10, 5, 8, 2, 12, 6]
    answers = [1, 1, 3, 0, 3]   # answers starting from 5

    tree = AVLTree(lst[0])

    total = 0
    for idx, val in enumerate(lst[1:]):
        inversions = tree.upper_bound_count(val)
        assert inversions == answers[idx]
        total += inversions
        tree.insert(val)

    assert total == 8




if __name__ == '__main__':
    count_inversions()
