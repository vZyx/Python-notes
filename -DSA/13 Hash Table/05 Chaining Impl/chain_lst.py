##################################################################################################
# Ignore these lines. I am just disabling hash randomization to administrate the example for you
import os
import sys

disable = True
hashseed = os.getenv('PYTHONHASHSEED')  # PYTHONHASHSEED responsible for randomization
if not disable and not hashseed:
    os.environ['PYTHONHASHSEED'] = '0'
    os.execv(sys.executable, [sys.executable] + sys.argv)


# If you got weird error, use disable = False
##################################################################################################

class OurDict:
    def __init__(self, table_size):
        self.table_size = table_size
        self.table = [None] * table_size

    def add(self, key, value):
        hkey = hash(key) % self.table_size  # [0, sz-1]
        new_item = [key, value]

        if self.table[hkey] is None:
            self.table[hkey] = [new_item]   # initial list of items
        else:
            items_equal_key = self.table[hkey]
            for item in items_equal_key:    # search
                if item[0] == key:          # key match
                    item[1] = value         # update
                    return

            self.table[hkey].append(new_item)

    def print(self):
        for key_values in self.table:
            if key_values is None or len(key_values) == 0:
                continue

            hkey = hash(key_values[0][0]) % self.table_size
            print(f'Key {hkey} - Pairs {key_values}')


    def get(self, key):
        hkey = hash(key) % self.table_size

        assert self.table[hkey] is not None, f'No such item {key}'

        items_equal_key = self.table[hkey]
        for item in items_equal_key:
            if item[0] == key:
                return item[1]

        assert False, f'No value attached with item {key}'

    def exists(self, key):
        hkey = hash(key) % self.table_size

        if self.table[hkey] is None:
            return False

        items_equal_key = self.table[hkey]
        for idx, item in enumerate(items_equal_key):
            if item[0] == key:
                return True

        return False

    def remove(self, key):
        hkey = hash(key) % self.table_size

        if self.table[hkey] is None:
            return False

        items_equal_key = self.table[hkey]
        for idx, item in enumerate(items_equal_key):
            if item[0] == key:
                items_equal_key.pop(idx)    # O(n) removal
                # more efficient way? Swap with last and pop in O(1)
                return True

        return False


if __name__ == '__main__':
    dct = OurDict(table_size=5)

    dct.add('Mostafa', 1)   # 2
    dct.add('Ziad', 2)      # 2
    dct.add('Ali', 5)       # 0
    dct.add('Amal', 6)      # 0
    dct.add('Hany', 8)      # 4
    dct.add('Belal', 10)    # 1
    dct.add('Safaa', 11)    # 3
    dct.add('Safa', 3)      # 2
    dct.add('Ashraf', 4)    # 2

    dct.add('Ziad', 555)    # reassign

    #dct.add('Saad', 9)  # 4

    dct.print()
    '''
    Key 0 - Pairs [['Ali', 5], ['Amal', 6]]
    Key 1 - Pairs [['Belal', 10]]
    Key 2 - Pairs [['Mostafa', 1], ['Ziad', 2], ['Safa', 3], ['Ashraf', 4]]
    Key 3 - Pairs [['Safaa', 11]]
    Key 4 - Pairs [['Saad', 9], ['Hany', 8]]
    '''

    print(dct.exists('Ziad'))  # True
    print(dct.exists('Saad'))  # False

    print(dct.get('Amal'))  # 6
    print(dct.get('Ziad'))  # 555
    #print(dct.get('Saad'))  # AssertionError

    print(dct.remove('Ziad'))   # True
    print(dct.remove('Ziad'))   # False
    print(dct.remove('Saad'))   # False

    # Optional homework: OOP this class with special methods
