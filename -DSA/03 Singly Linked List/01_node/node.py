
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None  # Pointer

    def __repr__(self):
        return f'{self.data}'
    

if __name__ == '__main__':

    # Create 4 objects and set data
    node1 = Node(6)
    node2 = Node(10)
    node3 = Node(8)
    node4 = Node(15)
    # Set 4 links
    node1.next = node2  # 1-2 link
    node2.next = node3  # 2-3 link
    node3.next = node4  # 3-4 link
    node4.next = None   # 4-E link

    print(node1.next.next.next.data)    # 15
    print(node2.next.next.data)         # 15
    print(node3.next.data)              # 15
    print(node4.data)                   # 15

    print(id(node1), id(node1.next))
    print(id(node2), id(node2.next))
    print(id(node3), id(node3.next))
    print(id(node4), id(node4.next))

    """
    139768834628048 139768834629536
                    139768834629536 139768834475776
                                    139768834475776 139768834475968
                                                    139768834475968 94734547242336
    """
