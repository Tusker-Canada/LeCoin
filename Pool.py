from collections import deque


class Pool:

    def __init__(self):
        self.queue = deque()

    def append(self, block):
        self.queue.append(block)

    def pop(self, block):
        self.queue.pop(0)

    def clear(self):
        self.queue.clear()

    def show(self):
        self.queue