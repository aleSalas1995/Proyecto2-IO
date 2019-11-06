import random
import time
import argparse

from MinaPD import * #Importa la clase MinaPD
from MinaFB import *  #Importa la clase MinaFB

#Variables globales
global filas
global columnas
global iteraciones
global archivo
global oroMax

#Funcion main
def main():
    
	#Varaibles globales
    global filas
    global columnas
    global oroMax

    #Variable creada para obtencion de atributos desde la terminal
    parser = argparse.ArgumentParser(description="Programa Mina de Oro | Menu de Ayuda")

    #Agrega cada uno de los parametro siendo obtenidos de las terminal
    parser.add_argument("-om", dest = "oroMax", help = "Contiene el oro maximo en la matriz")
    parser.add_argument("-g", dest = "generar", help = "Generar experimentos")
    parser.add_argument("-n",dest = "filas", help = "Cantidad de filas")
    parser.add_argument("-m", dest = "columnas", help = "Cantidad de columnas")
    parser.add_argument("-i", dest = "iteraciones", help = "Cantidad de iteraciones")
    parser.add_argument("-pd", dest = "programacionDinamica", help = "Archivo txt a leer para aplicar programacionDinamica")
    parser.add_argument("-fb", dest = "fuerzaBruta", help = "Archivo txt a leer para aplicar fuerzaBruta")

    #Parseo los parametros o argumentos y guardo
    args = parser.parse_args()

    ## Seleccionar que ejecutar en el programa con los argumentos que entraron
    if args.generar:#entra aqui para generar la matriz y calcular FB y PD
    	#Si encuentra argumento filas lo guarda en su respectiva variable
        if args.filas:
            filas = int(args.filas)
        #Si encuentra argumento columnas lo guarda en su respectiva variable
        if args.columnas:
            columnas = int(args.columnas)
        #Si encuentra el numero de iteraciones lo guarda en su respectiva variable
        if args.iteraciones:
            iteraciones = int(args.iteraciones)
        #Si encuentra el numero de oro Maximo lo guarda en su respectiva variable
        if args.oroMax:
            oroMax = int(args.oroMax)
        #Llama a la funcion que genera la matriz
        matriz = generar_Matriz() #Se genera la matriz
        #impresiones para saber que todos los datos estan bien
        #print(matriz)
        #print(filas)
        #print(columnas)

        #Llama a las respectivas funciones para que realicen calculos y los guarda en variables resp1 y resp2 que son listas
        resp1, tiempoFB = iniciarFuerzaBruta(matriz,iteraciones) #Guarda los resultados de FB (tiempo,resultado)
        resp2, tiempoD = iniciarDinamica(matriz,iteraciones) #Guarda los resultados de PD (tiempo,resultado)


        promedioFuerzaBruta = resp1[0] / iteraciones #Saca el promedio
        promedioDinamica = resp2[0] / iteraciones   #Saca el promedio

        #impresiones y final de la funcion generando el reporte
        #print("Generando Reporte...")
        #time.sleep(3)

        #Genera reporte en un archivo txt   
        generarReporteExperimento(filas,columnas,matriz,promedioFuerzaBruta,resp1[1],promedioDinamica,resp2[1],iteraciones)

    #Entra existen argumentos de PD
    elif args.programacionDinamica:

        programacionDinamica = args.programacionDinamica#Obtiene los argumentos en una variable
        print("Programación Dinámica")
        mainPD(programacionDinamica)#Llama a la funcion main de PD y le manda un archivo que contiene los argumentos
    #Entra si existen argumentos de FB
    elif args.fuerzaBruta:

        fuerzaBruta = args.fuerzaBruta#Obtiene los argumentos en una variable
        print("Fuerza Bruta")
        mainFB(fuerzaBruta)#Llama a la funcion main de FB y le manda el archivo con los argumentos necesarios


#Se genera la matriz con numeros random hasta el oroMax
#La salida es una matriz
def generar_Matriz():
    global oroMax#Crea una variable global
    matriz = []#lista donde se guarda cada fila de la matriz
    for i in range(0, filas):
        lista = []
        for j in range(0, columnas):
            lista.append(random.randrange(oroMax))#Agrega cada dato en la lista
        matriz.append(lista)#Despues de que llena la lista con el largo de columnas la agrega a la matriz
    return matriz

#Funcion que se encarga de escribir en un archivo el experimento realizado
def generarReporteExperimento(filas,columnas,mina,promedioFB,resFB,promedioPD,resPD,iteraciones):
    
    print("Experimento con problema de Mina de Oro")
    print("Se eligio un N de " + str(filas) + " y un M de " + str(columnas))
    print("Cantidad de iteraciones: " + str(iteraciones))
    print("Oro máximo de "+str(oroMax))
    print("Mina de Oro \n")
    for i in range(len(mina)):
        print(str(mina[i]) + "\n")
    print("El resultado con fuerza bruta fue: " + str(resFB))
    print("El resultado con programacion dinamica fue: " + str(resPD))
    print("El tiempo promedio con fuerza bruta fue: " + str(promedioFB))
    print("El tiempo promedio con programacion dinamica fue: " + str(promedioPD))
main()
