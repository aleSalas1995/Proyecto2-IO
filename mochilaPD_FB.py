from mochilaPD import *
from mochilaFB import *

import sys
import time
import random

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


#random que se crea tomando en cuenta un maximo de 100
#se realiza la cantidad de veces especificada por el usuario mediante
#los elementos
def generar_beneficios(n_elementos, beneficio_maximo):
    lista = []
    for j in range(0, n_elementos):
        lista.append(random.randrange(beneficio_maximo))
    return lista



#random que se crea tomando en cuenta un maximo  dado por el usuario
#se realiza la cantidad de veces especificada por el usuario mediante
#los elementos
def generar_pesos(n_elementos,peso_maximo):
    lista = []
 
    for j in range(0, n_elementos):
        lista.append(random.randrange(peso_maximo))
    return lista


#suma todos los tiempo y los divide entre la cantidad para
#saber cuanto se duro en promedio
def promedio(lista):
    num = 0
    suma = 0
    for i in lista:
        suma = suma + i
        num += 1
    return suma/num


#escribe en archivo texto plano el maximo beneficios y los items agregados
def imprimir_resultado(index, valorM):

    #print("\n Benefico Maximo: " + str(valorM) + "\n")
    print("Se agregaron los items: "+str(index))


#escribe en archivo texto plano el peso maximo los elementos y los pesos obtenidos
# asi como tambien los beneficios
def escribir_datos(pesos, beneficios,tamanio_contenedor,n_elementos):

    print("Datos de prueba:")
    print("Peso Maximo: " + str(tamanio_contenedor))
    print("Numero de Items: " + str(n_elementos))
    print("Lista con los pesos de cada elemento y sus beneficios:")
    print(str(pesos) + "-> Pesos")
    #print("\n")
    #print("Lista con los beneficios de cada elemento: \n")
    print(str(beneficios)+"-> Beneficios")


#funcion en la cual se realiza un ciclo segun las iteraciones
#elegidas por el usuario, en el ciclo se llama a la funcion de programacion
#dinamica , fuerza bruta y se va midiendo el tiempo para luego sacar el promedio
#recibe como entrada el peso maximo los items y las iteraciones , cada uno de esos
#datos es proporcionado por el usuario mediante terminal
def simulacion_F(tamanio_contenedor,n_elementos,iteraciones,peso_maximo, beneficio_maximo):
    Y_FB = []
    X = []
    Y_D = []

    pesos_F = generar_pesos(n_elementos,peso_maximo)
    beneficios_F = generar_beneficios(n_elementos, beneficio_maximo)
    escribir_datos(pesos_F, beneficios_F,tamanio_contenedor,n_elementos)
    matriz = crearMatriz(pesos_F,beneficios_F)
    sol=[]
    for i in range(0, iteraciones):
        X.append(i + 1)

        start_time_i = time.time()
        index,valorM = callpd(tamanio_contenedor, pesos_F, beneficios_F)
        Y_D.append(time.time() - start_time_i)

        start_time_j = time.time()
        sol = max(combinaciones(matriz, tamanio_contenedor), key=total_valor)
        
        Y_FB.append(time.time() - start_time_j) 


    print("\nEl beneficio maximo con  mochila es: "+str(total_valor(sol)))
    imprimir_resultado(index, valorM)
    print("\nTiempo: ")
    #print("X "+str(X))
    print(" -Dinamica:" +str(Y_D))
    print(" -FBruta: "+str(Y_FB))

    print("Numero de iteraciones: " + str(iteraciones))
    print("Promedio de duracion de algoritmo Fuerza Bruta: " + str(promedio(Y_FB)))
    print("Promedio de duracion de algoritmo Programacion Dinamica: " + str(promedio(Y_D)))


