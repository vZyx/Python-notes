

class A:
    @staticmethod
    def hello():
        print('hello')

    @staticmethod
    def world():
        print('world from A')

class B(A):
    @staticmethod
    def world():
        print('world from B')



if __name__ == '__main__':
    B.hello()   # hello
    B.world()   # world from B