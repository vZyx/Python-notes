
class Trie:
    def __init__(self):
        self.child = [None] * 26
        self.is_leaf = False

    def _to_idx(self, ch):
        # return 0 for 'a', 1 for 'b', ... 25 for 'z'
        return ord(ch) - ord('a')

    def insert(self, str):
        node = self

        for ch in str:
            cur = self._to_idx(ch)
            if node.child[cur] is None:
                node.child[cur] = Trie()
            node = node.child[cur]

        node.is_leaf = True

    def word_exist(self, str):
        node = self

        for ch in str:
            cur = self._to_idx(ch)
            if node.child[cur] is None:
                return False
            node = node.child[cur]

        return node.is_leaf

    def prefix_exist(self, str):
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
    root.insert("abf")
    root.insert("xn")
    root.insert("ab")
    root.insert("bcd")

    print(root.word_exist("xyz"))
    print(root.word_exist("xy"))
    print(root.prefix_exist("xy"))

