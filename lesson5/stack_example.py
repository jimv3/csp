from lesson5.forward_only_node import Node


class Stack(object):
    def __init__(self):
        self._top = None

    def push(self, node):
        node.next = self._top
        self._top = node

    def pop(self):
        item = self._top
        self._top = self._top.next
        return item

    def peek(self):
        return self._top
