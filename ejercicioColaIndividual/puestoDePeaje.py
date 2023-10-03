#Copyright 2023 Sebasian Lopez Montenegro - Universidad de San Buenaventura Cali
from cola import * ; import random

cabinaDeCobro1=Cola()
cabinaDeCobro1.name="Cabina de cobro 1"
cabinaDeCobro2=Cola()
cabinaDeCobro2.name="Cabina de cobro 2"
cabinaDeCobro3=Cola()
cabinaDeCobro3.name="Cabina de cobro 3"

def llenarCola():
    tiposDeAutos={
        1:"automoviles",
        2:"camionetas",
        3:"camiones",
        4:"colectivos"
    }
    for i in range(30):
        cabina=random.randint(1,3)
        if cabina==1:
            arribo(cabinaDeCobro1,tiposDeAutos[random.randint(1,4)])
        if cabina==2:
            arribo(cabinaDeCobro2,tiposDeAutos[random.randint(1,4)])
        if cabina==3:
            arribo(cabinaDeCobro3,tiposDeAutos[random.randint(1,4)])

def mayorRecaudo(recaudo1,recaudo2,recaudo3):
    if recaudo1>recaudo2:
        if recaudo1>recaudo3:
            print(f"El mayor recaudo fue hecho por la {cabinaDeCobro1.name} y es: ${recaudo1}")
        else:
            print(f"El mayor recaudo fue hecho por la {cabinaDeCobro3.name} y es: ${recaudo3}")
    else:
        if recaudo2>recaudo3:
            print(f"El mayor recaudo fue hecho por la {cabinaDeCobro2.name} y es: ${recaudo2}")
        else:
            print(f"El mayor recaudo fue hecho por la {cabinaDeCobro3.name} y es: ${recaudo3}")

llenarCola()
x = 0
count=1
while (x != 5): 
    try:
        x = int(input("\n---------Elige la opcion a ejecutar---------\n1)Realizar la atención de las cabinas\n2)Determinar qué cabina recaudó mayor cantidad de pesos \n3)Determinar cuántos vehículos de cada tipo se atendieron en cada cola.\n4)Generar Nueva Tanda de pagos de peaje(repetir proceso con otros 30 vehiculos)\n5)Salir\n"))
    except ValueError:
        print("El dato ingresado no es de tipo entero")
    if (x == 1):
        if count==1:
            print("="*60)
            recaudo1=cobrar(cabinaDeCobro1)
            recaudo2=cobrar(cabinaDeCobro2)
            recaudo3=cobrar(cabinaDeCobro3)
            print("Cobro Realizado con Exito.")
            print("="*60)
        elif count!=1:
            print("="*60)
            print("El cobro ya fue realizado anteriormente")
            print("="*60)
        count+=1
    elif (x == 2):
        print("="*60)
        try:
            mayorRecaudo(recaudo1,recaudo2,recaudo3)
        except NameError:
            print("Recuerda cobrar primero antes de pedir el mayor recaudo")
        print("="*60)
    elif (x == 3):
        if count==1:
            print("="*60)
            print("Recuerda cobrar primero antes de pedir los carros atendidos")
            print("="*60)
        else:
            print("="*60)
            imprimirVehiculos(cabinaDeCobro1)
            print("="*60)
            imprimirVehiculos(cabinaDeCobro2)
            print("="*60)
            imprimirVehiculos(cabinaDeCobro3)
            print("="*60)
    elif (x == 4):
        limpiarCola(cabinaDeCobro1)
        limpiarCola(cabinaDeCobro2)
        limpiarCola(cabinaDeCobro3)
        llenarCola()
        print("="*60)
        print("Se han generado 30 vehiculos nuevos para realizar el proceso")
        print("="*60)
    elif (x == 5):
        print("\nEl programa fue finalizado con exito.\n")
    else:
        try:
            x = int(input("\n---------Elige la opcion a ejecutar---------\n1)Realizar la atención de las cabinas\n2)Determinar qué cabina recaudó mayor cantidad de pesos \n3)Determinar cuántos vehículos de cada tipo se atendieron en cada cola.\n4)Generar Nueva Tanda de pagos de peaje(repetir proceso con otros 30 vehiculos)\n5)Salir\n"))
        except ValueError:
            print("El dato ingresado no es de tipo entero")