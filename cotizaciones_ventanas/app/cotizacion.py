# app/cotizacion.py
class Cotizacion:
    _instance = None

    def __init__(self, cliente, ventanas, fecha, descuento=0):
        if Cotizacion._instance is not None:
            raise Exception("Esta clase es un Singleton. Use get_instance() para obtener la instancia.")
        self.cliente = cliente
        self.ventanas = ventanas
        self.fecha = fecha
        self.descuento = descuento
        self.cantidad_ventanas = len(ventanas)
        self.numero_cotizacion = id(self)
    
    @staticmethod
    def get_instance(cliente, ventanas, fecha, descuento=0):
        if Cotizacion._instance is None:
            Cotizacion._instance = Cotizacion(cliente, ventanas, fecha, descuento)
        return Cotizacion._instance

    def calcular_total(self):
        total = sum(ventana.calcular_costo_total() for ventana in self.ventanas)
        if self.cantidad_ventanas > 100:
            total *= 0.9  # Aplicar 10% de descuento
        return total
