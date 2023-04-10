# https://leetcode.com/problems/kth-smallest-element-in-a-bst/

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

# The idea is to keep doing inorder traversal in the tree
# but maintain &k to know if you find it
# Order is O(n)
# The interesting inside idea is doing this partial inorder traversal
# 
# Another way: If the tree has for each node count for how many nodes in its tree
# we can get answer in O(h)
class Solution(object):
    def kthSmallest(self, root, k):
        def inorder(root, k):
            if k <= 0:
                return -1

            if not root:
                return k

            k = inorder(root.left, k)

            if k == 1:
                self.answer = root.val
                return 0

            k = inorder(root.right, k - 1)
            return k

        self.answer = None
        inorder(root, k)
        return self.answer



if __name__ == '__main__':
    tree = BinaryTree(50)
    tree.insert([20, 70, 15, 45, 60, 73, 35])

