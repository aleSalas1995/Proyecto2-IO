import time
pesosD=[]

#ALGORITMO de mochila usando programacion dinamica y tambien memo
#para guardar las rutas
def mochila(W, pesos, ben, n):
    M = [[0 for x in range(W + 1)] for x in range(n + 1)]
    for i in range(n + 1):
        for w in range(W + 1):
            if i == 0 or w == 0:
                M[i][w] = 0
            elif pesos[i - 1] <= w:
                M[i][w] = max(ben[i - 1] + M[i - 1][w - pesos[i - 1]], M[i - 1][w])
            else:
                M[i][w] = M[i - 1][w]

    i = n
    j = W
    index = []

    global pesosD
    pesosD=[]
    while M[i][j] > 0:
        if M[i - 1][j] != M[i][j]:
            index.append(ben.index(ben[i - 1]) + 1)
            j = j - pesos[i - 1]
            pesosD.append(pesos[i-1])
        i -= 1
    index.sort()
    
    return index, M[n][W]

#ALGORITMO de mochila usando programacion dinamica y tambien memo
#para guardar las rutas
#recibe el peso maximo, pesos, y beneficios
#retorna el beneficio maximo y los items agregados
def callpd(peso_maximo, nuevos_pesos, beneficios):
    global W
    global pesos
    global ben

    W = peso_maximo

    pesos = nuevos_pesos
    ben = beneficios
    index, valorM = mochila(W, pesos, ben, len(pesos))

    return index, valorM




#Funcion que se encarga de leer el archivo de entrada
#Retorna : Lista con numero en forma de int
def leerArchivoEntrada(archivoEntrada):
    listaEntrada = []


    try:
        archivo = open(archivoEntrada,"r")
    except(FileNotFoundError):
        print("ERROR: Archivo de entrada no encontrado")
        exit(0)

    lineas = archivo.readlines()
    
    l = [[m.strip() for m in n] for n in [linea.split(",") for linea in lineas]]
    lista=[]
    for x in range(0,len(l)):
        aux=[]
        for y in range(0,len(l[x])):
            aux.append(int(l[x][y]))
        lista.append(aux)
    return lista

# se recorre la lista original luego de leer el archivo y 
# de ahi se crea una lista unicamente solo con beneficios y otra con los pesos
#por aparte para que despues se pueda llamar a callPD
def crearPesos_Beneficios(lista):
    pesos=[]
    beneficios=[]
    for x in range(1,len(lista)):
        cont = lista[x][len(lista[x])-1]
        for y in range(0,cont):
            pesos.append(lista[x][0])
            beneficios.append(lista[x][1])
    return pesos,beneficios


# funcion para saber cuales items fueron agregados segun el algoritmo de la mochila
def ubicarIndices(lista):
    indices=[]
    for i in range(0,len(pesosD)):
        for j in range(1,len(lista)):
            if lista[j][0] == pesosD[i]:
                indices.append(j)

    return(indices)            
#funcion  en la cual se imprimen los items que fueron seleccionados
def imprimirIndices(indices):
    for i in range(0,len(indices)):
        print("Se agrego el articulo: "+str(indices[i]))


##se llama en controlador para realizar el proceso de la mochila  fuerza bruta
#funcion encargada de recibir el nombre del archivo y llamar a la funcion de leer para saber si ok
#imprime el tiempo en realizar el algoritmo
# llama a la funcion de mochila
#impresion beneficio maximo

#
def mainPD( archivo):

    lista = leerArchivoEntrada(archivo)
    maximo=lista[0][0]
    pesos,beneficios=crearPesos_Beneficios(lista)
    start_time = time.time()
    index,Maximo= callpd(maximo,pesos,beneficios)
    print("Duración: "+ str(time.time()-start_time))
    indices = ubicarIndices(lista)
    
    print("\nBeneficio maximo: "+str(Maximo))
    imprimirIndices(indices)

