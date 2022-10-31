from AbstractStructure import AbstractStructure
from cpu_info import CPUInfo
from generator import Generator
from Node import Node


class LinkList(AbstractStructure):
    __head: [None, Node] = None
    __tail: [None, Node] = None
    size: int = 0

    def __len__(self):
        return self.size

    def add(self, value: CPUInfo, index: [None, int] = None) -> bool:
        node = Node(value)
        if index is not None and (index < 0 or index >= self.size):
            return False
        if self.__head is None:
            self.__head = node
            self.__tail = node
        elif index is None:
            current = self.__tail
            current.next = node
            self.__tail = node
        else:
            i = 0
            current = self.__head
            while current.next and i < index - 1:
                current = current.next
                i += 1
            node.next = current.next
            current.next = node
        self.size += 1
        return True

    def insert(self, value: CPUInfo, index: int) -> bool:
        if index is None or index is not None and (index < 0 or index >= self.size):
            return False
        else:
            i = 0
            current = self.__head
            while current.next and i < index - 1:
                current = current.next
                i += 1
            node = Node(value)
            node.next = current.next
            current.next = node
            return True

    def find(self, value: CPUInfo) -> [int, None]:
        i = 0
        current = self.__head
        try:
            while current.data != value:
                current = current.next
                i += 1
            return i
        except AttributeError:
            return None

    def get(self, index: int) -> object:
        if index is None or index is not None and (self.size <= index or index < 0):
            return None
        else:
            i = 0
            current = self.__head
            while current.next and i < index:
                current = current.next
                i += 1
            return current.data

    def remove(self, value: CPUInfo) -> bool:
        current = self.__head
        if current is None:
            return False
        while current:
            try:
                if current.next.data == value:
                    current.next = current.next.next
                    break
            except AttributeError:
                pass
            if current.data == value:
                self.__head = current.next
                return True

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
    print("Array generated: \n", [p1, p2, p3, p4, p5])
    print("=" * 300)

    print("Linked list created:")
    s_list = LinkList()
    s_list.add(p1)
    s_list.add(p2)
    s_list.add(p3)
    s_list.add(p4)
    print(s_list.add(p5, 1))
    print("insert1: " + str(s_list.insert(p4, 1)))
    print("insert2: " + str(s_list.insert(p4, 10)))

    print(s_list.get_all())
    print(s_list.size)
    print(len(s_list))
