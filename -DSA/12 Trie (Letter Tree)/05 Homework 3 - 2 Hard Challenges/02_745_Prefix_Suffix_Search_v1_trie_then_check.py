'''
The idea of this solution is simple

1- Build a trie with words
2- Given prefix, find all words with this prefix
3- Iterate on the list and check which word has this prefix

How to implement efficiently:
1- Many words in input is duplicate. Use set to filter them. Do that in reverse order to keep the biggest index
2- Modify the trie node to have list indices where we store the indices of all words with this prefix
3- Add simple function to trie that returns the list of indices of a given prefix
4- Find the first one with the requested suffix

How do we make sure we returnt the last index? Insert in the trie in reversed order the unique words
'''

'''
Another solution:
1- Build trie 1 with the strings
2- Build trie 2 with the reversed strings (suffix)

Use prefix to find the list of indices with this prefix [as we did]
Use suffix to find the list of indices with this suffix

Intersect the lists.

'''

class Trie:
    def __init__(self):
        self.child = [None] * 26
        self.is_leaf = False
        self.indices = []   # List of indices of prefixes inserted here

    def _to_idx(self, ch):
        # return 0 for 'a', 1 for 'b', ... 25 for 'z'
        return ord(ch) - ord('a')

    def insert(self, str, word_idx):
        node = self

        for ch in str:
            cur = self._to_idx(ch)
            if node.child[cur] is None:
                node.child[cur] = Trie()
            node = node.child[cur]
            node.indices.append(word_idx)

        node.is_leaf = True

    def word_exist(self, str):
        node = self

        for ch in str:
            cur = self._to_idx(ch)
            if node.child[cur] is None:
                return False
            node = node.child[cur]

        return node.is_leaf

    def get_positions(self, str):
        node = self

        for ch in str:
            cur = self._to_idx(ch)
            if node.child[cur] is None:
                return []
            node = node.child[cur]

        return node.indices     # always sorted if insertion is sorted indices


class WordFilter(object):

    def __init__(self, words):
        self.words = words
        self.prefix_trie = Trie()

        # Many words are duplicate. Let's only keep ones with high index
        words_st = set()
        for idx in range(len(words)-1, -1, -1):
            if words[idx] not in words_st:
                words_st.add(words[idx])
                self.prefix_trie.insert(words[idx], idx)

    def f(self, prefix, suffix):
        pre_list = self.prefix_trie.get_positions(prefix)   # sorted reversely

        for idx in pre_list:
            if self.words[idx].endswith(suffix):
                return idx

        return -1





if __name__ == '__main__':
    root = Trie()
