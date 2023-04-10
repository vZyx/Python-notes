

class Book:
    def __init__(self):
        self.att1 = 1
        self.__att4 = 4
        self.___att5 = 5
        self.__att6_ = 6
        self.____att8_ = 8

if __name__ == '__main__':
    book = Book()
    # __dict__ : contains all the attributes of the object
    print(book.__dict__)
    #{'att1': 1, '_Book__att4': 4 , '_Book___att5': 5,
    #            '_Book__att6_': 6, '_Book____att8_': 8}
    print(book._Book__att4)     # 4
    # Observe: in run-time, interpreter changed the attributes names
    # by prefixing with: _Book


