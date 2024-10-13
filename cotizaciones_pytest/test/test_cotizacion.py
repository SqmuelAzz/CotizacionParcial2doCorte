import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.cotizacion import Cotizacion
from app.ventana import Ventana
from app.cliente import Cliente

def test_calcular_total_sin_descuento():
    cliente = Cliente("Ana Gómez", "Construcciones", 50)
    ventanas = [Ventana("O", 120, 150, "Pulido", "Transparente") for _ in range(50)]
    cotizacion = Cotizacion(cliente, ventanas)
    total = cotizacion.calcular_total()
    assert total > 0  # Verifica que se calcule un total mayor a 0

def test_calcular_total_con_descuento():
    cliente = Cliente("Ana Gómez", "Construcciones", 120)
    ventanas = [Ventana("O", 120, 150, "Pulido", "Transparente") for _ in range(120)]
    cotizacion = Cotizacion(cliente, ventanas)
    total_con_descuento = cotizacion.calcular_total()
    total_sin_descuento = sum(ventana.calcular_costo_total() for ventana in ventanas)
    assert total_con_descuento < total_sin_descuento  # Verifica que aplique el descuento