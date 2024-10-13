# app/vidrio.py
class Vidrio:
    def __init__(self, tipo):
        precios = {
            "Transparente": 8.25,
            "Bronce": 9.15,
            "Azul": 12.75
        }
        self.tipo = tipo
        self.precio_por_cm2 = precios.get(tipo, 0)
