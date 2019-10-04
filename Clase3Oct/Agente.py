class Agente():
    def __init__(self, entorno):
        self.entorno = entorno
        
        lectura = entorno.estado_inicial()
        self.promedio = self.ultimo_precio = lectura["precio"]
        self.inventario = lectura["inventario"]
    
    def ejecutar_acciones(self, n):
        for i in range(n):
            if self.ultimo_precio < 0.9 * self.promedio and self.inventario < 60:
                por_comprar = 48
            elif self.inventario < 12:
                por_comprar = 12
            else:
                por_comprar = 0
        
            lectura = self.entorno.paso(por_comprar)
            self.ultimo_precio = lectura["precio"]
            self.promedio += (self.ultimo_precio-self.promedio) * 0.05
            self.inventario = lectura["inventario"]