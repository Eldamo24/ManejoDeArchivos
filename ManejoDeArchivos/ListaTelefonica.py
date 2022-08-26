"""
Escribir un programa para gestionar un listín telefónico con los nombres y los teléfonos de los clientes
 de una empresa. El programa incorporar funciones crear el fichero con el listín si no existe,
 para consultar el teléfono de un cliente, añadir el teléfono de un nuevo cliente
 y eliminar el teléfono de un cliente.
 El listín debe estar guardado en el fichero de texto listin.txt donde el nombre del cliente y su teléfono
 deben aparecer separados por comas y cada cliente en una línea distinta.
"""

def crearLista(nombre, telefono):
    with open("listin.txt", "a", encoding="utf8") as archivo:
        archivo.write(f"{nombre}, {telefono}\n")

def buscarTelefonoPorNombre(nombre):
    try:
        with open("listin.txt", "r", encoding = "utf8") as archivo:
            for line in archivo:
                if nombre in line:
                    print(line)
    except Exception as ex:
        print(f"No se encontro el archivo: {ex}")

def eliminarCliente(nombre):
    data = ""
    try:
        with open("listin.txt", "r", encoding="utf8") as archivo:
            for line in archivo:
                if nombre not in line:
                    data += line
        with open("listin.txt", "w", encoding="utf8") as archivo:
            archivo.write(data)
    except Exception as ex:
        print(f"No se encontro el archivo: {ex}")

def listarClientes():
    try:
        with open("listin.txt", "r", encoding="utf8") as archivo:
            for line in archivo:
                print(line)
    except Exception as ex:
        print(f"No se encontro el archivo: {ex}")

def menu():
    op = 0
    nombre = None
    telefono = None
    while op != 5:
        print("1_Ingresar Cliente \n2_Buscar por nombre \n3_Eliminar cliente \n4_Listar clientes \n5_Salir")
        try:
            op = int(input("Ingrese su opcion: "))
        except Exception as ex:
            print(f"Valor invalido: {ex}")
        finally:
            if op == 1:
                try:
                    nombre = input("Ingrese nombre: ")
                    telefono = int(input("Ingrese telefono: "))
                    crearLista(nombre, telefono)
                except Exception as ex:
                    print(f"Ocurrio un error al ingresar los datos: {ex}")
            elif op == 2:
                try:
                    nombre = input("Ingrese nombre de cliente a buscar: ")
                    buscarTelefonoPorNombre(nombre)
                except Exception as ex:
                    print(f"Ocurrio un error: {ex}")
            elif op == 3:
                try:
                    nombre = input("Ingrese nombre de cliente a eliminar: ")
                    eliminarCliente(nombre)
                except Exception as ex:
                    print(f"Ocurrio un error: {ex}")
            elif op == 4:
                listarClientes()
            elif op == 5:
                print("Adios....")
            else:
                print("Opcion inexistente..")
menu()