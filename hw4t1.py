# class LinkedList(object):
#     def __iter__(self) -> Iterator: ...
#     def __getitem__(self, index: int) -> Any: ...
#     def __setitem__(self, index: int, value: Any) -> None: ...
#     def index(item: Any) -> int: ...
#     def pop(index: int = -1) -> Any: ...
#     def remove(item: Any) -> None: ...

# class Iterator(object):
#     __current: Node
#     def __iter__(self) -> Iterator: ...
#     def __next__(self) -> Iterator: ...
#
#

class Node(object):
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next


class LinkedList:
    def __init__(self):
        self.__start = None
        self.__end = None
        self.__len = 0

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
        if self.__start:
            current = self.__start
            out = f'{current.value}'
            while current.next:
                current = current.next
                out += f', {current.value}'
            return f'[{out}]'
        return 'LinkedList is empty'

    def __getitem__(self, position):
        length = 0
        current = None
        if self.__start:
            current = self.__start
            while position != length or current.next:
                current = current.next
                length += 1
            if position == length:
                current = current.value
        return current

    def append(self, value):
        self.__len += 1
        if self.__start:
            self.__end.next = self.__end = Node(value, None)
        else:
            self.__start = self.__end = Node(value, None)

    def insert(self, position, value):
        if not self.__start:
            self.__end = self.__end = Node(value, None)
            return
        if not position:
            self.__start = Node(value, self.__start)
            return
        current = self.__start
        count = 0
        while current:
            count += 1
            if count == position:
                current.next = Node(value, current.next)
                if not current.next.next:
                    self.__end = current.next
                break
            current = current.next





a = LinkedList()
a.append(2)
a.append(3)
a.append(4)
a.append(5)
a.append(6)
a.append(7)
a.append(8)
a.append(9)
a.append(0)

a.insert(1, 45)
print(len(a))
print(a)
print(a.index(6))
