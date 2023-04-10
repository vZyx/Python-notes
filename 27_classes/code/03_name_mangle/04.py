

class Book:
    def __init__(self):
        self.__att4 = 4  # _Book__att4

    def hello(self):
        print(self.__att4)  # visible from INSIDE!
        print(self._Book__att4)  # visible from inside!


if __name__ == '__main__':
    book = Book()
    # print(book.__att4)          # NOT visible from OUTSIDE
    print(book._Book__att4)  # we still can access indirectly
    book.hello()



