
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

    def first_word_prefix(self, str):
        node = self

        for idx, ch in enumerate(str):
            cur = self._to_idx(ch)
            if node.child[cur] is None:
                break   # not found

            # Does this child marked as word? we forund a prefix that is a word
            if node.child[cur].is_leaf:
                return str[:idx+1]
            node = node.child[cur]

        return None




if __name__ == '__main__':
    root = Trie()

    root.insert("xyz")
    root.insert("xyzwfe")

    print(root.first_word_prefix("xy"))     # None
    print(root.first_word_prefix("xyz"))    # xyz
    print(root.first_word_prefix("xyzw"))   # xyz
    print(root.first_word_prefix("xyzH"))   # xyz

    root.insert("x")
    print(root.first_word_prefix("xy"))     # x
    print(root.first_word_prefix("xyz"))    # x

