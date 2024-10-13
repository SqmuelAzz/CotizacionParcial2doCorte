import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.ventana import Ventana

def test_calcular_ancho_naves():
    ventana = Ventana("XO", 200, 150, "Pulido", "Transparente")
    ancho_nave, naves = ventana.calcular_ancho_naves()
    assert naves == 2
    assert ancho_nave == 100

def test_calcular_costo_total():
    ventana = Ventana("O", 120, 150, "Pulido", "Transparente")
    costo_total = ventana.calcular_costo_total()
    assert costo_total > 0  # Verifica que el costo total sea mayor a 0