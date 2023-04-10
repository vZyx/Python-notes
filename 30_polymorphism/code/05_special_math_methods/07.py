
class MyPair:
    def __init__(self, first, second):
        self.first = first
        self.second = second

    def __repr__(self):
        return f'({self.first}, {self.second})'

    def __neg__(self):   # -pair
        return MyPair(-self.first, -self.second)


if __name__ == '__main__':
    p1 = MyPair(2, 3)
    print(-p1)       # (-2, -3)
