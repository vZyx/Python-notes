
class MyPair:
    def __init__(self, first, second):
        self.first = first
        self.second = second

    def __repr__(self):
        return f'({self.first}, {self.second})'

    def __add__(self, other):
        return MyPair(self.first  + other.first,
                      self.second + other.second)

    def __format__(self, format_spec):
        import time
        tm = time.localtime()
        return repr(self) + ' ' + time.strftime(format_spec, tm)
        # In practice: format_spec is whatever agreed then you parse it

if __name__ == '__main__':
    p = MyPair(2, 3)
    print(format(p))    # (2, 3) , default empty
    print(format(p, '%m-%d-%Y, %H:%M:%S'))
    # (2, 3) 02/28/2021, 17:21:07
