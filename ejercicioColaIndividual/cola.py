class nodoCola(object):
    info,sig=None,None

class Cola(object):
    def __init__(self):
        self.frente,self.final=None,None
        self.name=""
        self.tamano=0
        self.recaudo=0

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

def cobrar(cola):
    autosAtendidos={
    "automoviles":0,
    "camionetas":0,
    "camiones":0,
    "colectivos":0
    }

    precioPeaje={
    "automoviles": 47,
    "camionetas": 59,
    "camiones": 71,
    "colectivos": 64
    }
    caux=Cola()
    recaudo=0
    while(not cola_vacia(cola)):
        enAtencion=atencion(cola)
        autosAtendidos[enAtencion]+=1
        recaudo+=precioPeaje[enAtencion]
        arribo(caux,enAtencion)
    while(not cola_vacia(caux)):
        enAtencion=atencion(caux)
        arribo(cola,enAtencion)
    return recaudo

def imprimirVehiculos(cola):
    autosAtendidos={
    "automoviles":0,
    "camionetas":0,
    "camiones":0,
    "colectivos":0
    }

    precioPeaje={
    "automoviles": 47,
    "camionetas": 59,
    "camiones": 71,
    "colectivos": 64
    }
    caux=Cola()
    recaudo=0
    while(not cola_vacia(cola)):
        enAtencion=atencion(cola)
        autosAtendidos[enAtencion]+=1
        recaudo+=precioPeaje[enAtencion]
        arribo(caux,enAtencion)
    print(f"El numero de autos atendidos en la {cola.name} es:")
    for enAtencion,cantidad in autosAtendidos.items():
        print(f"{enAtencion} : {cantidad}")
    while(not cola_vacia(caux)):
        enAtencion=atencion(caux)
        arribo(cola,enAtencion)
    return recaudo

def limpiarCola(cola):
    cola.frente=None
    cola.final=None