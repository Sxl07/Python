#Copyright 2023 Sebastian Lopez Montenegro-Universidad De San Buenaventura Cali
from pila import * ; import random

mes=Pila()
numeroDeDias=0
def definirDias():
    numeroDeDias=int(input("digite el mes para introducir los valores promedio de temperatura (1-12):\n"))
    while numeroDeDias<1 or numeroDeDias>12:
        print("el numero digitado no está permitido, debe estar en un rango de 1 a 12")
        numeroDeDias=int(input("digite el mes para introducir los valores promedio de temperatura (1-12):\n")) 

    tamanoPila=0
    if numeroDeDias in [1,3,5,7,8,10,12]:
        print("El mes selecionado tiene 31 Dias\n")
        tamanoPila=31

    if numeroDeDias in [4,6,9,11]:
        print("El mes selecionado tiene 30 Dias\n")
        tamanoPila=30

    if numeroDeDias==2:
        print("El mes selecionado puede tener 28 o 29 Dias")
        
        n=int(input("cuantos dias quieres que tenga tu mes?\n1). 28 dias\n2). 29 dias\n"))
     
        while n!=1 and n!=2:
            print("el numero digitado no está permitido")
            n=int(input("cuantos dias quieres que tenga tu mes?\n1). 28 dias\n2). 29 dias\n"))
            
        if n==1:
            print("El mes selecionado tiene 28 Dias\n")
            tamanoPila=28
        if n==2:
            print("El mes selecionado tiene 29 Dias\n")
            tamanoPila=29
    i=0
    while i<tamanoPila:
        dato=random.randint(-60,60)
        apilar(mes,dato)
        i+=1

definirDias()
x = 0
while (x != 5):  
    x = int(input("---------Elige la opcion a ejecutar---------\n1)Determinar el rango de temperatura del mes, temperatura mínima y máxima\n2)Calcular la media de temperatura del total de valores\n3)Determinar la cantidad de valores por encima y por debajo de la media.\n4)Cambiar mes a analizar\n5)Salir\n"))
    if (x == 1):
        print("\n===========================================\n")
        maxAndMin(mes)
        print("===========================================\n")
    elif (x == 2):
        print("\n===========================================\n")
        media(mes)
        print("===========================================\n")
    elif (x == 3):
        print("\n===========================================\n")
        cantidadValores(mes)
        print("===========================================\n")
    elif (x == 4):
        eliminarPila(mes)
        definirDias()
    elif (x == 5):
        print("\nEl programa fue finalizado con exito.\n")
    else:
        x = int(input("---------Elige la opcion a ejecutar---------\n1)Determinar el rango de temperatura del mes, temperatura mínima y máxima\n2)Calcular la media de temperatura del total de valores\n3)Determinar la cantidad de valores por encima y por debajo de la media.\n4)Cambiar mes a analizar\n5)Salir\n"))