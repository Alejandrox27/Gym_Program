import pickle
from gimnasio.modelos.Clientes import Clientes
from gimnasio.modelos.Cliente import Cliente
from datetime import datetime
import os

def menu():
    print('Ingrese una de las siguientes opciones:'
          '\n1. Agregar nuevos clientes'
          '\n2. Eliminar clientes'
          '\n3. consultar la información de un cliente'
          '\n4. Cambiar información de un cliente'
          '\n0. salir')
    
def continuar():
    print()
    input('inserte enter para continuar...')
    print()
    
def listar_clientes(clientes):
    for c in clientes:
        print(c.identidad, '-', c.nombre)


def guardar_datos(clientes):
    nombre_archivo = 'gimnasio/datos.pickle'
    while True:
        while True:
            try:
                opcion = int(input('Desea guardar la información de los clientes?\n1. Si\n2. No\n>>> '))
                if 0 < opcion < 3:
                    break
                else:
                    print('MENSAJE: El valor debe ser entre el rango de 1 y 2.')
            except ValueError as e:
                print('MENSAJE: Debe agregar un valor valido.')
                
        if opcion == 1:
            with open(nombre_archivo, 'wb') as f:
                pickle.dump(clientes,f)
            return True
        else:
            return False
            
    

def cargar_datos():
    nombre_archivo = 'gimnasio/datos.pickle'
    while True:
        while True:
            try:
                opcion = int(input('Desea cargar la información de los clientes?\n1. Si\n2. No\n>>> '))
                if 0 < opcion < 3:
                    break
                else:
                    print('MENSAJE: El valor debe ser entre el rango de 1 y 2.')
            except ValueError as e:
                print('MENSAJE: Debe agregar un valor valido.')
                
        if opcion == 1:
            with open(nombre_archivo, 'rb') as f:
                clientes = pickle.load(f)
                return clientes
        return None


def main():
    clieentes = Clientes()
    
    if os.path.isfile('gimnasio/datos.pickle'):
        clientes_1 = cargar_datos()
        
        if clientes_1:
            clieentes.clientes = clientes_1.clientes
        
    while True:
        while True:
            clieentes.Permiso_de_entrada()
            try:
                menu()
                opcion = int(input('\n>>>'))
                
                if 0 <= opcion < 5:
                    break
                else:
                    print('MENSAJE: El valor ingresado debe ser un valor entre 0 y 4.')
            except ValueError as e:
                print('MENSAJE: El valor ingresado no es valido.')
            continuar()
        if opcion == 0:
            break    
        elif opcion == 1:
            clieentes.agregar_clientes()
            clieentes.Permiso_de_entrada()
        elif opcion == 2:
            if len(clieentes.clientes):
                while True:
                    try:
                        listar_clientes(clieentes.clientes)
                        print()
                        identidad = int(input('inserte la tarjeta de identidad del cliente a eliminar: '))
                        break
                    except ValueError as e:
                        print('MENSAJE:',e)
                    
                if clieentes.eliminar_cliente(identidad):
                    print()
                    print('MENSAJE: Felicidades se ha eliminado el cliente con exito.')
                    continuar()
                else:
                    print()
                    print('MENSAJE: No se ha encontrado el cliente.')
                    continuar()
            else:
                print('\nMENSAJE: No hay clientes registrados todavía.')
                continuar()
        elif opcion == 3:
            if len(clieentes.clientes):
                while True:
                    try:
                        clieentes.Permiso_de_entrada()
                        listar_clientes(clieentes.clientes)
                        print()
                        identidad = int(input('inserte la tarjeta de identidad del cliente: '))
                        print()
                        
                        cliente = clieentes.Buscar_clientes(identidad)
                        clieentes.ordenar_clientes(cliente)
                        break
                    except ValueError as e:
                        print('MENSAJE: Debe ser un valor numerico')     
                continuar()
            else:
                print('\nMENSAJE: No hay clientes registrados todavía.')
                continuar()
                
        elif opcion == 4:
            if len(clieentes.clientes):
                while True:
                    try:
                        print('Qué desea cambiar de la info de algún cliente?\n'
                            '1. Su nombre'
                            '\n2. Su tarjeta de identidad'
                            '\n3. Su objetivo'
                            '\n4. Sus patologias'
                            '\n5. Su tipo de inscripción')
                        opcion = int(input('\n>>> '))
                        if 0 < opcion < 6:
                            break
                        else:
                            print()
                            print('MENSAJE: Debe ser un valor entre 1 y 5.')
                            continuar()
                    except:
                        print('MENSAJE: Debe ser un valor valido')
                        
                listar_clientes(clieentes.clientes)
                print()
                
                while True:
                    try:
                        identidad = int(input('Inserte el numero de identidad del cliente a cambiar su información: '))
                        if clieentes.Buscar_clientes(identidad) == None:
                            print()
                            print('MENSAJE: No hay ningun cliente con ese id.')
                            continuar()
                            continue
                        else:
                            break
                    except ValueError as e:
                        print('MENSAJE: Debe ser un valor entero.')
                        
                clieentes.cambiar_info_cliente(opcion, identidad)
            else:
                print()
                print('MENSAJE: Aún no hay clientes registrados.')
                continuar()
                        
    if guardar_datos(clieentes):
        print('MENSAJE: La información se ha guardado con exito.')
        
    else:
        print('MENSAJE: La información no se guardó.')
    continuar()
    
    print('El programa ha finalizado.')
                

if __name__ == '__main__':
    main()