empleados=[{"nombre":"juan perez","codigo":23456,"Cargo":"Gerente General"},
           {"nombre":"maria lopez","codigo":80912,"Cargo":"Jefe de Ventas"},
           {"nombre":"carlos garcia","codigo":56789,"Cargo":"Contador"},
           {"nombre":"ana martinez","codigo":12345,"Cargo":"Asistente Admin"},
           {"nombre":"luis torres","codigo":67890,"Cargo":"Director Ejecutivo"},
           {"nombre":"laura ramirez","codigo":43210,"Cargo":"Ingeniero"},
           {"nombre":"andres cruz","codigo":98765,"Cargo":"Marketing"},
           {"nombre":"sofia rojas","codigo":34567,"Cargo":"Analista de TI"}
]
#Ordenar Los Nombres Alfabeticamente--------------

def shellSort(array, n):
    interval = n // 2
    while interval > 0:
        for i in range(interval, n):
            temp = array[i]
            j = i
            while j >= interval and (((array[j - interval]["nombre"])>(temp["nombre"]))):
                array[j] = array[j - interval]
                j -= interval
            array[j]= temp
        interval //= 2
    for h in range(0,len(array)):
        print(array[h]["nombre"])

#Ordenar de menor a mayor Los codigos-------------------

def shellSort1(array, n):
    interval = n // 2
    while interval > 0:
        for i in range(interval, n):
            temp = array[i]
            j = i
            while j >= interval and (((array[j - interval]["codigo"])>(temp["codigo"]))):
                array[j] = array[j - interval]
                j -= interval
            array[j]= temp
        interval //= 2
    for h in range(0,len(array)):
        print(array[h]["codigo"],array[h]["nombre"])

#Buscar el empleado con el cargo a buscar
def centinela(lista, buscado):
    posicion = -1
    for i in lista:
        if (i["Cargo"] == buscado):
            posicion = i
            print("el cargo buscado le pertenece al empleado: ",i["nombre"])
            break
    if posicion==-1:
        print("no hay ningun empleado con el cargo buscado")
    return posicion

x=0
while (x!=4):
    x=int(input("---------elige la opcion a ejecutar---------\n1)Ordenar los nombres de los empleados\n2)Buscar el cargo de Director Ejecutivo\n3)Ordenar los codigos ascendentemente\n4)Salir\n"))
    if(x==1):
        print("\n===========================================\n")
        #impresion de la lista de los empleados alfabeticamente
        size=len(empleados)
        shellSort(empleados,size)
        print("\n===========================================\n")
        
    elif (x==2):
        print("\n===========================================\n")
        #impresion del cargo a buscar
        buscado="Director Ejecutivo"
        centinela(empleados,buscado)
        print("\n===========================================\n")
 
    elif(x==3):
        print("\n===========================================\n")
        #impresion de la lista de los codigos ascedentemente
        size1=len(empleados)
        shellSort1(empleados,size1)
        print("\n===========================================\n")
        
    elif(x==4):
        print("\nEl programa fue finalizado con exito.\n")

    else:
        x=int(input("---------elige la opcion a ejecutar---------\n1)Ordenar los nombres de los empleados\n2)Buscar el cargo de Director Ejecutivo\n3)Ordenar los codigos ascendentemente\n4)Salir\n"))
