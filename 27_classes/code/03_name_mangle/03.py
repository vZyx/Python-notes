
class Book:
    def __init__(self):
        pass
    def __f1(self):
        print('__f1')
    def __f2_(self):
        print('__f2_')
    def _f3(self):
        print('_f3')

book = Book()
#book.__f1()   # AttributeError
#book.__f2_()  # AttributeError
book._f3()     # _f3

print(dir(book))    # return the names in the current scope
# ['_Book__f1', '_Book__f2_', '__class__', ... , '_f3']

