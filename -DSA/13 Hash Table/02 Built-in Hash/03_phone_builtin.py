

class PhoneEntry:
    def __init__(self, name, number, address):
        self.name = name
        self.number = number
        self.address = address

    def __hash__(self):
        tup = (self.name, self.number)
        return hash(tup)


    def __eq__(self, other):
        return self.name == other.name and \
               self.number == other.number

if __name__ == '__main__':
    p1 = PhoneEntry('Most', '123', 'Egypt')
    p2 = PhoneEntry('Most', '123', 'Canada')

    print(hash(p1)) # 8450947171949827232
    print(hash(p2)) # 8450947171949827232
