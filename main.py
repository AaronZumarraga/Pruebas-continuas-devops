# main.py
def add(a, b):
    """Suma dos números."""
    return a + b

def subtract(a, b):
    """Resta dos números."""
    return a - b

if __name__ == "__main__":
    print("Resultado de add(3, 5):", add(3, 5))
    print("Resultado de subtract(10, 5):", subtract(10, 5))

# Pruebas automatizadas con pytest
def test_add():
    assert add(3, 5) == 8
    assert add(-1, 1) == 0

def test_subtract():
    assert subtract(10, 5) == 5
    assert subtract(0, 4) == -4

# Para ejecutar las pruebas directamente:
if __name__ == "__main__":
    import pytest
    pytest.main(["-v"])
