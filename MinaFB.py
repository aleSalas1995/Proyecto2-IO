import time
import argparse

#Variables globales
global filas
global columnas
global solucion

#Funcion main que recibe la matriz y el numero de iteraciones
def iniciarFuerzaBruta(minaDeOro,iteraciones):
    #Variables globales
    global filas
    global columnas

    #Ejemplos
    #minaDeOro = [[1,3,3],[2,1,4],[0,6,4]]
    #minaDeOro = [[10, 33, 13, 15],[22, 21, 0, 1],[5, 0, 2, 3],[0, 6, 14, 2]]
    #minaDeOro = [[1, 3, 1, 5],[2, 2, 4, 1],[5, 0, 2, 3],[0, 6, 1, 2]]

    #Largo filas
    filas = len(minaDeOro)
    #Largo columnas
    columnas = len(minaDeOro[0])
    #Inicia el tiempo
    start_time = time.time()
    i = 0
    duracionFinal = 0
    tiempos = []
    #Hace un while que experimente n cantidad de veces y saca la duracion final
    #Retorna una lista
    while i < iteraciones:
        start_time = time.time()#Inicia el temporizador
        solucion = (solucionFuerzaBruta(minaDeOro,filas,columnas))#Llama a la funcion solucionDinamica y le pasa los paramtros
        #print(solucion)
        duracion = time.time() - start_time#Resta la duracion actual con la inicial y obtiene la duracion del proceso
        tiempos.append(duracion)
        duracionFinal += duracion#Va sumando en el contador otro proceso para saber toda la duracion
        #print("Duracion: " + str(time.time() - start_time))
        i = i + 1
    #Guarda en el indice 0 la duracion y en el indice 1 la respuesta
    respuestas = []
    respuestas.append(duracionFinal)
    respuestas.append(solucion)
    #Retorna las respuestas
    return respuestas, tiempos

#Recibe la matriz y las filas y columnas
def solucionFuerzaBruta(minaDeOro,filas,columnas):
    #Numero de columnas inicial (Empieza el recorrido de la esquina mas a la derecha arriba)
    j = columnas - 1
    i = 0

    #Saca la solucion inicial para poder empezar hacer las comparaciones
    solucionAuxiliar = solucionFuerzaBruta2(minaDeOro,0,j)

    #print("solucionAuxiliar 1 = "+str(solucionAuxiliar))

    while i < filas:
        #Compara la solucion obtenido anterior con la obtenida actual y verifica cual es el maximo
        solucionAuxiliar2 = max(solucionAuxiliar,solucionFuerzaBruta2(minaDeOro,i+1,j))

        #print("solucionAuxiliar2 = "+str(solucionAuxiliar2))
        #Establece el nuevo maximo
        solucionAuxiliar = solucionAuxiliar2
        #Aumenta la fila
        i = i + 1
        #Si la fila llega al limite, se empieza a recorrer la siguiente columna y se vuelve a poner la fila en 0
        if(i == filas):
            j = j - 1
            i = 0
        #Si la columna llega a ser menor que 0, significa que ya termino de recorrer todas las columnas
        if (j < 0):
            break
    #print(matrizDeCantidad)
    #Retorna el maximo obtenido
    #print(minaDeOro)
    return solucionAuxiliar

#Recibe la matriz y las filas y columnas
#Salida es una posicion de la matriz ya modificada
def solucionFuerzaBruta2(minaDeOro,i,j):
    global filas
    global columnas

    #Si se sale de los limites, retorno 0 .
    if i < 0 or i > filas-1 or j == columnas:
        return 0

    #Solucion si se mueve a la derecha
    derecha = solucionFuerzaBruta2(minaDeOro,i, j + 1)
    #Solucion si se mueve a la derecha arriba
    derechaArriba = solucionFuerzaBruta2(minaDeOro,i - 1, j + 1)
    #Solucion si se mueve a la derecha abajo
    derechaAbajo = solucionFuerzaBruta2(minaDeOro,i + 1, j + 1)

    maximo = max(derecha,derechaArriba,derechaAbajo)
    #Retorna el nuevo valor

    #print(str(i)+" - "+str(j)+" Valores = "+str(minaDeOro[i][j]))

    return minaDeOro[i][j] + maximo


#Funcion que se encarga de leer el archivo de entrada
#Salida es una lista con una lista de cada una de las filas del archivo
def leerArchivoEntrada(archivoEntrada):
    listaEntrada = []
    try:
        archivo = open(archivoEntrada,"r")#indica el nombre del archivo y "r" es que lo va leer
    except(FileNotFoundError):
        print("ERROR: Archivo de entrada no encontrado")
        exit(0)
    #Recorremos el archivo
    for linea in archivo:
        line = []
        line.append(linea.rstrip('\n'))
        listaEntrada.append(line)

    return listaEntrada#Lista de listas en donde esta la matriz

#Convierta la matriz a int para poder empezar a solucionarla
def convertirInt(matriz):
    lista = []
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            x = str(matriz[i][0])
            linea = x.split(",")
            lista2 = []
            for z in range(len(linea)):
                lista2.append(int(linea[z]))#guarda cada fila en esta lista y luego la pega a las lista para que se crear una lista de listas
            lista.append(lista2)
    #Devuelve la lista de listas
    return lista


#Main cuando se corre el archivo solo, agarra el nombre del archivo como argumentos
#Lee el archivoEntrada y lo convierte a Investigacion
#Llena la matriz auxiliar de 0 y empieza buscar la solucion
def mainFB(archivo):
    global filas
    global columnas

    matriz = leerArchivoEntrada(archivo)#Lee el archivo y lo guarda en matriz como lista de listas
    mina = convertirInt(matriz)#Convierte la matriz a int y la devuelve como lista de listas

    #Largo filas
    filas = len(mina)
    #Largo columnas
    columnas = len(mina[0])

    start_time = time.time()#Inicia el tiempo
    print("La cantidad maxima de oro es: " + str(solucionFuerzaBruta(mina,filas,columnas)))#Imprime la solucion
    print("Duracion con fuerza bruta : " + str(time.time() - start_time))#Imprime el tiempo que duro calculandolo
