class OurDict:
    def __init__(self, table_size, limit_load_factor = 0.75):
        self.table_size = table_size
        self.table = [None] * table_size
        self.limit_load_factor = limit_load_factor
        self.total_elements = 0

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

        self.total_elements += 1
        self._rehash()

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
                self.total_elements -= 1
                # more efficient way? Swap with last and pop in O(1)
                return True

        return False

    def _rehash(self):
        cur_load_factor = float(self.total_elements) / self.table_size

        if cur_load_factor < self.limit_load_factor:
            return  # still we can add more

        print(f'Rehashing - new size will be: {2*self.table_size}')
        # double size
        dct = OurDict(2*self.table_size, self.limit_load_factor)

        for key_values in self.table:
            if key_values is None or len(key_values) == 0:
                continue

            for item in key_values:
                dct.add(item[0], item[1])

        # let's steal this object data
        self.table_size = dct.table_size
        self.table = dct.table
        self.total_elements = dct.total_elements







if __name__ == '__main__':
    dct = OurDict(10, 0.5)

    dct.add('Mostafa', 1)
    dct.add('Ziad', 2)
    dct.add('Ali', 3)
    dct.add('Amal', 4)
    dct.add('Hany', 5)
    dct.add('Belal', 6)
    dct.add('Safaa', 7)
    dct.add('Safa', 8)
    dct.add('Ashraf', 9)
    dct.add('Morad', 10)
    dct.add('John', 11)

