class Node:
    def __init__(self, val=None,
                 left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def print_postorder(current):
    if not current:
        return
    print_postorder(current.left)
    print_postorder(current.right)
    print(current.val, end = ' ')


if __name__ == '__main__':

    plus = Node('+')
    plus.left = Node('2')
    plus.right = Node('3')

    div = Node('/')
    div.left = Node('8')
    div.right = Node('4')

    minus = Node('-')
    minus.left = Node('9')
    minus.right = div

    multiply = Node('*')
    multiply.left = plus
    multiply.right = minus

    print_postorder(multiply)

    # 2 3 + 9 8 4 / - *
