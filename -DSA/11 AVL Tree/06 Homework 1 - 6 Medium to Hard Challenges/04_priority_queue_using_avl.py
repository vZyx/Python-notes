'''
- Extend the node class to allow a value to have extra data item (e.g. use it for taks IDs)
- The node (priority) will have a list of tasks
- For efficiency, we add/remove from the back only to be O(1)
- Change insert function for this logic
- These are nice generic feature

- Build PriorityQueue based on that
- We use a single node per priority, and add its tasks to the list
- Deque just get a task from the list. If no more items, we just remove the node

- Design cons: the design assumes the prioirty class knows how STL is implemented.
- This is not good. But let's keep things simple here
'''


class Node:
    def __init__(self, val=None, attached_data = None, left=None, right=None):
        self.val = val                          # used to compare nodes
        if attached_data is None:
            self.data_list = []
        else:
            self.data_list = [attached_data]
        self.left = left
        self.right = right
        self.height = 0  # 0 for leaf

    def ch_height(self, node):  # child height
        if not node:
            return -1  # -1 for null
        return node.height  # 0 for leaf

    def update_height(self):  # call in end of insert function
        self.height = 1 + max(self.ch_height(self.left), self.ch_height(self.right))

    def balance_factor(self):
        return self.ch_height(self.left) - self.ch_height(self.right)

    def is_leaf(self):
        return not self.left and not self.right


class AVLTree:
    def __init__(self, value, attached_data = None):
        self.root = Node(value, attached_data)

    def _right_rotation(self, Q):
        print("right_rotation", Q.val)
        P = Q.left
        Q.left = P.right
        P.right = Q
        Q.update_height()
        P.update_height()
        return P

    def _left_rotation(self, P):
        print("left_rotation", P.val)
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
        elif node.balance_factor == -2:
            if node.right.balance_factor() == 1:
                node.right = self._right_rotation(node.right)

            node = self._left_rotation(node)

        return node

    def insert(self, val, attached_data = None):
        def process(current, val, attached_data):
            if val < current.val:
                if not current.left:
                    current.left = Node(val, attached_data)
                else:
                    # change left. update left as it might be balanced
                    current.left = process(current.left, val, attached_data)
            elif val > current.val:
                if not current.right:
                    current.right = Node(val, attached_data)
                else:
                    current.right = process(current.right, val, attached_data)
            else:   # found: add an extra element
                current.data_list.append(attached_data)

            current.update_height()
            return self.balance(current)

        self.root = process(self.root, val, attached_data)

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
        lst = self.inorder(current.root)
        # We can do the comparison without loop
        for idx in range(1, len(lst)):
            if lst[idx - 1] >= lst[idx]:
                return False
        return True


    ##################################

    def min_node(self, cur):
        while cur and cur.left:
            cur = cur.left
        return cur

    def delete(self, val):
        def process(current, val):
            if not current:
                return

            if val < current.val:  # Value on the left side
                # the left subtree will be changed. This can be left itself
                current.left = process(current.left, val)  # must link
                return current

            if val > current.val:  # Value on the right side
                current.right = process(current.right, val)
                return current

            # we found the node: we have 3 cases
            if current.is_leaf():  # case 1: leaf
                return None  # Just remove

            if not current.right:  # case 2: has left only
                current = current.left
            elif not current.left:  # case 2: has right only
                current = current.right
            else:
                # 2 children: Use successor
                mn = self.min_node(current.right)
                current.val = mn.val  # copy data
                current.right = process(current.right, mn.val)

            current.update_height()
            return self.balance(current)

        self.root = process(self.root, val)

    def max_node(self):
        cur = self.root
        while cur and cur.right:
            cur = cur.right
        return cur


class PriorityQueue:
    def __init__(self):
        self.avl = AVLTree(-1)
        self.items_cnt = 0

    def enqueue(self, task_id, priority):
        self.items_cnt += 1
        self.avl.insert(priority, attached_data=task_id)

    def dequeue(self):
        assert not self.empty()
        self.items_cnt -= 1

        bst_node = self.avl.max_node()
        # To keep dequeue O(logn) although node have several tasls
        # We will always push and pop from back in O(1)
        item = bst_node.data_list.pop()

        if not bst_node.data_list:  # no more elements
            self.avl.delete(bst_node.val)

        return item


    def empty(self):
        return self.items_cnt == 0


if __name__ == '__main__':

    tasks = PriorityQueue()

    tasks.enqueue(1131, 1)
    tasks.enqueue(3111, 3)
    tasks.enqueue(2211, 2)
    tasks.enqueue(3161, 3)

    print(tasks.dequeue())  # 3161
    print(tasks.dequeue())  # 3111

    tasks.enqueue(1535, 1)
    tasks.enqueue(2815, 2)
    tasks.enqueue(3845, 3)
    tasks.enqueue(3145, 3)

    while not tasks.empty():
        print(tasks.dequeue(), end=' ')
    # 3145 3845 2815 2211 1535 1131

