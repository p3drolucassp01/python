import pytest

from Atividade01102024 import validar_nome,validar_idade

def soft():
    return validar_nome()

def test_validaridade():
    assert validar_nome('Pedro') == True 
    
def test_validar_idade():
    assert validar_idade(21) == True