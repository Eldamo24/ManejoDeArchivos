"""
Escribir una función que pida un número entero entre 1 y 10,
lea el fichero tabla-n.txt con la tabla de multiplicar de ese número,
done n es el número introducido, y la muestre por pantalla.
 Si el fichero no existe debe mostrar un mensaje por pantalla informando de ello.
"""

def lecturaArchivo(num):
    try:
        archivo = open(f"tabla{num}.txt", "r")
    except Exception as ex:
        print(f"Ocurrio un error al leer el archivo ya que no existe: {ex}")
    else:
        for linea in archivo:
            print(linea)
        archivo.close()

try:
    num = int(input("Ingrese numero entero: "))
except Exception as ex:
    print(f"Ha ocurrido un error: {ex}")
else:
    lecturaArchivo(num)