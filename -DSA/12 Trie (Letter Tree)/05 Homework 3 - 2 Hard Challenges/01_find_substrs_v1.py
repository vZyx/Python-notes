
class Trie:
    def __init__(self):
        MAX_CHAR = 26
        self.child = [None] * MAX_CHAR
        self.is_leaf = False

    def _to_idx(self, ch):
        # return 0 for 'a', 1 for 'b', ... 25 for 'z'
        return ord(ch) - ord('a')

    def insert(self, str, idx = 0):
        if idx == len(str):
            self.is_leaf = True
        else:
            cur = self._to_idx(str[idx])
            if self.child[cur] is None:
                self.child[cur] = Trie()
            self.child[cur].insert(str, idx + 1)

    def prefix_exist(self, str, idx = 0):
        if idx == len(str):
            return True

        cur = self._to_idx(str[idx])
        if self.child[cur] is None:
            return False	# such path don't exist

        return self.child[cur].prefix_exist(str, idx + 1)


def list_substrs(long_str, queries_lst):
    trie = Trie()

    # Generate all suffixes and add: O(S^2): S string length
    for idx in range(len(long_str)):
        suffix = long_str[idx:]
        trie.insert(suffix)

    # O(QL)	queries * string length
    ans = []
    for word in queries_lst:
        if trie.prefix_exist(word):
            ans.append(word)

    return ans


if __name__ == '__main__':
    long_str = 'heyabcdtwxyw'
    queries_lst = ["xy", "ab", "t", "yz"]
    ans = list_substrs(long_str, queries_lst)
    print(ans)
    # ['xy', 'ab', 't']
