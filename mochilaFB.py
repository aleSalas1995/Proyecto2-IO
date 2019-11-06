from operator import itemgetter
from mochilaPD import *

# Útiles para acceso al peso y valores (irían mejor definiendo una clase)
get_peso = itemgetter(1)
get_valor = itemgetter(2)

def total_peso(paquetes):
    return sum(get_peso(x) for x in paquetes)

def total_valor(paquetes):
    return sum(get_valor(x) for x in paquetes)

# Obtención de todas las combinaciones posibles
# Función recursiva
def combinaciones(paquetes, peso_maximo):
    paqs = [ p for p in paquetes if get_peso(p) <= peso_maximo ]
    resultado = []
    for p in paqs:
        res = combinaciones([x for x in paqs if x!=p], peso_maximo - get_peso(p))
        if len(res) == 0:
            resultado.append([p])
        else:
            resultado.extend([[p]+x for x in res])
    return resultado


# funcion la cual crea una matriz tomando en cuenta nombre peso y beneficio por 
#cada una de las filas
def crearMatriz(pesos,beneficios):
    matriz=[]
    for j in range(0,len(pesos)):
        lista=[]
        lista.append(str(j))
        lista.append(pesos[j])
        lista.append(beneficios[j])
        matriz.append(lista)
    return (matriz)


# funcion para saber cuales items fueron agregados segun el algoritmo de la mochila
def brindar_items(lista,sol):
    indices=[]
    for i in range(0,len(sol)):
        for j in range(1,len(lista)):
            if lista[j][0] == sol[i][1] and lista[j][1] == sol[i][2]:
                indices.append(j)
    return indices


#funcion en la cual se imprimen los items que fueron seleccionados
def imprimirItems(indices):
    for i in range(0,len(indices)):
        print("Se agrego el articulo: "+str(indices[i]))

##se llama en controlador para realizar el proceso de la mochila  fuerza bruta
#funcion encargada de recibir el nombre del archivo y llamar a la funcion de leer para saber si ok
#imprime el tiempo en realizar el algoritmo
# llama a la funcion de mochila
#impresion beneficio maximo

def mainFB( archivo ):

    lista = leerArchivoEntrada(archivo)
    maximo=lista[0][0]
   # print(lista)
    pesos,beneficios=crearPesos_Beneficios(lista)
    start_time = time.time()
    matriz= crearMatriz(pesos,beneficios)

    sol = max(combinaciones(matriz, maximo), key=total_valor)

    print("Duración: "+ str(time.time()-start_time))

    print("\nBeneficio maximo corresponde a: "+str(total_valor(sol)))

    indices = brindar_items(lista,sol)
    imprimirItems(indices)