'''
The idea is simple, but need careful coding

Traverse the trie and have allowed_changes counter
Now either try to change a letter and decrease the allowed_changes or not if there is a match
'''

class Trie:
    def __init__(self):
        self.child = {}
        self.is_leaf = False

    def insert(self, str):
        node = self

        for cur in str:
            if cur not in node.child:
                node.child[cur] = Trie()
            node = node.child[cur]

        node.is_leaf = True

    # generic allow any kind o changes
    def word_exist_changes(self, str, allowed_changes=1, idx=0):
        if idx == len(str):     # if done make sure changes are finished
            return allowed_changes == 0 and self.is_leaf

        if str[idx] in self.child:  # this letter already exist. No changes
            if self.child[str[idx]].word_exist_changes(str, allowed_changes, idx + 1):
                return True     # we managed to find a solution

        # Let's try to do a change, but can we?
        if allowed_changes == 0:
            return False

        # try to change using each OTHER letters in this tree
        for letter in self.child:
            if letter != str[idx]:
                if self.child[letter].word_exist_changes(str, allowed_changes - 1, idx + 1):
                    return True

        return False


class MagicDictionary(object):
    def __init__(self):
        self.root = Trie()

    def buildDict(self, dictionary):
        for word in dictionary:
            self.root.insert(word)

    def search(self, searchWord):
        return self.root.word_exist_changes(searchWord, 1)





if __name__ == '__main__':
    dct = MagicDictionary()
    dct.buildDict(["hello", "leetcode"])

    print(dct.search('xello'))