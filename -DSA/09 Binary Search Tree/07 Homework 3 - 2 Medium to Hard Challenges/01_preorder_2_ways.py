class Node:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BinaryTree:
    def __init__(self, value):
        self.root = Node(value)

    def preorder(self):
        nodes_lst = []

        def process(current):
            if not current:
                return

            nodes_lst.append(current.val)
            process(current.left)
            process(current.right)

        process(self.root)
        return nodes_lst

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

    #################################
    '''
    Assume input is:  50 20 15 45 35 60 70 73
    Root is 50, but where is left and right?
    We know right must be greater than 50
    So Find the FIRST number > 50, which is 60
        left = 20 15 45 35
        right = 60 70 73

    Repeat and build recursively
    '''

    def get_tree_from_preorder(self, nodes_lst):  # O(n^2)
        def process(nodes_lst):
            if not nodes_lst:
                return None

            node = Node(nodes_lst[0])
            # find first index with value > root, if any
            split = None
            for idx in range(1, len(nodes_lst)):
                if nodes_lst[idx] > nodes_lst[0]:
                    split = idx
                    break

            if split is None:
                node.left = process(nodes_lst[1:])
            else:
                node.left = process(nodes_lst[1:split])
                node.right = process(nodes_lst[split:])

            return node

        tree = BinaryTree(None)
        tree.root = process(nodes_lst)
        return tree

    '''
    Can we make this code linear?
    Sure! Recall the next greater task from stack
    Observe here: we mainly need to get the next greater index in O(n) for every value
    This way we git rid of the loop to find the split

    Changing the recursion to have (start, end) indices in the list
    makes overall code O(n) 

    '''


def test1():
    tree = BinaryTree(50)
    tree.insert([20, 70, 15, 45, 60, 73, 35])

    lst1 = tree.preorder()
    tree2 = tree.get_tree_from_preorder(lst1.copy())
    lst2 = tree2.preorder()

    assert lst1 == lst2


def test2():
    tree = BinaryTree(50)
    tree.insert([20, 60, 15, 45, 70, 35, 73, 14, 16, 36, 58])

    lst1 = tree.preorder()
    tree2 = tree.get_tree_from_preorder(lst1.copy())
    lst2 = tree2.preorder()

    assert lst1 == lst2


if __name__ == '__main__':
    test1()
    test2()
