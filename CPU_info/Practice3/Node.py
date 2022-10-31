from cpu_info import CPUInfo


class Node:

    def __init__(self, data: CPUInfo):
        self.data = data    # type: CPUInfo
        self.next = None    # type: [Node, None]

    def has_value(self, value: CPUInfo):
        """method to compare the value with the node data"""
        if self.data is value:
            return True
        else:
            return False

    def __repr__(self):
        return self.data
