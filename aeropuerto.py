"""Sebastian Lopez
   Juan Pablo Silvestre
   Alejandro Salazar
   Tomas Mancera

   este codigo nos sacó canas :(
   """

import time
import datetime
class vuelo(object):
    def __init__(self,aerolinea,horaSalida,horaLlegada,aeropuertoOrigen,aeropuertoDestino,tipoVuelo):
        self.aerolinea=aerolinea
        self.horaSalida=horaSalida
        self.horaLlegada=horaLlegada
        self.aeropuertoOrigen=aeropuertoOrigen
        self.aeropuertoDestino=aeropuertoDestino
        self.tipoVuelo=tipoVuelo

class nodoCola(object):
    info,sig=None,None

class Cola(object):
    def __init__(self):
        self.frente,self.final=None,None
        self.tamano=0

def arribo(cola,dato):
    nodo=nodoCola()
    nodo.info=dato
    if cola.frente is None:
        cola.frente=nodo
    else:
        cola.final.sig=nodo
    cola.final=nodo
    cola.tamano+=1

def atencion(cola):
    dato=cola.frente.info
    cola.frente=cola.frente.sig
    if cola.frente is None:
        cola.final=None
    cola.tamano-=1
    return dato

def cola_vacia(cola):
    return cola.frente is None

def en_frente(cola):
    return cola.frente.info

def tamano(cola):
    return cola.tamano
    
def mover_al_final(cola):
    dato=atencion(cola)
    arribo(cola,dato)
    return dato

def barrido(cola):
    caux=Cola()
    while(not cola_vacia(cola)):
        dato=atencion(cola)
        print(dato)
        arribo(caux,dato)
    while(not cola_vacia(caux)):
        dato=atencion(caux)
        arribo(cola,dato)
        
def barrido_moverfinal(cola):
    i=0
    while(i<tamano(cola)):
        dato=mover_al_final(cola)
        print(dato)
        i+=1

cola_despegues = Cola()
cola_aterrizajes = Cola()

def agregar_despegue(cola_despegues):
    aerolinea = input("Ingrese la aerolínea: ")
    hora_salida = input("Ingrese la hora de salida (formato HH:MM): ")
    aeropuerto_origen = input("Ingrese el aeropuerto de origen: ")
    aeropuerto_destino = input("Ingrese el aeropuerto de destino: ")
    tipo_vuelo = input("Ingrese el tipo de vuelo (pasajeros/carga): ")
    avion = vuelo(aerolinea, hora_salida, None, aeropuerto_origen, aeropuerto_destino, tipo_vuelo)
    arribo(cola_despegues, avion)
    print("El vuelo para despegue fue agregado con exito")

def agregar_aterrizaje(cola_aterrizajes):
    aerolinea = input("Ingrese la aerolínea: ")
    hora_llegada = input("Ingrese la hora de llegada (formato HH:MM): ")
    aeropuerto_origen = input("Ingrese el aeropuerto de origen: ")
    aeropuerto_destino = input("Ingrese el aeropuerto de destino: ")
    tipo_vuelo = input("Ingrese el tipo de vuelo (pasajeros/carga): ")
    avion = vuelo(aerolinea, None, hora_llegada, aeropuerto_origen, aeropuerto_destino, tipo_vuelo)
    arribo(cola_aterrizajes, avion)
    print("El vuelo para aterrizaje fue agregado con exito")

def atender_vuelo(cola_despegues, cola_aterrizajes):
    if not cola_vacia(cola_aterrizajes):
        if not cola_vacia(cola_despegues):
            if cola_aterrizajes.frente.info.horaLlegada <= cola_despegues.frente.info.horaSalida:
                avion = atencion(cola_aterrizajes)
                print("Atendiendo vuelo de aterrizaje:", avion.aerolinea, avion.horaLlegada, avion.aeropuertoOrigen, avion.aeropuertoDestino, avion.tipoVuelo)
            else:
                avion = atencion(cola_despegues)
                print("Atendiendo vuelo de despegue:", avion.aerolinea, avion.horaSalida, avion.aeropuertoOrigen, avion.aeropuertoDestino, avion.tipoVuelo)
        else:
            avion = atencion(cola_aterrizajes)
            print("Atendiendo vuelo de aterrizaje:", avion.aerolinea, avion.horaLlegada, avion.aeropuertoOrigen, avion.aeropuertoDestino, avion.tipoVuelo)
    elif not cola_vacia(cola_despegues):
        avion = atencion(cola_despegues)
        print("Atendiendo vuelo de despegue:", avion.aerolinea, avion.horaSalida, avion.aeropuertoOrigen, avion.aeropuertoDestino, avion.tipoVuelo)
    else:
        print("No hay vuelos para atender")
        return

    if avion.tipoVuelo.lower() == "pasajeros":
        if not cola_vacia(cola_despegues) and cola_despegues.frente.info.tipoVuelo.lower() == "pasajeros":
            tiempo_espera = (datetime.strptime(cola_despegues.frente.info.horaSalida, "%H:%M") - datetime.strptime(avion.horaLlegada, "%H:%M")).seconds
            if tiempo_espera > 7:
                print("El vuelo ha esperado", tiempo_espera, "segundos")
            else:
                time.sleep(7 - tiempo_espera)
                print("El vuelo ha despegado con éxito")
        else:
            time.sleep(7)
            print("El vuelo ha despegado con éxito")
    else:
        if not cola_vacia(cola_despegues) and cola_despegues.frente.info.tipoVuelo.lower() == "carga":
            tiempo_espera = (datetime.strptime(cola_despegues.frente.info.horaSalida, "%H:%M") - datetime.strptime(vuelo.horaLlegada, "%H:%M")).seconds
            if tiempo_espera > 11:
                print("El vuelo ha esperado", tiempo_espera, "segundos")
            else:
                time.sleep(11 - tiempo_espera)
                print("El vuelo ha aterrizado con éxito")
        else:
            time.sleep(11)
            print("El vuelo ha aterrizado con éxito")

def cancelar_vuelo_despegue(cola_despegues):
    if not cola_vacia(cola_despegues):
        vuelo_cancelado = atencion(cola_despegues)
        print("Vuelo de despegue cancelado:", vuelo_cancelado.aerolinea, vuelo_cancelado.horaSalida, vuelo_cancelado.aeropuertoOrigen, vuelo_cancelado.aeropuertoDestino, vuelo_cancelado.tipoVuelo)
    else:
        print("No hay vuelos de despegue para cancelar")


opcion=0
while opcion!=5:
    try:
        opcion = int(input("---------Elige la opción a ejecutar---------\n1) Agregar vuelo de despegue\n2) Agregar vuelo de aterrizaje\n3) Atender vuelo\n4) Cancelar vuelo de despegue\n5) Finalizar Ejecucion\n"))
    except ValueError:
        print("El dato ingresado no está permitido")
    if opcion == 1:
        agregar_despegue(cola_despegues)
    elif opcion == 2:
        agregar_aterrizaje(cola_aterrizajes)
    elif opcion == 3:
        atender_vuelo(cola_despegues, cola_aterrizajes)
    elif opcion == 4:
        cancelar_vuelo_despegue(cola_despegues)
    elif opcion == 5:
        print("El programa ha sido finalizado con exito")
    else:
        print("Opción inválida")