import ctypes


class Array:
    def __init__(self, size):
        array_data_type = ctypes.py_object * size
        self.size = size
        self.memory = array_data_type()
        for i in range(size):
            self.memory[i] = None

    def __len__(self):
        return self.size

    def __getitem__(self, idx):
        return self.memory[idx]  # Is valid idx?

    def __setitem__(self, idx, value):
        self.memory[idx] = value

    def __repr__(self):
        result = ''
        for i in range(self.size):
            result += str(self.memory[i]) + ', '
        return result

    def append1(self, item):
        # 1) create a new array of bigger size: size+1 steps
        array_data_type = ctypes.py_object * (self.size + 1)
        new_memory = array_data_type()

        # 2) copy old data - 2 size steps
        for i in range(self.size):
            new_memory[i] = self.memory[i]

        # add the new element and increase size: 2 steps
        new_memory[self.size] = item
        self.size += 1

        # use the new memory and delete old one: size+2 steps
        del self.memory
        self.memory = new_memory
        # Total approximately: 4size + 5 steps

    def append(self, item):
        # 1) create a new array of bigger size
        array_data_type = ctypes.py_object * (self.size + 1)
        new_memory = array_data_type()

        # 2) copy old data
        for i in range(self.size):
            new_memory[i] = self.memory[i]

        # add the new element and increase size
        new_memory[self.size] = item
        self.size += 1

        # use the new memory and delete old one
        del self.memory
        self.memory = new_memory



if __name__ == '__main__':


    array = Array(3)

    for i in range(len(array)):
        array[i] = i + 1

    array.append('12')
    array.append('hello')

    print(array)

    for i in range(10 ** 6):
        array.append(i)

    print(len(array))
    # takes too much time to finish!
