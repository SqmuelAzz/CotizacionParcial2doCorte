# app/ventana.py
from nave import Nave

class Ventana:
    def __init__(self, estilo, ancho, alto, acabado, tipo_vidrio, esmerilado=False):
        self.estilo = estilo
        self.ancho = ancho
        self.alto = alto
        self.acabado = acabado
        self.tipo_vidrio = tipo_vidrio
        self.esmerilado = esmerilado
        self.naves = self.crear_naves()

    def crear_naves(self):
        estilo_naves = {
            "O": 1,
            "XO": 2,
            "OXO": 3,
            "OXXO": 4,
        }
        naves = estilo_naves[self.estilo]
        ancho_nave = self.ancho / naves
        return [Nave("X" if i % 2 else "O", ancho_nave, self.alto, self.tipo_vidrio, self.acabado, self.esmerilado) for i in range(naves)]

    def calcular_costo_total(self):
        return sum(nave.calcular_costo_total() for nave in self.naves)
