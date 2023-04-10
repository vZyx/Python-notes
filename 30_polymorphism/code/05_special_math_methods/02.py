
class MyPair:
    def __init__(self, first, second):
        self.first = first
        self.second = second

    def __repr__(self):
        return f'({self.first}, {self.second})'

    def __iadd__(self, value):   # support +=
        self.first += value
        self.second += value
        return self


if __name__ == '__main__':
    p1 = MyPair(2, 3)
    p1 += 10
    print(p1)       # (12, 13)