
class Node:
    def __init__(self, val=None, parent=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        self.parent = parent


class BinaryTree:
    def __init__(self, value):
        self.root = Node(value)

    def insert(self, val):
        def process(current, val):
            if val < current.val:
                if not current.left:
                    current.left = Node(val, current)   # add parent
                else:
                    process(current.left, val)
            elif val > current.val:
                if not current.right:
                    current.right = Node(val, current)
                else:
                    process(current.right, val)
            # Elise - already exists

        if not isinstance(val, list):
            val = [val]
        for item in val:
            process(self.root, item)


    def min(self, cur):
        while cur and cur.left:
            cur = cur.left
        return cur.val

    def find_node(self, val):
        def process(current, val):
            if not current:
                return None
            if val == current.val:
                return current
            if val < current.val:
                return process(current.left, val)
            return process(current.right, val)

        return process(self.root, val)

    def successor(self, target):
        child = self.find_node(target)
        if not child:   # value is not in tree!
            return None

        if child.right:
            return self.min(child.right)
        if not child.parent:   # root
            return None

        parent = child.parent
        # Cancel chain of ancestors I am BIGGER than them
        while parent and parent.right == child:
            child, parent = parent, parent.parent

        if not parent:
            return None
        return parent.val


if __name__ == '__main__':
    tree = BinaryTree(50)
    lst = [20, 70, 15, 45, 60, 73, 35]
    tree.insert(lst)

    lst.append(50)
    lst.append(51)
    lst = sorted(lst)
    print(lst)

    for val in lst:
        print(val, tree.successor(val))
