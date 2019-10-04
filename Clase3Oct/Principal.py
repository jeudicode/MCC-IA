import Agente
import Entorno
import Grafica

entorno = Entorno(20)
agente = Agente(entorno)
grafica = Grafica(agente, entorno)

agente.ejecutar_acciones(100)
grafica.graficar()