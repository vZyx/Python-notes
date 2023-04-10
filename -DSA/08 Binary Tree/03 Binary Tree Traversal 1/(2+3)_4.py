class Node:
    def __init__(self, val=None,
                 left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


if __name__ == '__main__':
    plus = Node('+')
    node2 = Node('2')
    node3 = Node('3')
    plus.left = node2
    plus.right = node3

    # Build/connect root to + *
    multiply = Node('*')
    node4 = Node('4')

    multiply.left = plus
    multiply.right = node4
