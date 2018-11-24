from lesson5.forward_only_node import Node


class Queue(object):
    def __init__(self):
        self._front = None
        self._last = None

    def enqueue(self, node):
        if self._last:
            self._last.next = node

        self._last = node
        
        if not self._front:
            self._front = node

    def dequeue(self):
        item = self._front
        self._front = self._front.next
        return item

    def peek(self):
        return self._front
