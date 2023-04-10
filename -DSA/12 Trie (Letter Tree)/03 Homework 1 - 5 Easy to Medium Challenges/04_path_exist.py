
class Trie:
    def __init__(self):
        # The major change: instead of letter on edge, it will be a string
        # Let's use a dictionary
        self.child = {}
        self.is_leaf = False

    def insert(self, path_lst, idx = 0):
        if idx == len(path_lst):
            self.is_leaf = True
        else:
            cur = path_lst[idx]
            if not cur in self.child:
                self.child[cur] = Trie()
            self.child[cur].insert(path_lst, idx + 1)

    def subpath_exist(self, path_lst, idx = 0):
        if idx == len(path_lst):
            return True

        cur = path_lst[idx]
        if not cur in self.child:
            return False

        return self.child[cur].subpath_exist(path_lst, idx + 1)


if __name__ == '__main__':


    root = Trie()

    root.insert(["home", "software", "eclipse"])
    root.insert(["home", "software", "eclipse", "bin"])
    root.insert(["home", "installed", "gnu"])
    root.insert(["user", "mostafa", "tmp"])

    print(root.subpath_exist(["user", "mostafa", "tmp"]))   # True
    print(root.subpath_exist(["user", "mostafa"]))          # True
    print(root.subpath_exist(["user"]))                     # True
    print(root.subpath_exist(["user", "most"]))             # False
    print(root.subpath_exist(["user", "NOT"]))              # False
