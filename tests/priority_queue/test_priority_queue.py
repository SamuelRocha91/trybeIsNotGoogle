import pytest
from ting_file_management.priority_queue import PriorityQueue
from ting_file_management.queue import Queue
from ting_file_management.file_process import process


def test_basic_priority_queueing():
    """Aqui irá sua implementação"""
    project = Queue()
    dict = process("statics/arquivo_teste.txt", project)
    priority = PriorityQueue()
    assert priority.is_priority(dict) is True
    priority.enqueue(dict)
    assert len(priority) == 1
    assert len(priority.high_priority) == 1
    assert len(priority.regular_priority) == 0
    assert priority.search(0) == dict
    dict_2 = process("statics/novo_paradigma_globalizado-min.txt", project)
    priority.enqueue(dict_2)
    assert len(priority) == 2
    assert priority.search(1) == dict_2
    assert len(priority.high_priority) == 1
    assert len(priority.regular_priority) == 1
    priority.dequeue()
    assert len(priority) == 1
    assert len(priority.high_priority) == 0
    assert len(priority.regular_priority) == 1
    with pytest.raises(IndexError, match="Índice Inválido ou Inexistente"):
        priority.search(1)
