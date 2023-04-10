# https://leetcode.com/problems/search-in-a-binary-search-tree/

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
    def searchBST(self, current, val):
        while current:
            if val == current.val:
                return current
            if val < current.val:
                current = current.left
            else:
                current = current.right

        return None



if __name__ == '__main__':
    tree = BinaryTree(50)
    tree.insert([20, 70, 15, 45, 60, 73, 35])

