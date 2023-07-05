from buffer_fifo.abc_fifo import BufferFIFO


class ArrayBufferFIFO(BufferFIFO):
    def __init__(self, max_size=5):
        self._items = [None] * max_size
        self._head = 0
        self._tail = 0
        self._length = 0
        self._size = max_size

    def push(self, item):
        if self.is_full():
            raise Exception("Queue is full")
        self._items[self._head] = item
        self._length += 1
        self._head = self._update_index(self._head)

    def pop(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        item = self._items[self._tail]
        self._items[self._tail] = None
        self._length -= 1
        self._tail = self._update_index(self._tail)
        return item

    def peek(self):
        return self._items[self._tail]

    def _update_index(self, index):
        new_index = index + 1
        if new_index >= self._size:
            new_index = 0
        return new_index

    def is_full(self):
        return self._length == self._size

    def is_empty(self):
        return self._length == 0

    def __len__(self):
        return self._length
