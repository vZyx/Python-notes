# https://leetcode.com/problems/validate-binary-search-tree/

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


class Solution(object):
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

    # the inorder traversal must be: 1) sorted 2) unique
    def isValidBST(self, current):
        lst = self.inorder(current)
        # We can do the comparison without loop
        for idx in range(1, len(lst)):
            if lst[idx-1] >= lst[idx]:
                return False
        return True


if __name__ == '__main__':
    tree = BinaryTree(50)
    tree.insert([20, 70, 15, 45, 60, 73, 35])



