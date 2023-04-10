
class MyPair:
    def __init__(self, first, second):
        self.first = first
        self.second = second

    def __repr__(self):
        return f'({self.first}, {self.second})'

    def __add__(self, other):
        return MyPair(self.first  + other.first,
                      self.second + other.second)

    def __contains__(self, item):
        return self.first == item or self.second == item

if __name__ == '__main__':
    p = MyPair(2, 3)
    print(2 in p)   # True
    print(3 in p)   # True
    print(4 in p)   # False
