from operaciones import sumar, multiplicar
import pytest

# Los decoradores o marcas nos dan diferentes utilidades. En este casonos permite correr el scrip sin usar el test
#pytest.mark.skip(reason="no deseo hacer el test")

@pytest.mark.marca1
def test_sumar():
    assert sumar(2,5) == 4
    
@pytest.mark.marca1
def test_sumar2():
    assert sumar(2,2) == 4



#Permite hacer multiples pruebas en un mismo test.
@pytest.mark.parametrize(
    "a, b, resultado", 
    [
        (1, 2, 2), 
        (3, 2, 6), 
        (3, 2, 7),
        (3, 3, 9)
    ]
)

@pytest.mark.marca2
def test_multiplicar(a, b, resultado):
    assert multiplicar (a, b) == resultado