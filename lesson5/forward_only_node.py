class Node(object):
    def __init__(self, data, next):
        self._data = data
        self._next = next

    @property
    def next(self):
        return self._next

    @next.setter
    def next(self, next):
        self._next = next
