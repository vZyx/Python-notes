
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

    # Trace the whole tree and add each word that is complete
    def get_all_strings(self):
        ans = []

        def traverse(trie, cur_str):
            if trie.is_leaf:
                ans.append(cur_str)

            for idx, node in enumerate(trie.child):
                if node is None:
                    continue
                letter = chr(ord('a') + idx)
                traverse(node, cur_str + letter)

        traverse(self, '')
        return ans




if __name__ == '__main__':

    root = Trie()

    root.insert("xyz")
    root.insert("abcd")
    root.insert("abf")
    root.insert("ab")
    root.insert("xyzwfe")

    print(root.get_all_strings())
    # ['ab', 'abcd', 'abf', 'xyz', 'xyzwfe']
