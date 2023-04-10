

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

    dct = {}
    dct[p1] = 90
    dct[p2] = 80

    print(dct[p1])  # 80
    print(dct[p2])  # 80
    print(len(dct)) # 1
    p1.name = 'another'
    #print(dct[p1])  # 90   KeyError
    # Don't change the object once entered in the hash table
    # It will just make unexpected errors
    # That is why immutability matter
