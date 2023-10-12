"""Sebastian Lopez
Juan Pablo Silvestre
Tomas Mancera
Alejandro Salazar"""

import random

def crear_tabla_hash_anual():
    tabla_hash_meteorologica = {}
    meses = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
    horas = [str(i).zfill(2) for i in range(24)]
    
    for mes in meses:
        for dia in range(1, 32):
            for hora in horas:
                clave = f"{mes}_{str(dia).zfill(2)}_{hora}"
                tabla_hash_meteorologica[clave] = None  # Inicializa con un valor vacío
    
    return tabla_hash_meteorologica

def crear_estacion_meteorologica(nombre_estacion, pais,latitud, longitud, altitud):
    estacion = {
        'Nombre':nombre_estacion,
        'País': pais,
        'Latitud':latitud,
        'Longitud': longitud,
        'Altitud': altitud,
        'Datos Meteorológicos': crear_tabla_hash_anual()
    }
    return estacion

# Función para ingresar datos meteorológicos en una clave específica
def ingresar_datos_meteorologicos(estacion, clave, temperatura, presion, humedad, estado_clima):
    if clave in estacion['Datos Meteorológicos']:
        estacion['Datos Meteorológicos'][clave] = {
            'Temperatura': temperatura,
            'Presión': presion,
            'Humedad': humedad,
            'Estado del Clima': estado_clima
        }
    else:
        print("Clave no válida.")

estacion1 = crear_estacion_meteorologica("Estacion1", "Colombia",-74.645, 42.2321, 500)
estacion2 = crear_estacion_meteorologica("Estacion2", "Noruega",76.23, 23.644, 120)
estacion3 = crear_estacion_meteorologica("Estacion3", "Japon",75.322, 32.12, 40)
estaciones=[estacion1,estacion2,estacion3]

def calcular_promedio_por_mes(estacion, mes):
    total_temperatura = 0
    total_humedad = 0
    cantidad_registros = 0

    tabla_hash = estacion['Datos Meteorológicos']
    
    for clave, registro in tabla_hash.items():
        if clave.startswith(mes):
            if registro is not None:
                total_temperatura += registro['Temperatura']
                total_humedad += registro['Humedad']
                cantidad_registros += 1

    if cantidad_registros > 0:
        promedio_temperatura = total_temperatura / cantidad_registros
        promedio_humedad = total_humedad / cantidad_registros
        return promedio_temperatura, promedio_humedad
    else:
        return None
    
def ubicar_estaciones_por_estado_clima(estaciones, estado_clima):
    estaciones_con_estado_clima = []

    for estacion in estaciones:
        tabla_hash = estacion['Datos Meteorológicos']
        for clave, registro in tabla_hash.items():
            if registro is not None and registro['Estado del Clima'] == estado_clima:
                estaciones_con_estado_clima.append(estacion)
                break  

    return estaciones_con_estado_clima
print("Recuerde primero registrar por lo menos un dato")
x=0
while x!=4:
    x=int(input("Digite la opcion:\n1)Registre los datos meteorologicos por fecha y hora\n2)Calcular promedio de tempratura y humedad mensual\n3)Buscar Estaciones por estado de clima\n4)Salir.\n"))
    if x==1:
        e=int(input("Digite el correspondiente a la Estacion\n1)Estacion 1(Colombia)\n2)Estacion 2(Noruega)\n3)Estacion 3(Japon)\n"))
        mes=int(input("Digite el mes del año\n"))
        dia=int(input("Digite el dia del mes\n"))
        hora=int(input("Digite la hora del dia(0-23)\n"))
        clave_ingreso=""
        estado_clima_ingreso=""
        if mes < 1 or mes > 12 or dia < 1 or dia > 31 or hora < 0 or hora > 23:
            print("Valores de entrada no válidos. Asegúrate de que el mes esté entre 1 y 12, el día entre 1 y 31, y la hora entre 0 y 23.")
        else:
            clave_ingreso = f"{mes:02d}_{dia:02d}_{hora:02d}" 
            
        temperatura_ingreso = float(input(f"Ingrese la temperatura en la hora {hora}:\n"))
        presion_ingreso = float(input(f"Ingrese la presion en la hora {hora}:\n"))
        humedad_ingreso = float(input(f"Ingrese la humedad en la hora {hora}:\n"))
        estado_clima = int(input("Digite el numero correspondiente al estado de clima:\n1)soleado\n2)nublado\n3)lloviendo\n4)nevando\n"))
        
        if estado_clima==1:
            estado_clima_ingreso="soleado"
        if estado_clima==2:
            estado_clima_ingreso="nublado"
        if estado_clima==3:
            estado_clima_ingreso="lloviendo"
        if estado_clima==4:
            estado_clima_ingreso="nevando"
        
        if e==1:
            ingresar_datos_meteorologicos(estacion1, clave_ingreso, temperatura_ingreso, presion_ingreso, humedad_ingreso, estado_clima_ingreso)
        elif e==2:
            ingresar_datos_meteorologicos(estacion2, clave_ingreso, temperatura_ingreso, presion_ingreso, humedad_ingreso, estado_clima_ingreso)
        if e==3:
            ingresar_datos_meteorologicos(estacion3, clave_ingreso, temperatura_ingreso, presion_ingreso, humedad_ingreso, estado_clima_ingreso)
            
        print("Registro exitoso")
    elif x==2:
        mes_a_calcular = input("Ingrese el mes (en formato MM) para calcular el promedio de temperatura y humedad por estación: \n")

        for estacion in estaciones:
            promedio = calcular_promedio_por_mes(estacion, mes_a_calcular)
            if promedio is not None:
                promedio_temperatura, promedio_humedad = promedio
                print("-"*25)
                print(f"Promedio de temperatura para {estacion['Nombre']} en el mes {mes_a_calcular}: {promedio_temperatura:.2f}")
                print(f"Promedio de humedad para {estacion['Nombre']} en el mes {mes_a_calcular}: {promedio_humedad:.2f}")
            else:
                print("-"*25)
                print(f"No hay datos disponibles para {estacion['Nombre']} en el mes {mes_a_calcular}.")
    elif x==3:
        estado_clima_a_buscar=""
        estado_clima= int(input("Digite el numero correspondiente al estado de clima:\n1)soleado\n2)nublado\n3)lloviendo\n4)nevando\n"))
        if estado_clima==1:
            estado_clima_a_buscar="soleado"
        if estado_clima==2:
            estado_clima_a_buscar="nublado"
        if estado_clima==3:
            estado_clima_a_buscar="lloviendo"
        if estado_clima==4:
            estado_clima_a_buscar="nevando"
        estaciones_con_estado_clima = ubicar_estaciones_por_estado_clima(estaciones, estado_clima_a_buscar)

        if estaciones_con_estado_clima:
            print("-"*25)
            print(f"Estaciones con estado de clima '{estado_clima_a_buscar}':")
            for estacion in estaciones_con_estado_clima:
                print(estacion['Nombre'])
        else:
            print(f"No se encontraron estaciones con estado de clima '{estado_clima_a_buscar}'.")
    elif x==4:
        print("-"*25)
        print("El programa fue finalizado con exito")
    else:
        print("El numero digitado no está permitido")
