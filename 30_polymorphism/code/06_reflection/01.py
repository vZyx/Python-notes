

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

    print(p1 < p2)  # True
    print(p2 > p1)  # True:
    # Python calls automatically swaps and calls p1 < p2

