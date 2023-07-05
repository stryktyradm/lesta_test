from buffer_fifo.abc_fifo import BufferFIFO


class ListNode:
    def __init__(self, data, prev, link):
        self.data = data
        self.prev = prev
        self.link = link
        if prev is not None:
            self.prev.link = self
        if link is not None:
            self.link.prev = self


class LinkedBufferFIFO(BufferFIFO):
    def __init__(self, max_size=5, head=None, tail=None):
        self._head = head
        self._tail = tail
        self._size = max_size
        self._length = 0

    def push(self, item):
        if self.is_full():
            raise Exception("Queue is full")
        node = ListNode(item, None, self._head)
        if self._tail is None:
            self._tail = node
        self._head = node
        self._length += 1

    def pop(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        item = self._tail
        before = self._tail.prev
        self._tail = before
        self._length -= 1
        return item.data

    def peek(self):
        return getattr(self._tail, 'data', None)

    def is_full(self):
        return self._length == self._size

    def is_empty(self):
        return self._length == 0

    def __len__(self):
        return self._length
