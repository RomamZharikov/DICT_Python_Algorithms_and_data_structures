from AbstractStructure import AbstractStructure
from generator import Generator
from cpu_info import CPUInfo

class List(AbstractStructure):
    __list = []
    size: int = 0

    def add(self, value: CPUInfo, index: [int, None] = None) -> bool:
        if index is not None and self.size <= index < -self.size:
            return False
        if index is None:
            self.__list.append(value)
        else:
            self.insert(value, index)
        self.size += 1
        return True

    def insert(self, value: CPUInfo, index: int) -> bool:
        if (index is not None and self.size <= index < -self.size) or index is None:
            return False
        else:
            self.__list[index] = value
            return True

    def find(self, value: CPUInfo) -> [int, None]:
        if value in self.__list:
            return self.__list.index(value)
        else:
            return None

    def get(self, index: int) -> [CPUInfo, None]:
        if -self.size < index <= self.size:
            return self.__list[index]
        else:
            return None

    def remove(self, value: CPUInfo) -> bool:
        if value in self.__list:
            self.__list.remove(value)
            self.size -= 1
            return True
        else:
            return False

    def get_all(self) -> list:
        return self.__list

    def __len__(self) -> int:
        return self.size
