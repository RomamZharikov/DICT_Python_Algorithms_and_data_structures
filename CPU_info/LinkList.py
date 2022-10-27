from AbstractStructure import AbstractStructure
from Practice2.Person import Person
from Practice2.Person import Generator
from Node import Node


class LinkList(AbstractStructure):
    __head: [None, Node] = None
    __tail: [None, Node] = None
    size: int = 0

    def add(self, value: Person, index: [None, int] = None) -> bool:
        if index is not None and (index < 0 or index >= self.size):
            return False

        if self.__head is None:
            node = Node(value)
            self.__head = node
            self.__tail = node
        elif index is None:
            # вариант 1, через цикл
            # current = self.__head
            # while current.next:
            #     current = current.next
            # node = Node(value)
            # current.next = node

            # вариант 2, через вспомогательную переменную, указывающую на последний элемент
            current = self.__tail
            node = Node(value)
            current.next = node
            self.__tail = node
        else:
            i = 0
            current = self.__head
            while current.next and i < index-1:
                current = current.next
                i += 1
            node = Node(value)
            node.next = current.next
            current.next = node
        self.size += 1
        return True

    def insert(self, value, index) -> bool:
        pass

    def find(self, value) -> [int, None]:
        pass

    def get(self, index) -> object:
        pass

    def remove(self, value) -> bool:
        # current.next.data == value
        # current.next = current.next.next
        pass

    def get_all(self) -> list:
        out = []
        current = self.__head
        while current is not None:
            out.append(current.data)
            current = current.next
        return out


if __name__ == "__main__":

    g = Generator()

    p1 = g.generate_single()
    p2 = g.generate_single()
    p3 = g.generate_single()
    p4 = g.generate_single()
    p5 = g.generate_single()
    print([p1, p2, p3, p4, p5])

    s_list = LinkList()
    s_list.add(p1)
    s_list.add(p2)
    s_list.add(p3)
    s_list.add(p4)
    print(s_list.add(p5, 1))
    # print("insert1: " + str(s_list.insert(p4, 1)))
    # print("insert2: " + str(s_list.insert(p4, 10)))

    print(s_list.get_all())
    print(s_list.size)
    # print(len(s_list))
