
# it is totally ok to come up with other designs
# Read below and learn

class IkeaRootException(BaseException):
    pass

class PriceError(IkeaRootException):
    pass


class Item:
    def __init__(self, name, id, price = None):
        self.name = name
        self.id = id
        self._price = price
        self.parts = []

    def add_part(self, item):
        if self._price is not None:
            raise PriceError("Item that has an initial price shouldn't have parts!")
        self.parts.append(item)

    @property
    def price(self):
        if self._price is not None:
            return self._price

        return sum([item.price for item in self.parts])   # deep price!


class SpecialChair(Item):
    def __init__(self, name, id, color, price=None):
        super().__init__(name, id, price)
        self.color = color

    @staticmethod
    def builder(color):
        item1 = Item('Chair left leg', 1234, 65)
        # item2.add_part(None)    PriceError

        item2 = Item('Chair right leg', 1235)
        item2.add_part(Item('Main Base', 123451, 30))
        item2.add_part(Item('Main Extension', 123452, 70))

        item_chair = SpecialChair('Chair', 1236, color)
        item_chair.add_part(item1)
        item_chair.add_part(item1)
        item_chair.add_part(item2)

        return item_chair


# And so on

if __name__ == '__main__':
    item_chair = SpecialChair.builder('Black')
    print(item_chair.price)
