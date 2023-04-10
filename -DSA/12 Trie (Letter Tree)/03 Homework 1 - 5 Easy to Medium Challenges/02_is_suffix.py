
class Trie:
    def __init__(self):
        self.child = [None] * 26
        self.is_leaf = False

    def _to_idx(self, ch):
        # return 0 for 'a', 1 for 'b', ... 25 for 'z'
        return ord(ch) - ord('a')

    def insert(self, str):
        # by reversing a string, we can trivially check for suffixes!
        str = reversed(str)

        node = self

        for ch in str:
            cur = self._to_idx(ch)
            if node.child[cur] is None:
                node.child[cur] = Trie()
            node = node.child[cur]

        node.is_leaf = True

    def suffix_exist(self, str):
        str = reversed(str)

        node = self

        for ch in str:
            cur = self._to_idx(ch)
            if node.child[cur] is None:
                return False
            node = node.child[cur]

        return True


if __name__ == '__main__':

    root = Trie()

    root.insert("abcd")
    root.insert("xyz")

    print(root.suffix_exist("abc"))     # False
    print(root.suffix_exist("bcd"))     # True
    print(root.suffix_exist("xyz"))     # True
    print(root.suffix_exist("xy"))      # False
    print(root.suffix_exist("yz"))      # True
    print(root.suffix_exist("xyzxyz"))  # False

