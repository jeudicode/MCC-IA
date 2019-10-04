import random

class Entorno():
    precio_minimo = 230
    precio_maximo = 320
    usados_minimo = 0
    usados_maximo = 6
    
    def __init__(self, inventario_inicial):
        self.t = 0
        self.historial_inventario = []
        self.historial_precio = []
        
        self.inventario = inventario_inicial

    def estado_inicial(self):
        self.historial_inventario.append(self.inventario)
        precio = random.randrange(self.precio_minimo, self.precio_maximo)
        self.historial_precio.append(precio)
        return {"precio": precio, "inventario": self.inventario}
    
    def paso(self, cantidad_compra):
        self.t += 1
        usados = random.randrange(self.usados_minimo, self.usados_maximo)
        self.inventario = self.inventario - usados + cantidad_compra

        self.historial_inventario.append(self.inventario)
        precio = random.randrange(self.precio_minimo, self.precio_maximo)
        self.historial_precio.append(precio)
        return {"precio": precio, "inventario": self.inventario}