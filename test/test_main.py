from main import suma, dividir, es_mayor_de_edad, Usuario
import pytest

def test_suma():
    assert suma(2,3) == 5

# para correr la prueba se debe guardar los cambios Ctrl + s, y correr pytest o pytest -v 
# 'para que de los resultados segmentados' en la terminal.

def test_dividir():
    assert dividir(10, 2) == 5
    with pytest.raises(ValueError):
        dividir(10, 0)


def test_es_mayor_de_edad():
    assert es_mayor_de_edad(20) is True
    assert es_mayor_de_edad(16) is False



def test_usuario_es_adulto():
    usuario = Usuario("Juan", 25)
    assert usuario.es_adulto() is True
    usuario = Usuario("Lucía", 17)
    assert usuario.es_adulto() is False