
class MyPair:
    def __init__(self, first, second):
        self.first = first
        self.second = second

    def __add__(self, other):
        if not isinstance(other, MyPair):
            return NotImplemented
        return MyPair(self.first+other.first,
                      self.second+other.second)


class SingleValue:
    def __init__(self, val):
        self.val = val

if __name__ == '__main__':
    p = MyPair(2, 3)
    s = SingleValue(10)
    p = p + s
    # TypeError: unsupported operand type(s) for +:
    # 'MyPair' and 'SingleValue'