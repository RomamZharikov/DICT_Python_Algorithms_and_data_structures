from AbstractStructure import AbstractStructure
from cpu_info import CPUInfo
from generator import Generator
from Node import Node


class LinkList(AbstractStructure):
    __head: [None, Node] = None
    __tail: [None, Node] = None
    size: int = 0

    def add(self, value: CPUInfo, index: [None, int] = None) -> bool:
        if index is not None and (index < 0 or index >= self.size):
            return False

        if self.__head is None:
            node = Node(value)
            self.__head = node
            self.__tail = node
        elif index is None:
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
        if index is None:
            return False
        else:
            past_element = None
            current = self.__head
            while current != index:
                past_element = current
                current = current.next
                print(f"{past_element}\n==\n{current}")
                if current is None:
                    return False
            node = Node(value)
            node.next = current.next
            current.next =
            past_element[1] = value[0]
            value[1] = current.next
            return True

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

    p1 = g.generator()
    p2 = g.generator()
    p3 = g.generator()
    p4 = g.generator()
    p5 = g.generator()
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
