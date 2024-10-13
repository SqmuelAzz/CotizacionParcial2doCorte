# app/acabado.py
class Acabado:
    def __init__(self, tipo):
        precios = {
            "Pulido": 50700 / 100,
            "Lacado Brillante": 54200 / 100,
            "Lacado Mate": 53600 / 100,
            "Anodizado": 57300 / 100
        }
        self.tipo = tipo
        self.precio_por_metro_lineal = precios.get(tipo, 0)
