
class Book:
    def __init__(self):
        self.att1 = 1
        self._att2 = 2
        self._att3_ = 3
        self.__att4 = 4
        self.___att5 = 5
        self.__att6_ = 6
        self.__att7__ = 7
        self.____att8_ = 8
        self.____att9__ = 9

if __name__ == '__main__':
    book = Book()
    print(book.att1)            # 1
    print(book._att2)           # 2
    print(book._att3_)          # 3
    #print(book.__att4)         # AttributeError
    #print(book.___att5)        # AttributeError
    #print(book.__att6_)        # AttributeError
    print(book.__att7__)        # 7
    #print(book.____att8_)      # AttributeError
    print(book.____att9__)      # 9


