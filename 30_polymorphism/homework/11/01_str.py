

class strv2(str):
    def __add__(self, other):
        if not isinstance(other, str):
            return NotImplemented
        return strv2(super().__add__(other))

    def __radd__(self, other):
        # see __rsub__ logic
        if not isinstance(other, str):
            return NotImplemented
        return strv2(other) + self

    def __mul__(self, other):
        if not isinstance(other, int):
            return NotImplemented
        return strv2(super().__mul__(other))

    def __rmul__(self, other):
        # see __rsub__ logic
        if not isinstance(other, int):
            return NotImplemented
        return self * other


    def __sub__(self, other):
        if not isinstance(other, str):
            return NotImplemented

        if not self.endswith(other):
            return self

        return strv2(self[:-len(other)])

    def __rsub__(self, other):
        # If we are here: then original call is other - self, but other is str
        # we do so operation again and reswap, but consider conver other to our class
        if not isinstance(other, str):
            return NotImplemented

        return strv2(other) - self

    def __isub__(self, other):
        if not isinstance(other, str):
            return NotImplemented

        self = self - other

        return self


if __name__ == '__main__':

    s1 = strv2('abcd')
    s2 = strv2('cd')

    r = s1 - s2                 # ab
    r = r * 2 + 2 * s2          # ababcdcd
    r -= 'dcd'                  # ababc
    r += 'Xabcd' - s1 - 'Y'     # ababcX

    print(r, type(r))
