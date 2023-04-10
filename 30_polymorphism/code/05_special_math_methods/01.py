
class MyPair:
    def __init__(self, first, second):
        self.first = first
        self.second = second

    def __repr__(self):
        return f'({self.first}, {self.second})'

    def __add__(self, other):
        return MyPair(self.first  + other.first,
                      self.second + other.second)


if __name__ == '__main__':
    p1 = MyPair(2, 3)
    p2 = MyPair(4, 7)
    p3 = p1 + p2
    print(p3)       # (6, 10)