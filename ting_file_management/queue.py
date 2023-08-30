from ting_file_management.abstract_queue import AbstractQueue


class Queue(AbstractQueue):
    def __init__(self):
        """Inicialize sua estrutura aqui"""
        self.data = []

    def __len__(self):
        """Aqui irá sua implementação"""
        return len(self.data)

    def enqueue(self, value):
        """Aqui irá sua implementação"""
        self.data.append(value)

    def dequeue(self):
        """Aqui irá sua implementação"""
        value = self.data[0]
        self.data.pop(0)
        return value

    def search(self, index):
        """Aqui irá sua implementação"""
        if index < 0 or index >= len(self.data):
            raise IndexError("Índice Inválido ou Inexistente")
        return self.data[index]
