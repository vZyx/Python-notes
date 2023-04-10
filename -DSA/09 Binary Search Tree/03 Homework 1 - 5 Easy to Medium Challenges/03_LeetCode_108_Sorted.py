# https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/

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
    def sortedArrayToBST(self, nums):
        def process(nums):
            if len(nums) == 0:
                return None
            mid = len(nums) // 2
            root = Node(nums[mid])
            root.left = process(nums[:mid])
            root.right = process(nums[mid + 1:])
            return root

        return process(nums)



if __name__ == '__main__':
    tree = BinaryTree(50)
    tree.insert([20, 70, 15, 45, 60, 73, 35])

