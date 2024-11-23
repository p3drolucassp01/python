import pytest
from arquivo import calcular_soma  # Assumindo que o código acima está no arquivo "program.py"

# Caso de teste 1: N < M, N par
def test_caso_1():
    N, M, SOMA = calcular_soma(2, 6)
    assert (N, M, SOMA) == (2, 6, 8)

# Caso de teste 2: N < M, N ímpar
def test_caso_2():
    N, M, SOMA = calcular_soma(3, 8)
    assert (N, M, SOMA) == (3, 8, 15)

# Caso de teste 3: N >= M (INTERVALO INCORRETO)
def test_caso_3():
    resultado = calcular_soma(7, 4)
    assert resultado == "INTERVALO INCORRETO"

# Caso de teste 4: N < M, M negativo
def test_caso_4():
    resultado = calcular_soma(1, -3)
    assert resultado == "INTERVALO INCORRETO"

# Caso de teste 5: N = M
def test_caso_5():
    resultado = calcular_soma(5, 5)
    assert resultado == "INTERVALO INCORRETO"
