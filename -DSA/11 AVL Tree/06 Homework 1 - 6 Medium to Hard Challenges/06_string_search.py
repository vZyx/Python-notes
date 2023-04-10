class Node:
    def __init__(self, val=None, is_full_word = True, left=None, right=None):
        self.val = val
        self.is_full_word = is_full_word
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
    def __init__(self, value, is_full_word):
        self.root = Node(value, is_full_word)

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
        if node.balance_factor() == 2:              # Left
            if node.left.balance_factor() == -1:    # Left Right
                node.left = self._left_rotation(node.left)  # To Left Left

            node = self._right_rotation(node)       # Balance Left Left
        elif node.balance_factor == -2:
            if node.right.balance_factor() == 1:
                node.right = self._right_rotation(node.right)

            node = self._left_rotation(node)

        return node

    def insert(self, val, is_full_word):	# O(L logn) where L is word length
        def process(current, val, is_full_word):
            if val < current.val:
                if not current.left:
                    current.left = Node(val, is_full_word)
                else:
                    # ** change left. update left as it might be balanced
                    current.left = process(current.left, val, is_full_word)
            elif val > current.val:
                if not current.right:
                    current.right = Node(val, is_full_word)
                else:
                    current.right = process(current.right, val, is_full_word)
            elif is_full_word:
                # if existed before but this is full_word, mark it
                current.is_full_word = 1

            current.update_height()
            return self.balance(current)

        self.root = process(self.root, val, is_full_word)

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

    def insert_string(self, target): 	# O(N^2 + L N LogN)
        # Idea is to insert all the possible prefixes and add to AVL
        # Mark which is prefix and which is full word
        if target == "":
            return

        cur = ''
        for i in range(len(target)):	
            cur += target[i]    # this line causes O(n) in python - O(1) in C++
            # If it is last index, self is the original full word
            self.insert(cur, i == len(target) - 1)	# O(L logN)

    def search_word_status(self, val):
        # return -1 if not found or the is_full_word status (1, 0)
        def process(current, val):
            if not current:
                return -1   # not found

            if current.val == val:
                return current.is_full_word

            if val < current.val:
                return process(current.left, val)

            return process(current.right, val)

        return process(self.root, val)

    def word_exist(self, target):
        return self.search_word_status(target) == 1

    def prefix_exist(self, target):
        return self.search_word_status(target) != -1    # e.g. 0 or 1


if __name__ == '__main__':
    tree = AVLTree("", True)

    tree.insert_string("abcd")
    tree.insert_string("xyz")

    print(tree.word_exist("abcd"))      # True
    print(tree.word_exist("ab"))        # False
    print(tree.prefix_exist("abcd"))    # True
    print(tree.prefix_exist("ab"))      # True

    tree.insert_string("ab")

    print(tree.word_exist("ab"))        # True
    print(tree.word_exist("cd"))        # False
    print(tree.word_exist("abcde"))     # False
