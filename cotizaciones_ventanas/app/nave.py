# app/nave.py
from vidrio import Vidrio
from acabado import Acabado

class Nave:
    def __init__(self, tipo_nave, ancho, alto, tipo_vidrio, tipo_acabado, esmerilado=False):
        self.tipo_nave = tipo_nave
        self.ancho = ancho
        self.alto = alto
        self.vidrio = Vidrio(tipo_vidrio)
        self.acabado = Acabado(tipo_acabado)
        self.esmerilado = esmerilado

    def calcular_costo_vidrio(self):
        area = (self.ancho - 1.5) * (self.alto - 1.5)
        costo_vidrio = area * self.vidrio.precio_por_cm2
        if self.esmerilado:
            costo_vidrio += area * 5.20
        return costo_vidrio

    def calcular_costo_acabado(self):
        perimetro = 2 * (self.ancho + self.alto) - 4 * 1.5
        return perimetro * self.acabado.precio_por_metro_lineal

    def calcular_costo_total(self):
        return self.calcular_costo_vidrio() + self.calcular_costo_acabado()
