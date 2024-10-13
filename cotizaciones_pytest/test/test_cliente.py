import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.cliente import Cliente

def test_cliente_attributes():
    cliente = Cliente("Juan Pérez", "Ventanas SA", 150)
    assert cliente.nombre == "Juan Pérez"
    assert cliente.empresa == "Ventanas SA"
    assert cliente.cantidad_ventanas == 150