from ting_file_management.priority_queue import PriorityQueue
import pytest

mock_high_priorit = {
    "nome_do_arquivo": "arquivo_teste.txt",
    "qtd_linhas": 3,
    "linhas_do_arquivo": [""],
}

mock_low_priorit = {
    "nome_do_arquivo": "arquivo_teste.txt",
    "qtd_linhas": 9,
    "linhas_do_arquivo": [""],
}


def test_basic_priority_queueing():
    queue = PriorityQueue()

    queue.enqueue(mock_high_priorit)
    queue.enqueue(mock_low_priorit)

    assert len(queue) == 2

    priority = queue.is_priority(mock_low_priorit)
    assert priority is False

    result = queue.search(0)
    assert result["qtd_linhas"] == 3

    result = queue.search(1)
    assert result["qtd_linhas"] == 9

    queue.dequeue()
    assert len(queue) == 1

    result = queue.search(0)
    print(result)
    assert result["qtd_linhas"] == 9
    assert result == mock_low_priorit

    with pytest.raises(IndexError, match="Índice Inválido ou Inexistente"):
        queue.search(99)
