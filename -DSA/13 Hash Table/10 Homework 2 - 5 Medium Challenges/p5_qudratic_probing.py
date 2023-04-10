class OurDictPropbing:
    _DELETED_MARK = object()

    def __init__(self, table_size, limit_load_factor = 0.75):
        self.table_size = table_size
        self.table = [None] * table_size
        self.limit_load_factor = limit_load_factor
        self.total_elements = 0


    def _find_idx(self, key):
        # When to stop?
        # One might stop when he performs table_size steps
        # my impression: we better stop when we cycle back to same index
        #
        # Computationally, we can see that we can fail to add in both cases
        # ALTHOUGH there are still free elements!
        # This never happens in linear probing
        #
        # If we failed to add: then do rehashing and try again
        # 	which will typically works well (or do rehashing again)		 *

        hkey = hash(key) % self.table_size
        original_hkey = hkey
        first_available = None

        # bug fixed. Step must start with 1, so that step*step be something new!
        for step in range(1, self.table_size+1):
            item = self.table[hkey]
            if item is None or item == self._DELETED_MARK:
                if first_available is None:
                    first_available = hkey

                if item is None:
                    break   # We are done with the block

            elif item[0] == key:
                return hkey, True

            hkey = (original_hkey + step * step) % self.table_size  # quadratic proping

            if hkey == original_hkey:
                break   # cycle to the first index

        # Caution: now first_available CAN be NONE, even though there are empty slots in the array
        return first_available, False

    def print(self):
        for idx, item in enumerate(self.table):
            print(idx, end=': ')

            if item is None:
                print('E')
            elif item == self._DELETED_MARK:
                print('D')
            else:
                print(item)

        print('*******************')

    def add(self, key, value):
        assert self.total_elements < self.table_size, 'Table is FULL'
        hkey, found = self._find_idx(key)

        if hkey is None:    # we can't add
            self._rehash()
            return self.add(key, value) # let's try again

        self.table[hkey] = [key, value]

        if not found:
            self.total_elements += 1
            self._rehash()

    def get(self, key):
        hkey, found = self._find_idx(key)
        assert found, f'No such item {key}'
        return self.table[hkey][1]

    def exists(self, key):
        hkey, found = self._find_idx(key)
        return found

    def remove(self, key):
        hkey, found = self._find_idx(key)
        if found:
            self.table[hkey] = self._DELETED_MARK
            self.total_elements -= 1
        return found

    def _rehash(self):
        cur_load_factor = float(self.total_elements) / self.table_size

        if cur_load_factor < self.limit_load_factor:
            return  # still we can add more

        print(f'Rehashing - new size will be: {2*self.table_size}')
        # double size
        dct = OurDictPropbing(2*self.table_size, self.limit_load_factor)

        for idx, item in enumerate(self.table):
            if item is None or item == self._DELETED_MARK:
                continue
            else:
                dct.add(item[0], item[1])

        # let's steal this object data
        self.table_size = dct.table_size
        self.table = dct.table
        self.total_elements = dct.total_elements


if __name__ == '__main__':

    dct = OurDictPropbing(table_size=9)

    dct.add('Mostafa', 1)
    dct.add('Ziad', 2)
    dct.add('Ali', 5)
    dct.add('Belal', 10)
    dct.add('Ashraf', 4)
    dct.add('Ziad', 555)    # reassign

    dct.print()
    '''
    0: ['Belal', 10]
    1: ['Ashraf', 4]
    2: E
    3: ['Ziad', 555]
    4: E
    5: E
    6: E
    7: ['Mostafa', 1]
    8: ['Ali', 5]
    '''

    dct.remove('Belal')
    dct.remove('Ali')
    dct.print()
    '''
    0: D
    1: ['Ashraf', 4]
    2: E
    3: ['Ziad', 555]
    4: E
    5: E
    6: E
    7: ['Mostafa', 1]
    8: D
    '''

    dct.add('wert', 75)
    dct.print()
    '''
    0: D
    1: ['Ashraf', 4]
    2: E
    3: ['Ziad', 555]
    4: E
    5: E
    6: E
    7: ['Mostafa', 1]
    8: ['wert', 75]
    '''


