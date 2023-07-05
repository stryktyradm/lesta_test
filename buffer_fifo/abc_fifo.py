import abc


class BufferFIFO(abc.ABC):
    @abc.abstractmethod
    def push(self, item):
        raise NotImplementedError

    @abc.abstractmethod
    def pop(self):
        raise NotImplementedError

    @abc.abstractmethod
    def peek(self):
        raise NotImplementedError

    @abc.abstractmethod
    def is_full(self):
        raise NotImplementedError

    @abc.abstractmethod
    def is_empty(self):
        raise NotImplementedError

    @abc.abstractmethod
    def __len__(self):
        raise NotImplementedError
