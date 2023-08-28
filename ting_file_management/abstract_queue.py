from abc import ABC, abstractmethod


class AbstractQueue(ABC):
    @abstractmethod
    def __len__(self):
        raise NotImplementedError

    @abstractmethod
    def enqueue(self, value):
        raise NotImplementedError

    @abstractmethod
    def dequeue(self):
        raise NotImplementedError
