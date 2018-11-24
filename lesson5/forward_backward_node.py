class Node(object):
    def __init__(self, data, next, previous):
        self._data = data
        self._next = next
        self._previous = previous

    @property
    def data(self):
        return self._data

    @property
    def next(self):
        return self._next

    @next.setter
    def next(self, next):
        self._next = next

    @property
    def previous(self):
        return self._previous

    @previous.setter
    def previous(self, previous):
        self._previous = previous
