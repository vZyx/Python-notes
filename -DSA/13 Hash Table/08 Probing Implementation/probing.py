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

class OurDictPropbing:
    _DELETED_MARK = object()

    def __init__(self, table_size):
        self.table_size = table_size
        self.table = [None] * table_size
        self.total_elements = 0


    # Critical function - commonly wrongly implemented
    # Don't just return the first of: available or found
    # First make sure it is NOT found, before returning first valid idx

    def _find_idx(self, key):
        '''
        Find either:
        1- The elment exist: return (its idx, true)
        2- Don't exist: return the first available position, false for not found
        '''
        hkey = hash(key) % self.table_size
        first_available = None

        for step in range(self.table_size):
            item = self.table[hkey]
            if item is None or item == self._DELETED_MARK:
                if first_available is None:
                    first_available = hkey

                if item is None:
                    break   # We are done with the block

            elif item[0] == key:
                return hkey, True

            hkey = (hkey + 1) % self.table_size  # move 1 step (linear proping)

        # NOT found. Here is an insertion slot
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
        self.table[hkey] = [key, value]
        self.total_elements += not found

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


