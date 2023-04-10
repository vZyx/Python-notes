

class MyDict(dict):
    def __setitem__(self, key, value):
        print(f'Update: {key} - {value}')
        if type(key) is float:
            print(f'\tDo Conversion to {key}')
            key = int(key)
        super().__setitem__(key, value)

    # https://docs.python.org/3/library/stdtypes.html#dict.update
    def update(self, dct_or_iterable = None, **kwargs):
        if dct_or_iterable is not None:
            kwargs.update(dct_or_iterable)

        for key, value in kwargs.items():
            self[key] = value

    def update_longer(self, dct_or_iterable = None, **kwargs):
        if isinstance(dct_or_iterable, dict):
            iterable = dct_or_iterable.items()
        else:
            iterable = dct_or_iterable

        if iterable is not None:
            for key, value in iterable:
                self[key] = value

        for key, value in kwargs.items():
            self[key] = value

    # https://docs.python.org/3/library/stdtypes.html#dict.setdefault
    def setdefault(self, key, value = None):
        if key in self:
            return self[key]

        self[key] = value
        return value

dct = MyDict()
dct[10.5] = 20
dct[(4, 5)] = 'Mostafa'
print (10.5 in dct)
print(dct)

exit(0)
dct = MyDict.fromkeys([1.5, 2.7])
dct[10.5] = 20
dct[(4, 5)] = 'Mostafa'

dct.update({'name': 30, 0.7: [1, 2, 3]})
dct.update(((7.5, 7),))
dct.update([[8.5, 8]])
dct.update(val=35)
dct.update([(9.5, 9)], hey = 12)
dct.update()
print(dct.setdefault(11.3, 'belal'))
print(dct.setdefault((4, 5), 'Ziad'))

print(dct)
# {1: None, 2: None, 10: 20, (4, 5): 'Mostafa', 'name': 30, 0: [1, 2, 3], 7: 7, 8: 8, 'val': 35, 'hey': 12, 9: 9, 11: 'belal'}

print(dct[0])   # [1, 2, 3]

#print(dct[9.5])   # KeyError: 9.5

