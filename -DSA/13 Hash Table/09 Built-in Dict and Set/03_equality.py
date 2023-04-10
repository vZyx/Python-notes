
class PhoneEntry:
    def __init__(self, name, number, address):
        self.name = name
        self.number = number
        self.address = address

    def __hash__(self):
        return hash((self.name, self.number))

    def __eq__(self, other):
        return False

p1 = PhoneEntry('Most', '123', 'Egypt')
p2 = PhoneEntry('Most', '123', 'Canada')
dct = {}
dct[p1] = 90
dct[p2] = 80
print(len(dct))     # 2
