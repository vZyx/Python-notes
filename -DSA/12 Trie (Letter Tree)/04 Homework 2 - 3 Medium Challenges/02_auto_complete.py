
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

    # Trace the whole tree starting from this node and add each word that is complete
    def get_all_strings(self, node, cur_str):
        ans = []

        def traverse(trie, cur_str):
            if trie.is_leaf:
                ans.append(cur_str)

            for idx, node in enumerate(trie.child):
                if node is None:
                    continue
                letter = chr(ord('a') + idx)
                traverse(node, cur_str + letter)

        traverse(node, cur_str)
        return ans

    # traverse the tree using this prefix
    # from this node, get all strings
    def autocomplete(self, str):
        node = self

        for ch in str:
            cur = self._to_idx(ch)
            if node.child[cur] is None:
                return []
            node = node.child[cur]

        return self.get_all_strings(node, str)



if __name__ == '__main__':

    root = Trie()

    root.insert("xyz")
    root.insert("abcd")
    root.insert("abf")
    root.insert("ab")
    root.insert("xyzwfe")

    print(root.autocomplete('a'))
    # ['ab', 'abcd', 'abf']

    print(root.autocomplete('xy'))
    # ['xyz', 'xyzwfe']
