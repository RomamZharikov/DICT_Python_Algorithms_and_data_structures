from CPU_info import cpu_info


class Node:

    def __init__(self, data: cpu_info):
        self.data = data    # type: cpu_info
        self.next = None    # type: [Node, None]

    def has_value(self, value: cpu_info):
        """method to compare the value with the node data"""
        if self.data is value:
            return True
        else:
            return False

    def __repr__(self):
        return self.data
