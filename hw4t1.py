class Node(object):
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next


class LinkedList(object):
    def __init__(self):
        self.__start = None
        self.__end = None
        self.__len = 0

    def __iter__(self):
        return Iterator(self.__start)

    def __len__(self):
        length = 0
        if self.__start:
            length = 1
            current = self.__start
            while current.next:
                current = current.next
                length += 1
        return length

    def __str__(self):
        if not self.__start:
            return 'LinkedList is empty'
        current = self.__start
        output = f'{current.value}'
        while current.next:
            current = current.next
            output += f' | {current.value}'
        return f'-({output})-'

    def append(self, value):
        self.__len += 1
        if not self.__start:
            self.__start = Node(value)
            self.__end = self.__start
        else:
            self.__end.next = Node(value)
            self.__end = self.__end.next

    def insert(self, value, position):
        if position < 0:
            position = self.__len + position
        if not self.__start:
            self.__start = Node(value)
            self.__end = self.__start
            self.__len += 1
        if not position:
            self.__start = Node(value, self.__start)
            self.__len += 1
            return
        current = self.__start
        currentposition = 0
        while current:
            currentposition += 1
            if currentposition == position:
                current.next = Node(value, current.next)
                if not current.next:
                    self.__end = current
                self.__len += 1
                return
            current = current.next
        raise ValueError('Out of range')

    def index(self, value):
        currentposition = 0
        current = self.__start
        while current:
            if current.value == value:
                return currentposition
            current = current.next
            currentposition += 1
        raise ValueError('There is no this value')

    def pop(self, position):
        if position < 0:
            position = self.__len + position
        if not self.__start:
            raise IndexError('There is noting to pop')
        current = self.__start
        currentposition = 0
        if not position:
            self.start = self.__start.next
            self.__len -= 1
            return
        while current:
            if currentposition == position:
                if not current.next:
                    self.__end = current
                previous.next = current.next
                self.__len -= 1
                return
            previous = current
            current = current.next
            currentposition += 1
        raise ValueError('Out of range')

    def remove(self, value):
        if not self.__start:
            raise IndexError('There is noting to remove')
        current = self.__start
        if current.value == value:
            self.__start = self.__start.next
            return
        while current:
            if current.value == value:
                if not current.next:
                    self.__end = current
                previous.next = current.next
                self.__len -= 1
                return
            previous = current
            current = current.next
        raise ValueError('There is no this value to remove')

    def __getitem__(self, position):
        if position < 0:
            position = self.__len + position
        if not self.__start:
            raise IndexError('There is noting to get')
        current = self.__start
        currentposition = 0
        while current:
            if currentposition == position:
                return current.value
            currentposition += 1
            current = current.next
        raise IndexError('Out of range')

    def __setitem__(self, position, value):
        if position < 0:
            position = self.__len + position
        if not self.__start:
            raise IndexError('There is noting to set')
        current = self.__start
        currentposition = 0
        while current:
            if currentposition == position:
                current.value = value
                return
            currentposition += 1
            current = current.next
        raise IndexError('Out of range')


class Iterator(object):
    def __init__(self, current: Node):
        self.__current = current

    def __iter__(self):
        return self

    def __next__(self):
        current = self.__current
        if current:
            currentvalue = self.__current.value
            self.__current = self.__current.next
            return currentvalue
        raise StopIteration

a = LinkedList()
a.append(2)
a.append(6)
a.append(78)
a.append('fgtx')
a.insert('ist', 3)
print(a)
print(a[1])
a[-1] = 'here'
print([i for i in a])
