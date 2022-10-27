from Practice2.Person import Person


class Node:

    def __init__(self, data: Person):
        self.data = data    # type: Person
        self.next = None    # type: [Node, None]

    def has_value(self, value: Person):
        """method to compare the value with the node data"""
        if self.data is value:
            return True
        else:
            return False

    def __repr__(self):
        return self.data
