"""
Escribir una función que pida dos números n y m entre 1 y 10,
lea el fichero tabla-n.txt con la tabla de multiplicar de ese número,
y muestre por pantalla la línea m del fichero.
Si el fichero no existe debe mostrar un mensaje por pantalla informando de ello.
"""

def mostrarLinea(numN, numM):
    with open(f"tabla{numN}.txt", "r") as archivo:
        try:
            print(archivo.readlines()[numM])
        except IndexError as ex:
            print(f"Indice inexistente: {ex}")
        except Exception as ex:
            print(f"Excepcion inesperada: {ex}")

"""
    try:
        archivo = open(f"tabla{numN}.txt", "r")
        print(archivo.readlines()[numM])
    except FileNotFoundError as ex:
        print(f"El archivo no se encontro: {ex}")
    except IndexError as ex:
        print(f"Indice inexistente: {ex}")
        archivo.close()
    except Exception as ex:
        print(f"Ocurrio un error inesperado... {ex}")
        archivo.close()
    else:
        archivo.close()"""


try:
    numN = int(input("Ingrese un numero del cual quiere ver la tabla: "))
    numM = int(input("Ingrese numero de linea que quiere ver en el archivo: "))
except Exception as ex:
    print(f"Ocurrio un error al ingresar los numeros: {ex}")
else:
    mostrarLinea(numN, numM)
