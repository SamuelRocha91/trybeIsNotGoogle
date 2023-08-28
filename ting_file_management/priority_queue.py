from ting_file_management.abstract_queue import AbstractQueue
from ting_file_management.queue import Queue


class PriorityQueue(AbstractQueue):
    def __init__(self):
        self.regular_priority = Queue()
        self.high_priority = Queue()
        self.priority_limit = 5

    def is_priority(self, value):
        return value["qtd_linhas"] < self.priority_limit

    def __len__(self):
        return len(self.high_priority) + len(self.regular_priority)

    def enqueue(self, value):
        if self.is_priority(value):
            self.high_priority.enqueue(value)
        else:
            self.regular_priority.enqueue(value)

    def dequeue(self):
        if len(self.high_priority):
            return self.high_priority.dequeue()

        return self.regular_priority.dequeue()

    def search(self, index):
        if index < len(self.high_priority):
            return self.high_priority.search(index)
        return self.regular_priority.search(index - len(self.high_priority))
