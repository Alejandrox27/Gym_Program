from datetime import datetime
from gimnasio.modelos.Cliente import Cliente
class Clientes():
    def __init__(self):
        self.clientes = []

    def continuar(self):
        print()
        input('inserte enter para continuar...')
        print()

    def agregar_clientes(self):
        año = int(datetime.strftime(datetime.now(),'%Y'))
        mes = int(datetime.strftime(datetime.now(),'%m'))
        dia = int(datetime.strftime(datetime.now(),'%d'))
        
        hora = int(datetime.strftime(datetime.now(), '%H'))
        minuto = int(datetime.strftime(datetime.now(), '%M'))
        segundo = int(datetime.strftime(datetime.now(), '%S'))
        

        while True:
            try:
                nombre = input('inserte el nombre del nuevo cliente: ')
                if nombre.isalpha():
                    break
                else:
                    print()
                    print('MENSAJE: El nombre debe ser un valor de tipo texto.')
                    self.continuar()
            except ValueError as e:
                print('MENSAJE:',e)
                self.continuar()
                
        while True:
            try:
                identidad = int(input('inserte el numero de tarjeta de identidad/cedula del nuevo cliente: '))
                if self.Buscar_clientes(identidad) == None:
                    break
                else:
                    print()
                    print('MENSAJE: No pueden haber dos tarjetas de identidad iguales')
                    self.continuar()
                    continue
            except ValueError as e:
                print('MENSAJE:',e)
                self.continuar()
                
        while True:
            try:
                objetivo = input('inserte el objetivo del nuevo cliente: ')
                if objetivo.isalpha():
                    break
                else:
                    print('MENSAJE: El objetivo debe ser un valor de tipo texto')
            except ValueError as e:
                print('MENSAJE:',e)
                self.continuar()
                
        while True:
            try:
                patologias = input('inserte las patologias del cliente: ')
                if patologias.isalpha():
                    break
                else:
                    print('MENSAJE: Las patologias deben ser valores de tipo texto')
            except ValueError as e:
                print('MENSAJE:',e)
                self.continuar()
        
        while True:
            try:
                inscripcion = int(input('inserte el tipo de inscripción del nuevo cliente:\n'
                                        '1. MENSUAL'
                                        '\n2. DIARIO'
                                        '\n3. SEMANAL\n>>>'))
                if 0 < inscripcion < 4:
                    break
                else:
                    print()
                    print('MENSAJE: El valor debe estar entre el rango de 1 y 3')
                    self.continuar()
            except ValueError as e:
                print('MENSAJE: El valor debe ser de tipo numerico')
                self.continuar()
                
        if inscripcion == 1:
            inscripcion = 'MENSUAL'
            mes += 1
            if mes > 12:
                mes -= 12
                año += 1
            fecha_final = datetime(año,mes,dia, hora, minuto, segundo)
            
        elif inscripcion == 2:
            inscripcion = 'DIARIO'
            dia += 1
            if dia > 30:
                dia -= 30
                mes += 1
            if mes > 12:
                mes -= 12
                año += 1
            fecha_final = datetime(año,mes,dia, hora, minuto, segundo)
            
        elif inscripcion == 3:
            inscripcion = 'SEMANAL'
            dia += 7
            if dia > 30:
                dia -= 30
                mes += 1
            if mes > 12:
                mes -= 12
                año += 1
            fecha_final = datetime(año,mes,dia, hora, minuto, segundo)
                
            
                        
        nuevo_cliente = Cliente(nombre, identidad, objetivo, patologias, inscripcion,fecha_final)
        self.clientes.append(nuevo_cliente)
                
    def Buscar_clientes(self,identidad):
        for c in self.clientes:    
            if c.identidad == identidad:
                return c
        return None
        
    def ordenar_clientes(self,cliente):
        print('Nombre: {}'.format(cliente.nombre))
        print('tarjeta de identidad: {}'.format(cliente.identidad))
        print('objetivo: {}'.format(cliente.objetivo))
        print('Patologias: {}'.format(cliente.patologias))
        print('Tipo de inscripción: {}'.format(cliente.inscripcion))
        print('Fecha en la que se acaba su inscripción: {}'.format(cliente.fecha_final))
        print('Permiso de entrada: {}'.format(cliente.permiso))
        
    def eliminar_cliente(self, id):
        for c in self.clientes:
            if c.identidad == id:
                self.clientes.remove(c)
                return True
        return False


    def Permiso_de_entrada(self):
        for e in self.clientes:
            if datetime.now() >= e.fecha_final:
                e.permiso = False
                
    def cambiar_info_cliente(self,opcion, identidad):
        cliente = self.Buscar_clientes(identidad)
        
        if opcion == 1:
            while True:
                try:
                    nombre = input('Inserte el nombre para cambiar al cliente: ')
                    if nombre.isalpha():
                        break
                except ValueError as e:
                    print('MENSAJE: Debe haber un nombre.')
                
            cliente.nombre = nombre
            print()
            print('Felicidades, el nombre ha sido cambiado con exito!:')
            print()
            self.ordenar_clientes(cliente)
            self.continuar()
            
        elif opcion == 2:
            while True:
                try:
                    identidad = int(input('Inserte el número de tarjeta de identidad/cedula para cambiar al cliente: '))
                    break
                except ValueError as e:
                    print('\nMENSAJE: Debe haber un número.')
                    self.continuar()
                
            cliente.identidad = identidad
            print()
            print('Felicidades, la cedula/tajeta de identidad ha sido cambiado con exito!:')
            print()
            self.ordenar_clientes(cliente)
            self.continuar()
            
        elif opcion == 3:
            while True:
                try:
                    objetivo = input('Inserte el objetivo para cambiar al cliente: ')
                    break
                except ValueError as e:
                    print('\nMENSAJE: Debe haber un valor de tipo texto.')
                    self.continuar()
                
            cliente.objetivo = objetivo
            print()
            print('Felicidades, el objetivo ha sido cambiado con exito!:')
            print()
            self.ordenar_clientes(cliente)
            self.continuar()
            
        elif opcion == 4:
            while True:
                try:
                    patologias = input('Inserte las patologias para cambiar al cliente: ')
                    break
                except ValueError as e:
                    print('\nMENSAJE: Debe haber un valor de tipo texto.')
                    self.continuar()
                
            cliente.patologias = patologias
            print()
            print('Felicidades, las patologias han sido cambiado con exito!:')
            print()
            self.ordenar_clientes(cliente)
            self.continuar()
            
        elif opcion == 5:
            año = int(datetime.strftime(datetime.now(),'%Y'))
            mes = int(datetime.strftime(datetime.now(),'%m'))
            dia = int(datetime.strftime(datetime.now(),'%d'))
            
            hora = int(datetime.strftime(datetime.now(), '%H'))
            minuto = int(datetime.strftime(datetime.now(), '%M'))
            segundo = int(datetime.strftime(datetime.now(), '%S'))
            while True:
                try:
                    inscripcion = int(input('Inserte el tipo de inscripción para cambiar al cliente: \n1. MENSUAL\n2. DIARIO\n3. SEMANAL\n>>> '))
                    if 0 < inscripcion < 4:
                        break
                    else:
                        print('MENSAJE: El valor debe estar entre el rango de 1 y 3.')
                    
                except ValueError as e:
                    print('\nMENSAJE: Debe haber un número.')
                    self.continuar()
                    
            if inscripcion == 1:
                inscripcion = 'MENSUAL'
                mes += 1
                if mes > 12:
                    mes -= 12
                    año += 1
                fecha_final = datetime(año,mes,dia, hora, minuto, segundo)
                
            elif inscripcion == 2:
                inscripcion = 'DIARIO'
                dia += 1
                if dia > 30:
                    dia -= 30
                    mes += 1
                if mes > 12:
                    mes -= 12
                    año += 1
                fecha_final = datetime(año,mes,dia, hora, minuto, segundo)
                
            elif inscripcion == 3:
                inscripcion = 'SEMANAL'
                dia += 7
                if dia > 30:
                    dia -= 30
                    mes += 1
                if mes > 12:
                    mes -= 12
                    año += 1
                fecha_final = datetime(año,mes,dia, hora, minuto, segundo)
                    
                
                
            
            cliente.fecha_final = fecha_final
            cliente.inscripcion = inscripcion
            cliente.Permiso = True
            print()
            print('Felicidades, la inscripción ha sido cambiada con exito!:')
            print()
            self.ordenar_clientes(cliente)
            self.continuar()