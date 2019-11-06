import matplotlib.pyplot as plt
import argparse

from mochilaPD_FB import *
from mochilaPD import *
from mochilaFB import *

tamanio_contenedor = 0
n_elementos = 0
iteraciones = 0
peso_maximo = 0
beneficio_maximo = 0

# se valida y luego se llama a la funcion que el usuairo haya deseado
# segun sea programacion dinamica fuerza bruta o ambas
#F corresponde a ambas
#B fuerza bruta
#D dinamica

def main(argv):

    global tamanio_contenedor 
    global n_elementos 
    global iteraciones 
    global beneficio_maximo
    global peso_maximo

    parser = argparse.ArgumentParser(description="Programa Mochila | Menu de Ayuda")

    parser.add_argument("-g", dest = "generar", help = "Generar experimentos")
    parser.add_argument("-w", dest = "tamanio_contenedor", help = "Tamao maximo del contenedor")
    parser.add_argument("-n", dest = "n_elementos", help = "N elementos")
    parser.add_argument("-i", dest = "iteraciones", help = "Numero de iteraciones")
    parser.add_argument("-p", dest = "peso_maximo", help = "Peso maximo")
    parser.add_argument("-b", dest = "beneficio_maximo" , help = "Beneficio Maximo")
    parser.add_argument("-pd", dest = "programacionDinamica", help = "Archivo txt a leer para aplicar programacionDinamica")
    parser.add_argument("-fb", dest = "fuerzaBruta", help = "Archivo txt a leer para aplicar fuerzaBruta")

    args = parser.parse_args()

    if args.generar:

        if args.tamanio_contenedor:
            tamanio_contenedor = int(args.tamanio_contenedor)

        if args.n_elementos:
            n_elementos = int(args.n_elementos)

        if args.iteraciones:
            iteraciones = int(args.iteraciones)

        if args.peso_maximo:
            peso_maximo = int(args.peso_maximo)

        if args.beneficio_maximo:
            beneficio_maximo = int(args.beneficio_maximo)
            if beneficio_maximo < 50:
                beneficio_maximo = 50

        simulacion_F(tamanio_contenedor, n_elementos, iteraciones, peso_maximo, beneficio_maximo)

    elif args.programacionDinamica:

        programacionDinamica = args.programacionDinamica
        print("Programación Dinámica")
        mainPD(programacionDinamica)

    elif args.fuerzaBruta:

        fuerzaBruta = args.fuerzaBruta
        print("Fuerza Bruta")
        mainFB(fuerzaBruta)

if __name__ == "__main__":
    main(sys.argv[1:])