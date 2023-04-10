

class MyPair:
    def __init__(self, first, second):
        self.first = first
        self.second = second

    def __repr__(self):
        return f'({self.first}, {self.second})'

    def __lt__(self, other_pair):
        return self.first < other_pair.first and \
               self.second < other_pair.second


if __name__ == '__main__':

    p1 = MyPair(5, 10)
    p2 = MyPair(7, 13)
    p3 = MyPair(4, 12)

    print(p1 < p1)  # False
    print(p1 < p2)  # True
    print(p1 < p3)  # False
    print(p3 < p2)  # True

