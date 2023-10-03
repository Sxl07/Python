class nodoPila(object):
    info,sig=None, None

class Pila(object):
    def __init__(self):
        self.cima=None
        self.tamano=0

def apilar(pila,dato):
    nodo=nodoPila()
    nodo.info=dato
    nodo.sig=pila.cima
    pila.cima=nodo
    pila.tamano+=1

def desapilar(pila):
    x=pila.cima.info
    pila.cima=pila.cima.sig
    pila.tamano-=1
    return x

def pila_vacia(pila):
    return pila.cima is None

def en_cima(pila):
    if pila.cima is not None:
        return pila.cima.info
    else:
        return None

def tamano(pila):
    return pila.tamano

def barrido(pila):
    paux=Pila()
    while(not pila_vacia(pila)):
        dato=desapilar(pila)
        print(dato)
        apilar(paux,dato)
    while(not pila_vacia(paux)):
        dato=desapilar(paux)
        apilar(pila,dato)

def eliminarPila(pila):
    pila.cima=None

def maxAndMin(pila):
    max,min=0,0
    paux=Pila()
    while(not pila_vacia(pila)):
        dato=desapilar(pila)
        if dato>max:
            max=dato
        if dato<min:
            min=dato
        apilar(paux,dato)
    print(f"El rango del mes es de {min}°C hasta {max}°C\nMax:{max}°C\nMin:{min}°C\n")
    while(not pila_vacia(paux)):
        dato=desapilar(paux)
        apilar(pila,dato)

def media(pila):
    sumatoria=0
    media=0.0
    paux=Pila()
    tamanio=tamano(pila)
    while(not pila_vacia(pila)):
        dato=desapilar(pila)
        sumatoria+=dato
        apilar(paux,dato)
    media=round(sumatoria/tamanio,2)
    print(f"La media de temperatura del total de valores es:\n{media}°C\n")
    while(not pila_vacia(paux)):
        dato=desapilar(paux)
        apilar(pila,dato)

def cantidadValores(pila):
    debajo=0
    encima=0
    sumatoria=0
    media=0.0
    paux=Pila()
    tamanio=tamano(pila)
    while(not pila_vacia(pila)):
        dato=desapilar(pila)
        sumatoria+=dato
        apilar(paux,dato)
    media=round(sumatoria/tamanio,2)
    while(not pila_vacia(paux)):
        dato=desapilar(paux)
        if dato<media:
            debajo+=1
        if dato>=media:
            encima+=1
        apilar(pila,dato)
    print(f"La cantidad de valores por debajo de la media({media}°C) es:\n{debajo}\n")
    print(f"La cantidad de valores por encima de la media({media}°C) es:\n{encima}\n")