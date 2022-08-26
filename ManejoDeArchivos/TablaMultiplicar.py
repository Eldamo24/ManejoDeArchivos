"""
Escribir una función que pida un número entero entre 1 y 10 y guarde en un fichero con el nombre tabla-n.txt
la tabla de multiplicar de ese número, done n es el número introducido.
"""

def guardarTabla(num):
    with open(f"tabla{num}.txt", "w") as archivo:
        for i in range(1, 11):
            archivo.write(f"{num} x {i} = {i*num}\n")

try:
    num = int(input("Ingrese un numero entero: "))
except Exception as ex:
    print(f"Ocurrio un error: {ex}")
    num = 1
finally:
    guardarTabla(num)