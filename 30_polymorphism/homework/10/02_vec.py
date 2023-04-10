from functools import total_ordering

@total_ordering
class Vector:
    def __init__(self, *values):
        self.values = list(values)

    def __repr__(self):
        return repr(self.values)

    def __eq__(self, other):
        if not isinstance(other, Vector):
            return NotImplemented
        return self.values == other.values

    def __lt__(self, other):
        if not isinstance(other, Vector):
            return NotImplemented
        return self.values < other.values

    def __add__(self, other):
        if not isinstance(other, Vector):
            return NotImplemented

        if len(self.values) != len(other.values):
            raise ValueError('Vectors are not of equal length')

        values = [a + b for a, b in zip(self.values, other.values)]
        return Vector(*values)


if __name__ == '__main__':
    v1 = Vector(1, 2, 3, 4)
    v2 = Vector(4, 5, 1, -2)
    v3 = Vector(4, 5, 1)

    print(v1 + v2)  # [5, 7, 4, 2]
    print(v1 <= v2)  # True

    #print(v1 + v3)  # ValueError: Vectors are not of equal length

