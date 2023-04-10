class Node:
    def __init__(self, data):
        self.data = data
        self.next = None  # Pointer

    def __repr__(self):
        return f'{self.data}'


def print_lst(head):
    while head is not None:
        print(head.data, end='->')
        head = head.next
    print()


def print_rec(head):
    if head is not None:
        print(head.data, end='->')
        print_rec(head.next)


def print_rec_reversed(head):
    if head is not None:
        print_rec_reversed(head.next)
        print(head.data, end='->')


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
    node4.next = None  # 4-E link

    print_rec_reversed(node1)
