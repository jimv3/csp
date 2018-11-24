from lesson5.forward_backward_node import Node


class DoublyLinkedList(object):
    def __init__(self):
        self._root = None
        self._last = self._root

    def add_node(self, node):
        if not self._last:
            node.before = self._root
            self._last = node
        else:
            node.previous = self._last
            self._last.next = node
            self._last = node

        if not self._root:
            self._root = node

    def list_nodes(self):
        n = self._roots
        while n:
            print(n.data)
            n = n.next

    def list_nodes_reverse(self):
        n = self._last
        while n:
            print(n.data)
            n = n.previous
