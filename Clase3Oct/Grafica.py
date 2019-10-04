import matplotlib.pyplot as plt

class Grafica():
    def __init__(self, agente, entorno):
        self.agente = agente
        self.entorno = entorno
        plt.xlabel("Tiempo")
        plt.ylabel("Inventario                          Precio")

    def graficar(self):
        num = len(self.entorno.historial_inventario)
        plt.plot(range(num), self.entorno.historial_inventario, label="Inventario")
        plt.plot(range(num), self.entorno.historial_precio, label="Precio")
        plt.show()