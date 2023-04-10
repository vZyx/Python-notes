'''
One brute force is as follows:
    Try to make all possible changes for the given work
        That is for each letter, change it with one of the 2 letters
        Now, just check if this word exists or not

However, this is slow solution. To get it accepted consider:
1- Use dictionary not list to save a lot of memory
2- Use iterative code
3- Convert the string to list so that you don't keep creating new strings. Remember this trick

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

    def word_exist(self, str):
        node = self

        for cur in str:
            if cur not in node.child:
                return False
            node = node.child[cur]

        return node.is_leaf


class MagicDictionary(object):
    def __init__(self):
        self.root = Trie()

    def buildDict(self, dictionary):
        for word in dictionary:
            self.root.insert(word)

    def search(self, searchWord):
        # list is mutable - O(1) to change
        searchWord = list(searchWord)

        for idx, cur_letter in enumerate(searchWord):
            cpy_letter = cur_letter

            for char_idx in range(26):
                new_letter = chr(ord('a') + char_idx)

                if cpy_letter == new_letter:
                    continue    # we need 1 change

                searchWord[idx] = new_letter
                if self.root.word_exist(searchWord):
                    return True

            searchWord[idx] = cpy_letter

        return False





if __name__ == '__main__':
    dct = MagicDictionary()
    dct.buildDict(["hello", "leetcode"])

    print(dct.search('xello'))