import inspect


class Node:
    def __init__(self, data, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

    def __repr__(self):
        return f'{self.data}'


class LinkedList:
    def __init__(self, initial_values=None):
        self.head = None
        self.tail = None
        self.length = 0

        self.debug_data = []  # add/remove nodes you use

        if initial_values:
            for value in initial_values:
                self.insert_end(value)

    def _add_node(self, node):
        self.debug_data.append(node)
        self.length += 1

    def _delete_node(self, node):
        if node in self.debug_data:
            self.debug_data.remove(node)
        else:
            print("Node does't exist!!")
            return

        self.length -= 1

    def debug_print_address(self):
        cur = self.head

        while cur is not None:
            print(f'{cur.data}@{id(cur)}', end='\t->\t')
            cur = cur.next
        print('None')

    def debug_print_node(self, node):
        if node is None:
            print('None')
            return

        prev_value = 'None' if node.prev is None else str(node.prev.data)
        print(prev_value.ljust(5), end='\t')

        print(str(node.data).ljust(5), end=' -> ')

        next_value = 'None' if node.next is None else str(node.next.data)
        print(next_value.ljust(5), end='\t')

        if node == self.head:
            print("head")
        elif node == self.tail:
            print("tail")
        else:
            print("")

    def debug_print_existing_nodes(self, msg=None):
        if msg:
            print(msg)

        for node in self.debug_data:
            self.debug_print_node(node)

        print('*******************')
        self.debug_verify_data_integrity()

    def debug_verify_data_integrity(self):
        if self.length == 0:
            assert self.head is None
            assert self.tail is None
            return

        assert self.head is not None
        assert self.head.prev is None
        assert self.tail is not None
        assert self.tail.next is None

        if self.length == 1:
            assert self.head == self.tail
        elif self.length == 2:
            assert self.head.next == self.tail
        else:
            assert self.length == len(self.debug_data)

            # Verify forward pass
            actual_lst_len = 0
            cur = self.head

            while cur is not None:
                cur = cur.next
                actual_lst_len += 1
                assert actual_lst_len < 1000  # Consider infinite cycle

            assert self.length == actual_lst_len
            
            # Verify backward pass 
            actual_lst_len = 0
            cur = self.tail

            while cur is not None:
                cur = cur.prev
                actual_lst_len += 1
                assert actual_lst_len < 1000  # Consider infinite cycle

            assert self.length == actual_lst_len

    ##############################################
    def print(self):
        cur = self.head

        while cur is not None:
            print(cur.data, end='->')
            cur = cur.next
        print('None')

    def print_reversed(self):
        cur = self.tail

        while cur is not None:
            print(cur.data, end='->')
            cur = cur.prev
        print('None')

    def __iter__(self):
        cur = self.head
        while cur is not None:
            yield cur
            cur = cur.next

    def __repr__(self):
        represent = ''
        cur = self.head

        while cur is not None:
            represent += str(cur.data)
            cur = cur.next
            if cur:
                represent += ', '

        return represent
    ##############################################
    @staticmethod
    def _link(first, second):
        if first:
            first.next = second
        if second:
            second.prev = first

    def insert_end(self, value):
        node = Node(value)
        self._add_node(node)

        if not self.head:
            self.head = self.tail = node
        else:
            self._link(self.tail, node)
            self.tail = node

        self.debug_verify_data_integrity()

    def insert_front(self, value):
        item = Node(value)
        self._add_node(item)

        self._link(item, self.head)
        self.head = item

        if self.length == 1:
            self.tail = self.head

        self.debug_verify_data_integrity()


    def _embed_after(self, node, value):
        # Add a node with value between node and its next
        new_node = Node(value)
        self._add_node(new_node)
        self._link(new_node, node.next)
        self._link(node, new_node)

    def insert_sorted(self, value):
        # 3 special cases for simplicity
        if not self.length or value <= self.head.data:
            self.insert_front(value)
        elif self.tail.data <= value:
            self.insert_end(value)
        else:
            prev, cur = None, self.head
            while cur:
                if value <= cur.data:
                    self._embed_after(prev, value)
                    break
                prev, cur = cur, cur.next

        self.debug_verify_data_integrity()



def test1():
    func_name = inspect.currentframe().f_code.co_name
    print(f'Testing {func_name}')

    lst = LinkedList([])
    lst.insert_sorted(77)

    lst.debug_print_existing_nodes()
    result = str(lst)
    expected = '77'

    assert result == expected, f'Mismatch between expected=[{expected}] and result=[{result}] in {func_name}'
    print('PASSED\n')


def test2():
    func_name = inspect.currentframe().f_code.co_name
    print(f'Testing {func_name}')

    lst = LinkedList([10])
    lst.insert_sorted(77)

    lst.debug_print_existing_nodes()
    result = str(lst)
    expected = '10, 77'

    assert result == expected, f'Mismatch between expected=[{expected}] and result=[{result}] in {func_name}'
    print('PASSED\n')


def test3():
    func_name = inspect.currentframe().f_code.co_name
    print(f'Testing {func_name}')

    lst = LinkedList([100])
    lst.insert_sorted(77)

    lst.debug_print_existing_nodes()
    result = str(lst)
    expected = '77, 100'

    assert result == expected, \
        f'Mismatch between expected=[{expected}] ' \
        f'and result=[{result}] in {func_name}'
    print('PASSED\n')


def test4():
    func_name = inspect.currentframe().f_code.co_name
    print(f'Testing {func_name}')

    lst = LinkedList([10, 20, 30, 40])
    lst.insert_sorted(77)

    lst.debug_print_existing_nodes()
    result = str(lst)
    expected = '10, 20, 30, 40, 77'

    assert result == expected, \
        f'Mismatch between expected=[{expected}] ' \
        f'and result=[{result}] in {func_name}'
    print('PASSED\n')


def test5():
    func_name = inspect.currentframe().f_code.co_name
    print(f'Testing {func_name}')

    lst = LinkedList([100, 200, 300, 400])
    lst.insert_sorted(100)

    lst.debug_print_existing_nodes()
    result = str(lst)
    expected = '100, 100, 200, 300, 400'

    assert result == expected, \
        f'Mismatch between expected=[{expected}] ' \
        f'and result=[{result}] in {func_name}'
    print('PASSED\n')


def test6():
    func_name = inspect.currentframe().f_code.co_name
    print(f'Testing {func_name}')

    lst = LinkedList([100, 200, 300, 400])
    lst.insert_sorted(150)

    lst.debug_print_existing_nodes()
    result = str(lst)
    expected = '100, 150, 200, 300, 400'

    assert result == expected, \
        f'Mismatch between expected=[{expected}] ' \
        f'and result=[{result}] in {func_name}'
    print('PASSED\n')


def test7():
    func_name = inspect.currentframe().f_code.co_name
    print(f'Testing {func_name}')

    lst = LinkedList([100, 200, 300, 400])
    lst.insert_sorted(250)

    lst.debug_print_existing_nodes()
    result = str(lst)
    expected = '100, 200, 250, 300, 400'

    assert result == expected, \
        f'Mismatch between expected=[{expected}] ' \
        f'and result=[{result}] in {func_name}'
    print('PASSED\n')



def test8():
    func_name = inspect.currentframe().f_code.co_name
    print(f'Testing {func_name}')

    lst = LinkedList([100, 200, 300, 400])
    lst.insert_sorted(350)

    lst.debug_print_existing_nodes()
    result = str(lst)
    expected = '100, 200, 300, 350, 400'

    assert result == expected, \
        f'Mismatch between expected=[{expected}] ' \
        f'and result=[{result}] in {func_name}'
    print('PASSED\n')

if __name__ == '__main__':
    test1()
    test2()
    test3()
    test4()
    test5()
    test6()
    test7()
    test8()
