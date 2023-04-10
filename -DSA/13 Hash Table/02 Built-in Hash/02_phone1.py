

class PhoneEntry:
    def __init__(self, name, number, address):
        self.name = name
        self.number = number
        self.address = address

    def get_hash(self):
        tup = (self.name, self.number)
        return hash(tup)

if __name__ == '__main__':
    p1 = PhoneEntry('Most', '123', 'Egypt')
    p2 = PhoneEntry('Most', '123', 'Canada')
    p3 = PhoneEntry('MOST', '123', 'USA')

    print(p1.get_hash())    # -3500145881171370879
    print(p2.get_hash())    # -3500145881171370879
    print(p3.get_hash())    # 904957105696487210
    # p1 and p2 are different objects
    # but their hash value is the same as it counts on the SAME values
