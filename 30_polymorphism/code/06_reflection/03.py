
class MyPair:
    def __init__(self, first, second):
        self.first = first
        self.second = second

    def __repr__(self):
        return f'({self.first}, {self.second})'

    def __add__(self, other_pair):
        if not isinstance(other_pair, MyPair):
            return NotImplemented
        return MyPair(self.first + other_pair.first,
                      self.second + other_pair.second)

class SingleValue:
    def __init__(self, val):
        self.val = val

    def __radd__(self, mypair):
        if not isinstance(mypair, MyPair):
            return NotImplemented
        return MyPair(self.val + mypair.first,
                      self.val + mypair.second)

if __name__ == '__main__':
    p = MyPair(2, 3)
    s = SingleValue(10)
    p = p + s
    print(p)   # (12, 13)