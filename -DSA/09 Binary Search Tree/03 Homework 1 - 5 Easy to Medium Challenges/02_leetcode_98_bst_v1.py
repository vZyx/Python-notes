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


'''
We can't just validate left and right. 
For exampole for tree
             5
        4               6
                    3           7
                    
6 is a valid BST, but 5 > 3, which is wrong

Idea: we need to make sure this value is proper with the parents too not just the child?
We can maintain the current [mn, mx] valid range per node during recursion
'''
class Solution(object):
    def isValidBST(self, current, mn=float('-inf'), mx=float('inf')):
        if not current:
            return True

        val, left, right = current.val, current.left, current.right

        if not (mn < val < mx):
            return False

        return self.isValidBST(left, mn, val) and self.isValidBST(right, val, mx)



if __name__ == '__main__':
    tree = BinaryTree(50)
    tree.insert([20, 70, 15, 45, 60, 73, 35])



