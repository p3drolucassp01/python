import pytest
from test_001 import maior_numero  # substitua 'seu_modulo' pelo nome do seu arquivo

def test_maior_numero():
    assert maior_numero(1, 2, 3) == 3
    assert maior_numero(3, 1, 2) == 3
    assert maior_numero(2, 3, 1) == 3
    assert maior_numero(5, 5, 3) == 5
    assert maior_numero(4, 4, 6) == 6
    assert maior_numero(7, 7, 7) == 7
    assert maior_numero(-1, -5, -3) == -1
    assert maior_numero(2, -1, 0) == 2
    assert maior_numero(1.5, 2.5, 1.0) == 2.5



