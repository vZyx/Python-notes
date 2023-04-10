
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

    def get_all_matches(self, str, start_idx):  # O(L^2):
        node = self
        steps = 0
        ans = []

        for idx in range(start_idx, len(str)):  # O(L) in worst case
            steps += 1
            cur = self._to_idx(str[idx])
            if node.child[cur] is None:
                break
            node = node.child[cur]
            if node.is_leaf:
                ans.append(str[start_idx : start_idx + steps])  # O(L) to cut substr

        return ans


def list_substrs(long_str, queries_lst):
    # Reverse thinking using trie.
    trie = Trie()

    # O(QL): Add the queries themselves to the trie
    for word in queries_lst:
        trie.insert(word)

    # For the long_str, generate all its suffixes   long_str[idx:]
    # For each suffix, iterate over the trie and find all words you meet
    # These words are prefixes of this suffix ==> are sub-strings from original string
    ans = []
    # O(SL): observe, we won't iterate in the tree MORE than L steps
    for idx in range(len(long_str)):
        # To avoid generating a huge suffix that most of it maynot be used
        # let's process it using its idx
        sub_list = trie.get_all_matches(long_str, idx)
        ans.extend(sub_list)

    # total: O(QL + SL^2) vs previously O(QL + SS)
    return ans
    # There is an assumption here we have the queries offline
    # In practice, these queries might be streamed one by one
    # so no early access to them


if __name__ == '__main__':
    long_str = 'heyabcdtwxyw'
    queries_lst = ["xy", "ab", "t", "yz"]

    ans = list_substrs(long_str, queries_lst)

    print(ans)
    # ['xy', 'ab', 't']
