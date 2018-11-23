class LinkedList(object):
    def __init__(self):
        self._root = None
        self._last = self._root

    def add_node(self, node):
        if not self._last:
            self._last = node
        else:
            self._last.next = node
            self._last = node

        if not self._root:
            self._root = node

    def list_nodes(self):
        n = self._root
        while n:
            print(n._data)
            n = n.next
