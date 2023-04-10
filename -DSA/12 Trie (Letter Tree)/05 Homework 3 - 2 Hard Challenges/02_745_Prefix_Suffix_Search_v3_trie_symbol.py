# https://leetcode.com/problems/prefix-and-suffix-search

class Trie:
    def __init__(self):
        self.child = {}
        self.idx = -1

    def insert(self, str, idx):
        node = self

        for cur in str:
            if cur not in node.child:
                node.child[cur] = Trie()
            node = node.child[cur]
            if node.idx == -1:  # If exist, don't override to keep the last index
                node.idx = idx

    def get_idx(self, str):
        node = self

        for cur in str:
            if cur not in node.child:
                return -1
            node = node.child[cur]

        return node.idx


class WordFilter(object):
    def __init__(self, words):
        self.trie = Trie()

        def add_word_prefix_suffix_combinations(word, word_idx):
            # Generate all pairs of suffix/prefix
            # But, trie already generates all prefixes, so generate suffixes + one prefix
            # Use unique symbol to differentiate suffix from prefix (otherwise a word is unclear)
            # As we create more words (n^2), this solution needs more memory
            # But it queries in O(L)
            # See editorial
            for idx in range(len(word)):
                suffix = word[idx:]
                new_word = suffix + '$' + word
                self.trie.insert(new_word, word_idx)

        words_st = set()    # Filter duplicate
        for idx in range(len(words)-1, -1, -1): # go backward
            if words[idx] not in words_st:
                words_st.add(words[idx])
                add_word_prefix_suffix_combinations(words[idx], idx)

    def f(self, prefix, suffix):
        new_word = suffix + "$" + prefix
        return self.trie.get_idx(new_word)


if __name__ == '__main__':
    root = Trie()
