import random
import numpy as np

print("Uber Simulation")

#Entorno
class Entorno():
    x_minimo = 0
    x_maximo = 0
    y_minimo = 0
    y_maximo = 0
    
    def __init__(self, M, N, cuantos_usuarios, cuantos_vehiculos):
        self.usuarios = []
        self.y_maximo = M
        self.x_maximo = N
        for i in range(cuantos_usuarios):
            self.usuarios.append(Usuario(i, random.randrange(self.x_minimo, self.x_maximo), random.randrange(self.y_minimo, self.y_maximo), random.randrange(self.x_minimo, self.x_maximo), random.randrange(self.y_minimo, self.y_maximo), self))
        self.vehiculos = []
        for i in range(cuantos_vehiculos):
            self.vehiculos.append(Vehiculo(i, random.randrange(self.x_minimo, self.x_maximo), random.randrange(self.y_minimo, self.y_maximo), random.randrange(self.x_minimo, self.x_maximo), random.randrange(self.y_minimo, self.y_maximo), self))
        self.matriz = self.crear_cuadricula(M, N)

    def crear_cuadricula(self, M,N):
        arr=[]
        id_celda=1
        for i in range(M):
            current_line=[]
            for j in range(N):
                current_line.append([id_celda])
                id_celda+=1
            arr.append(current_line)
        return arr
    
    def printMatriz(self,):
        ## Actualiza Entorno
        self.matriz = self.crear_cuadricula(self.y_maximo, self.x_maximo)
        print("")
        print("Usuarios")
        for i in range(len(self.usuarios)):
            print("pos_x: " + str(self.usuarios[i].x), end=' ')
            print("pos_y: " + str(self.usuarios[i].y), end=' ')
            print("destino: ", end=' ')
            print(self.usuarios[i].destino, end=' ')
            print("libre: " + str(self.usuarios[i].libre), end=' ')
            print("vehiculo_asignado: " + str(self.usuarios[i].vehiculo_asignado), end=' ')
            print("")
            self.matriz[self.y_maximo - self.usuarios[i].y - 1][self.usuarios[i].x].append("u"+str(i))
        print("")
        print("Vehiculos")
        for i in range(len(self.vehiculos)):
            print("pos_x: " + str(self.vehiculos[i].x), end=' ')
            print("pos_y: " + str(self.vehiculos[i].y), end=' ')
            print("destino: ", end=' ')
            print(self.vehiculos[i].destino, end=' ')
            print("libre: " + str(self.vehiculos[i].libre), end=' ')
            print("cliente_asignado: " + str(self.vehiculos[i].cliente_asignado), end=' ')
            print("trae_pasaje: " + str(self.vehiculos[i].trae_pasaje), end=' ')
            print("ultimo_pasajero: " + str(self.vehiculos[i].ultimo_pasajero), end=' ')
            print("")
            self.matriz[self.y_maximo - self.vehiculos[i].y - 1][self.vehiculos[i].x].append("v"+str(i))
        print("")
        print("MATRIZ")
        for i in range(self.y_maximo):
            for j in range(self.x_maximo):
                print(self.matriz[i][j], end='')
            print("")


#Agentes jerárquicos
class Uber():
    
    def __init__(self, entorno):
        self.historial_estados_vehiculos_usuarios = []
        self.entorno = entorno

    ## Paso del tiempo 
    def PasoTiempo(self, T):
        for i in range(T):
            self.asignarVehiculosAUsuarios()
            print("_____________________")
            print("TIEMPO " + str(i) + " ASIGNACION HECHA")
            self.entorno.printMatriz()
            print("_____________________")
            self.moverVehiculos()
            print("_____________________")
            print("TIEMPO " + str(i) + " SE MOVIERON VEHICULOS")
            self.entorno.printMatriz()
            print("_____________________")
    
    def asignarVehiculosAUsuarios(self,):
        for i in range(len(self.entorno.vehiculos)):
            if (self.entorno.vehiculos[i].libre==1):
                for j in range(len(self.entorno.usuarios)):
                    if (self.entorno.usuarios[j].libre==1 and self.entorno.vehiculos[i].ultimo_pasajero != j):
                        self.entorno.vehiculos[i].asignar(j)
                        self.entorno.usuarios[j].asignar(i)
                        break
    
    def moverVehiculos(self,):
        for i in range(len(self.entorno.vehiculos)):
            ## Avanzar vehiculo una unidad
            self.entorno.vehiculos[i].avanzar_unidad_cuadricula()

    #Comunicacion
    def contacto_entorno(self,):
        #El agente líder, tiene contacto con el entorno para obtener lalectura de las posiciones de los usuarios y el destino al que quieren llegar.
        return (self.entorno.usuarios, self.entorno.vehiculos)


class Vehiculo():
    def __init__(self, id, x, y, destino_x, destino_y, entorno):
        self.id = id
        self.x = x
        self.y = y
        self.destino = {"x":destino_x, "y":destino_y }
        self.libre = 1
        self.cliente_asignado = -1
        self.recoger_cliente = -1
        self.trae_pasaje = -1
        self.entorno = entorno
        self.ultimo_pasajero = -1

    def avanzar_unidad_cuadricula(self,):
        if self.x > self.destino["x"]:
            self.x -= 1
        elif self.x < self.destino["x"]:
            self.x += 1
        elif self.y > self.destino["y"]:
            self.y -= 1
        elif self.y < self.destino["y"]:
            self.y += 1
            
        ## Si trae pasaje
        if self.trae_pasaje == 1:
            self.entorno.usuarios[self.cliente_asignado].x = self.x
            self.entorno.usuarios[self.cliente_asignado].y = self.y
        
        ## Si llego a su destino
        if self.x == self.destino["x"] and self.y == self.destino["y"]:
            if (self.recoger_cliente):
                self.destino = self.entorno.usuarios[self.cliente_asignado].destino
                self.recoger_cliente = 0
                self.trae_pasaje = 1
            else:
                self.libre = 1
                self.entorno.usuarios[self.cliente_asignado].generarNuevoDestino()
                self.entorno.usuarios[self.cliente_asignado].libre = 1
                self.ultimo_pasajero = self.cliente_asignado
                self.cliente_asignado = -1
                self.trae_pasaje=0
   
    def asignar(self, usuario):
        self.cliente_asignado = usuario
        self.destino = {"x":self.entorno.usuarios[usuario].x, "y":self.entorno.usuarios[usuario].y}
        self.recoger_cliente = 1
        self.libre = 0

class Usuario():
    def __init__(self, id, x, y, destino_x, destino_y, entorno):
        self.id = id
        self.x = x
        self.y = y
        self.destino = {"x":destino_x, "y":destino_y }
        self.libre = 1
        self.vehiculo_asignado = 0
        self.entorno = entorno

    def asignar(self, vehiculo):
        self.vehiculo_asignado = vehiculo
        self.libre = 0

    def generarNuevoDestino(self, ):
        self.destino = {"x":random.randrange(self.entorno.x_minimo, self.entorno.x_maximo), "y":random.randrange(self.entorno.y_minimo, self.entorno.y_maximo) }
e = Entorno(5, 5, 2, 2)
print("_____________________")
print("ESTADO INICIAL")
e.printMatriz()
print("_____________________")
ub = Uber(e)
ub.PasoTiempo(15)


