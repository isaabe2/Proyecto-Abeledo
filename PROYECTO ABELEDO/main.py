
from Cruceros import Cruceros
from Rooms import Rooms
from Menu import Platos
from Combos import Combos
from Huesped import Huesped
import requests
from datetime import datetime
import string


def cruceros_info(cruceros,saman_caribbean):
    #Informacion de cada crucero
    for cruise in saman_caribbean:
        name = cruise['name']
        route = cruise['route']
        departure = cruise['departure']
        cost = cruise['cost']
        rooms = cruise['rooms']
        capacity = cruise['capacity']

        cruise = Cruceros(name,route,departure,cost,rooms,capacity)
        cruceros.append(cruise)
    
    return cruceros


def rooms_info(simple_r,premium_r, vip_r,saman_caribbean):
    
    for simple_room in saman_caribbean:
        clase = 'Simple'
        cost = simple_room['cost']['simple']
        capacity = simple_room['capacity']['simple']
        hallway = simple_room['rooms']['simple'][0]
        hab = simple_room['rooms']['simple'][1]

        room = Rooms(clase, capacity,cost, hallway, hab)
        simple_r.append(room)
        
    for premium_room in saman_caribbean:
        clase = 'Premium'
        cost = premium_room['cost']['premium']
        capacity = premium_room['capacity']['premium']
        hallway = premium_room['rooms']['premium'][0]
        hab = premium_room['rooms']['premium'][1]

        room = Rooms(clase, capacity,cost, hallway, hab)
        premium_r.append(room)

    for vip_room in saman_caribbean:
        clase = 'VIP'
        cost = vip_room['cost']['vip']
        capacity = vip_room['capacity']['vip']
        hallway = vip_room['rooms']['simple'][0]
        hab = vip_room['rooms']['simple'][1]

        room = Rooms(clase, capacity,cost, hallway, hab)
        vip_r.append(room)

         
    return simple_r, premium_r, vip_r


def sell_hab(cedula, room_list, cruceros, simple_r, premium_r, vip_r, saman_caribbean):
    
    alphabet = string.ascii_uppercase 
    #seleccion de busqueda segun destino o crucero
    while True:
        try:
            busqueda = int(input(f'''
            Desea escoger el viaje segun: 
            
            El destino:
            1- {cruceros[0].get_route()}
            2- {cruceros[1].get_route()}
            3- {cruceros[2].get_route()}
            4- {cruceros[3].get_route()}

            El Crucero:
            5- {cruceros[0].get_name()}
            6- {cruceros[1].get_name()}
            7- {cruceros[2].get_name()}
            8- {cruceros[3].get_name()}

            9 - Volver al menú principal

            >>> '''))
        except ValueError as identifier:
                print('El dato ingresado es invalido')
        
        if (busqueda == 1) or (busqueda == 5):
            #seleccion de tipo de habitacion
            try:
                room_type = int(input(f'''En {cruceros[0].get_name()} se tienen las siguientes opciones:
                1){simple_r[0]}

                2){premium_r[0]}

                3){vip_r[0]}

                >'''))
            except ValueError as identifier:
                print('El dato ingresado es invalido')
            simple = simple_r[0]
            premium = premium_r[0]
            vip = vip_r[0]
            cruise = cruceros[0]
            #Recoleccion de informacion de cada tipo de hatitacion
            if room_type == 1:
                hallways = simple.get_hallway()
                rooms = simple.get_hab()
                capacity = simple.get_capacity()
                cost = simple.get_cost()
                clase = "Simple"

            elif room_type == 2:
                hallways = premium.get_hallway()
                rooms = premium.get_hab()
                capacity =premium.get_capacity()
                cost = premium.get_cost()
                clase = 'Premium'
                
            elif room_type == 3:
                hallways = vip.get_hallway()
                rooms = vip.get_hab()
                capacity = vip.get_capacity()
                cost = vip.get_cost()
                clase = 'VIP'
                
            else:
                print('Dato erroneo, intente de nuevo')

        elif (busqueda == 2) or (busqueda == 6):
            #Seleccion de tipo de habitacion
            try:
                room_type = int(input(f'''En {cruceros[1].get_name()} se tienen las siguientes opciones:
                1){simple_r[1]}

                2){premium_r[1]}

                3){vip_r[1]}

                >'''))

            except ValueError as identifier:
                print('El dato ingresado es invalido')
            simple = simple_r[1]
            premium = premium_r[1]
            vip = vip_r[1]
            cruise = cruceros[1]
            #Recoleccion de informacion segun tipo de habitacion
            if room_type == 1:
                hallways = simple.get_hallway()
                rooms = simple.get_hab()
                capacity = simple.get_capacity()
                cost = simple.get_cost()
                clase = "Simple"
                
            elif room_type == 2:
                hallways = premium.get_hallway()
                rooms = premium.get_hab()
                capacity =premium.get_capacity()
                cost = premium.get_cost()
                clase = 'Premium'
                
            elif room_type == 3:
                hallways = vip.get_hallway()
                rooms = vip.get_hab()
                capacity = vip.get_capacity()
                cost = vip.get_cost()
                clase = 'VIP'

            else:
                print('Dato erroneo, intente de nuevo')

        elif (busqueda == 3) or (busqueda == 7):
            #Seleccion de tipo de habitacion
            try:
                room_type = int(input(f'''En {cruceros[2].get_name()} se tienen las siguientes opciones:
                1){simple_r[2]}

                2){premium_r[2]}

                3){vip_r[2]}

                >'''))

            except ValueError as identifier:
                print('El dato ingresado es invalido')
            
            simple = simple_r[2]
            premium = premium_r[2]
            vip = vip_r[2]
            cruise = cruceros[2]
            #Recoleccion de informacion segun tipo de habitacion
            if room_type == 1:
                hallways = simple.get_hallway()
                rooms = simple.get_hab()
                capacity = simple.get_capacity()
                cost = simple.get_cost()
                clase = "Simple"
                
            elif room_type == 2:
                hallways = premium.get_hallway()
                rooms = premium.get_hab()
                capacity =premium.get_capacity()
                cost = premium.get_cost()
                clase = 'Premium'
                
            elif room_type == 3:
                hallways = vip.get_hallway()
                rooms = vip.get_hab()
                capacity = vip.get_capacity()
                cost = vip.get_cost()
                clase = 'VIP'
            else:
                print('Dato erroneo, intente de nuevo')
                
        elif (busqueda == 4) or (busqueda == 8):
            #Seleccion de tipo de habitacion
            try:
                room_type = int(input(f'''En {cruceros[3].get_name()} se tienen las siguientes opciones:
                1){simple_r[3]}

                2){premium_r[3]}

                3){vip_r[3]}

                >'''))

            except ValueError as identifier:
                print('El dato ingresado es invalido')
            
            simple = simple_r[3]
            premium = premium_r[3]
            vip = vip_r[3]
            cruise = cruceros[3]
            #Recoleccion de informacion segun tipo de habitacion
            if room_type == 1:
                hallways = simple.get_hallway()
                rooms = simple.get_hab()
                capacity = simple.get_capacity()
                cost = simple.get_cost()
                clase = 'Simple'

            elif room_type == 2:
                hallways = premium.get_hallway()
                rooms = premium.get_hab()
                capacity =premium.get_capacity()
                cost = premium.get_cost()
                clase = 'Premium'
                
            elif room_type == 3:
                hallways = vip.get_hallway()
                rooms = vip.get_hab()
                capacity = vip.get_capacity()
                cost = vip.get_cost()
                clase = 'VIP'
                
            else:
                print('Dato erroneo, intente de nuevo')

        #Exit
        elif busqueda == 9:
            break
        else:
            print('El dato ingresado no existe')

        print('HABITACIONES')
        #Representacion matricial de habitaciones
        for i in range(hallways):
            for j in range(rooms):
                print(f'{alphabet[i]}{j+1}  ', end = ' ', sep = '\t')
            print(' ')
        try:
            #Cantidad de personas a comprar ticket
            cant_fam = int(input('Ingrese la cantidad de personas: '))
        except ValueError as identifier:
            print('El dato ingresado es invalido')
        
        discount = 0
        count = 1
        suma = 0
        
       #Registro de huespedes 
        with open(f'{cruise.get_name()}_{clase}.txt', 'a') as h:
                    h.write('')
        #Comparacion de cantidad de tickets por comprar vs capacidad de habitacion
        if cant_fam <= capacity:
            room_id = input('Identificacion de habitacion escogida: ').capitalize()
            with open(f'{cruise.get_name()}_{clase}.txt', 'r') as h:
                db = h.read()
                if room_id in db:
                        print('Lo siento, esta habitacion ya se encuentra ocupada')
                        break
                else:
                    maximo = 1
                    #Registro de datos de cada persona
                    while maximo <= cant_fam:
                        maximo +=1
                        name = input('Ingrese nombre: ').capitalize()
                        try:
                            dni = int(input('Ingrese cedula: '))
                            age = int(input('Ingrese su edad: '))
                        except ValueError as identifier:
                            print('El dato ingresado es invalido')

                        discapacity = input('Presenta alguna descapacidad si/no: ').lower()    
                        #Si el dni es numero primo se obtiene un descuento de 10%
                        for i in range(2,dni+1):
                            if (dni%i) ==0:
                                discount += 0.10
                        #Si el dni es numero abundante se obtiene un descuento de 15%
                        while (count<dni):
                            if (dni % count == 0):
                                suma += count
                            count = count + 1
                            if suma > dni:
                                discount += 0.15
                        #Si el huesped es discapacitado se obtiene un descuento de 30%
                        if discapacity == 'si':
                            discount += 0.30
                        
                        costo = cost 
                        descuento = cost*discount
                        iva = cost*0.16
                        total = costo + descuento + iva
                        
                        #Factura por persona    
                        print(f'''
                        ---FACTURA POR PERSONA---
                        NOMBRE: {name}
                        CEDULA: {dni}
                        EDAD: {age}
                        DISCAPACIDAD: {discapacity}
                        HABITACION: {room_id}
                        TOTAL SIN IVA: {total}
                        MONTO CON DESCUENTO: {descuento}
                        IMPUESTOS: {iva}
                        TOTAL: {total}
                        ''')
                        cedula.append(dni)
                        with open('dni.txt', 'a') as d:
                            d.write(f'{dni}')
                    print('COMPRA EXITOSA!')
                    #Registro de compra de habitacion
                    with open(f'{cruise.get_name()}_{clase}.txt', 'a') as h:
                                h.write(f'{room_id} ')
                    

def restaurante(comida, menu, menu_combos):
    name = ''
    clasification = ''
    price = ''
    #Todo tipo de cambio del menu
    while True:
        try:
            funcionalidades = int(input('''
            1 - Agregar plato
            2 - Eliminar producto del menu
            3 - Modificar producto del menu
            4 - Agregar Combos al menu de combos
            5 - Eliminar combos del menu de combos 
            6 - Buscar productos por nombre o rango de precio
            7 - Buscar combos por nombre o ranfo de precio
            8 - Volcer al menu
            >>> '''))
        except ValueError as identifier:
            print('El dato ingresado es invalido')
        #Agregar plato al menu
        if funcionalidades == 1:
            
            while True:
                try:
                    #Nombre del alimento/bebida
                    name = input('Ingrese nombre del plato: ').capitalize()
                    try:
                        #precio del alimento/bebida (sin IVA)
                        price = int(input('Precio del producto: '))
                        
                    except ValueError as identifier:
                        print('El precio ingresado es invalido')
                    #precio con IVA incluido
                    price += price*0.16
                    #Clasificacion del producto, si es bebida o comida
                    tipo = input('Es comida (c) o bebida (b): ').lower()
                    if tipo == 'c':
                        modo = input('Es de empaque (e) o de preparacion (p): ').lower()
                        if modo == 'e':
                            clasification = 'Empaque'
                        elif modo == 'p':
                            clasification = 'Preparacion'
                    elif tipo == 'b':
                        size = input('El tamaño de la bebida es pequeño (p), mediado (m) o grande (g): ').lower()
                        if size == 'p':
                            clasification = 'Pequeña'
                        elif size == 'm':
                            clasification = 'Mediana'
                        elif size == 'g':
                            clasification = 'Grande'
                        else:
                            print('El dato ingresado es invalido')
                    else:
                        print('El dato ingresado es invalido')
                    
                    break
                             
                        
                except:
                    print('Error, valide los datos')
             
                  
            alimento = Platos(name, clasification, price)

            menu[name] = [price,clasification]
            comida.append(name)
            comida.append(' ')
            print(comida)
            with open('menu.txt', 'a') as m:
                m.write(f'{name} ')
        
            print('\nRegistrado exitosamente')
            return alimento,menu  

        #Eliminar plato del menu
        if funcionalidades == 2:
            name_search = input('Ingresa el nombre del plato que desea eliminar: ').capitalize()
            
            
            if name_search in menu.keys():
                del menu[name_search]
                comida.remove(name_search)
                print(f'el/la {name_search} fue eliminado/a del menu')
                with open('menu.txt', 'w') as m:
                    for i in comida:
                        m.write(i)


    
            else:
                print('Lo siento el plato que busca no existe en el menu')
            
        #Modificar un plato del menu 
        elif funcionalidades == 3:
            name = input('Ingresa el nombre del plato que desea modificar: ').capitalize() 
            if name in menu.keys():
                for name in menu.items():
                    cambio = input('Desea cambiar la clasificacion (c) o el precio (p): ').lower()
                    
                    tipo = input('Es bebida (b) o alimento (a): ').lower()
                    
                    if cambio == 'c':
                        #Cambio de clasificacion de alimento
                        if tipo == 'b':
                            change_clasification = input('Ingrese la nueva clasificacion de la bebida (pequeño (s),mediano (m) grande (g)): ').lower()
                            if change_clasification == 'e':
                                for name in menu:
                                    menu[name][1] = 'Empaque'
                                    print('El cambio de clasificacion del plato fue realizado!')
                            elif change_clasification == 'p':
                                for name in menu:
                                    menu[name][1] = 'Preparacion'
                                    print('El cambio de clasificacion del plato fue realizado!')
                            else: 
                                print('\n ERROR dato invalido')
                        
                        #Cambio de clasificacion de bebida
                        elif tipo == 'a':
                            change_clasification = input('Ingrese la nueva clasificacion del plato, empaque (e) o preparacion (p): ').lower()
                            if change_clasification == 's':
                                for name in menu:
                                    menu[name][1] = 'Pequeño'
                                    print('El cambio de clasificacion del plato fue realizado!')
                            elif change_clasification == 'm':
                                for name in menu:
                                    menu[name][1] = 'Mediano'
                                    print('El cambio de clasificacion del plato fue realizado!') 
                            elif change_clasification == 'g':
                                for name in menu:
                                    menu[name][1] = 'Grande'
                                    print('El cambio de clasificacion del plato fue realizado!') 
                            else: 
                                print('\n ERROR dato invalido')
                    
                    #Cambio de precio de producto
                    elif cambio == 'p':
                        change_price = int(input('Ingrese nuevo precio del alimento: '))
                        new_price = change_price + change_price*0.16
                        for name in menu:
                            menu[name][0] = new_price
                            print(menu)
                            print('El cambio de precio fue realizado exitosamente!')
                    
                    else: 
                        print('\n ERROR dato invalido')



            else:
              print('El plato ingresado no existe')

        #Agregar combos
        elif funcionalidades == 4:
            while True:
                    #Nombre del alimento/bebida
                    name = input('Ingrese nombre del combo: ').capitalize()
                    try:
                        #precio del alimento/bebida (sin IVA)
                        price = int(input('Precio del producto: '))
                        
                    except ValueError as identifier:
                        print('El precio ingresado es invalido')
                    #precio con IVA incluido
                    price += price*0.16
                    #Clasificacion del producto, si es bebida o comida
                    
                    products = []
                    while True:    
                        food_in_combo = input('Ingrese alimento que incluye el combo (ingresa "no" cuando no desee continuar ingresando productos): ').capitalize()
                        if food_in_combo == 'No':
                            if len(products) < 2:
                                print('Lo siento el combo no puede tener menos de 2 productos')
                            elif len(products) >= 2:
                                break
                        products.append(food_in_combo)  

                    break
            
             
                  
            combo = Combos(name, products, price)
            
            menu_combos[name] =[price,products]
            with open("menu_combos.txt", 'a') as c:
                for combo in menu_combos:
                    c.write(f'\n{combo}: {menu_combos[combo][0]}$, incluye:{menu_combos[combo][1]}')
            print('\nRegistrado exitosamente')
            print(menu_combos)
            return combo, menu_combos

        #Eliminar combo del menu de combos
        elif funcionalidades == 5:
            name_search = input('Ingresa el nombre del combo que desea eliminar: ').capitalize()
            
            if name_search in menu_combos.keys():
                del menu_combos[name_search]
                print(f'el combo {name_search} fue eliminado/a del menu')
                 
            else:
                print('Lo siento el plato que busca no existe en el menu')

        #Buscar platos segun nombre o rango de precio
        elif funcionalidades == 6:
            
            busqueda = input('Desea buscar segun nombre "n" o segun rango de precio "p" ').lower()
            
            #Busqueda segun nombre
            if busqueda == 'n':
                name = input('Ingresa el plato/bebida que desea buscar: ').capitalize()
                if name in menu.keys():
                    print(f'''
                    PLATO/BEBIDA: {name}
                    PRECIO: {menu[name][0]}$
                    CLASIFICACION: {menu[name][1]}''' )     
                else:
                    print(f'{name} no existe')
            
            #Busqueda segun rango de precio
            elif busqueda == 'p':
                rango = input('Precios mayores al ingresado (c), menores al ingresado (b)')
                try:
                    price_search = int(input('Ingrese rango de precio: '))
                except ValueError as identifier:
                        print('El dato ingresado es invalido')
                if rango == 'b':
                    for plato in menu.keys():
                        #Buscar platos igual o mas baratos al precio indicado
                        if menu[plato][0] <= price_search:
                           
                            print(f'''
                        PLATO/BEBIDA: {plato}
                        PRECIO: {menu[plato][0]}
                        CLASIFICACION: {menu[plato][1]}''' )
                
                if rango == 'c':
                    for plato in menu.keys():
                        #Buscar platos igual o mas caros al precio indicado
                        if menu[plato][0] >= price_search:                            
                            print(f'''
                        PLATO/BEBIDA: {plato}
                        PRECIO: {menu[plato][0]}
                        CLASIFICACION: {menu[plato][1]}''' )
                else:
                    print('Lo siento dato invalido') 

            else:
                print('Lo siento dato invalido')            

        #Buscar combos segun nombre o rango de precio
        elif funcionalidades == 7:
            busqueda = input('Desea buscar segun nombre "n" o segun rango de precio "p" ').lower()
            if busqueda == 'n':
                name_search = input('Ingresa el combo que desea buscar: ').capitalize()
                #Buscar segun nombre
                if name_search in menu_combos.keys():
                    print(f'''
                    COMBO: {name_search}
                    INCLUYE: {menu_combos[name_search][1]}
                    PRECIO: {menu_combos[name_search][0]}$''' )
                else:
                    print(f'{name_search} no existe')
            
            #Buscar segun precio
            elif busqueda == 'p':
                rango = input('Precios mayores al ingresado (c), menores al ingresado (b)')
                try:
                    price_search = int(input('Ingrese rango de precio: '))
                except ValueError as identifier:
                        print('El dato ingresado es invalido')
                if rango == 'b':
                    for plato in menu_combos.keys():
                        #Buscar platos igual o mas baratos al precio indicado
                        if menu_combos[plato][0] <= price_search:
                            print(f'''
                        PLATO/BEBIDA: {plato}
                        PRECIO: {menu_combos[plato][0]}
                        CLASIFICACION: {menu_combos[plato][1]}''' )
                        
                      
                elif rango == 'c':
                    for plato in menu_combos.keys():
                        #Buscar platos igual o mas caros al precio indicado
                        if menu_combos[plato][0] >= price_search:
                            print(f'''
                        PLATO/BEBIDA: {plato}
                        PRECIO: {menu_combos[plato][0]}
                        CLASIFICACION: {menu_combos[plato][1]}''' )
                        
                else:
                    print('Lo siento dato invalido') 
            
            else:
                print('Lo siento dato invalido') 
        

        else:
            print('Dato Invalido')
            break


def tours(cedula,tour_1,tour_2,tour_3,tour_4,date):
    
    while True:
        try:
            dni = input('Ingrese el DNI: ')
            tour_op = int(input('''
            1- Tour en el puerto 
            2- Degustación de comida local 
            3- Trotar por el pueblo/ciudad
            4- Visita a ligares históricos
            5- Volver al menu
            >'''))
        except ValueError as identifier:
            print('El dato ingresado es invalido')
    
                    
        if tour_op == 1:
            print('El tour en el puerto tiene un costo de $30/persona y comienza las 7am con un cupo total de 10 personas')
            
            try:
                cant_ticket = int(input('Ingrese la cantidad de tickets por comprar: '))
                print()
            except ValueError as identifier:
                print('El dato ingresado es invalido')
            #Llevar cantidad de tickets contados
            tour_1.append(cant_ticket)
            while sum(tour_1) <= 10:
                #monto de ticket por persona
                monto = cant_ticket*30
                if  cant_ticket >= 1 and cant_ticket < 3:
                    print(  f'FECHA DE COMPRA: {date}\n' 
                            f'TOUR EN EL PUERTO 7 A.M\n'\
                            f'CANTIDAD DE BOLETOS: {cant_ticket}\n'\
                            f'MONTO TOTAL: ${monto}' )
                    break
            
                elif cant_ticket == 3:
                    descuento = 30*0.10
                    monto_total = monto - descuento
                    print(  f'FECHA DE COMPRA: {date}\n' 
                            f'TOUR EN EL PUERTO 7 A.M\n'\
                            f'CANTIDAD DE BOLETOS: {cant_ticket}\n'\
                            f'MONTO TOTAL: ${monto_total}' )
                    break

                elif cant_ticket == 4:
                    descuento = 60*0.10
                    monto_total = monto - descuento
                    print(  f'FECHA DE COMPRA: {date}\n'
                            f'TOUR EN EL PUERTO 7 A.M\n'\
                            f'CANTIDAD DE BOLETOS: {cant_ticket}\n'\
                            f'MONTO TOTAL: ${monto_total}' )
                    break

                else: 
                    print('Lo siento solo se pueden vender hasta 4 entradas por familia')
                    break
            if sum(tour_1) > 10:
                print('Lo siento, el tour llego a su capacidad maxima')
                tour_1.pop(-1)
    
        if tour_op == 2:
            print('La degustación de comida local tiene un costo de $100/persona y comienza las 12pm con un cupo total de 100 personas')
            
            try:
                cant_ticket = int(input('Ingrese la cantidad de tickets por comprar: '))
                print()
            except ValueError as identifier:
                print('El dato ingresado es invalido')
            #Llevar cantidad de tickets contados
            tour_2.append(cant_ticket)
            while sum(tour_2) <= 100:
                #monto de ticket por persona
                monto = cant_ticket*100
                if  cant_ticket > 1 and cant_ticket <= 2:
                    print(  f'FECHA DE COMPRA: {date}\n' 
                            f'DEGUSTACION 12 P.M\n'\
                            f'CANTIDAD DE BOLETOS: {cant_ticket}\n'\
                            f'MONTO TOTAL: ${monto}' )
                    break
            
                else: 
                    print('Lo siento solo se pueden vender hasta 2 entradas por familia')
            if sum(tour_2) > 100:
                print('Lo siento, el tour llego a su capacidad maxima')
                tour_2.pop(-1)

        if tour_op == 3:
            print('Trotar por el pueblo/ciudad no tiene costo, comienza las 6am con cupos ilimitados')
            
            try:
                cant_ticket = int(input('Ingrese la cantidad de tickets por comprar: '))
                print()
            except ValueError as identifier:
                print('El dato ingresado es invalido')
            #Llevar cantidad de tickets contados
            tour_3.append(cant_ticket)
            #monto de ticket por persona
            monto = 0 
            
            print(  f'FECHA DE COMPRA: {date}\n' 
                    f'TROTAR POR CIUDAD/PUEBLO 6A.M\n'\
                    f'CANTIDAD DE BOLETOS: {cant_ticket}\n'\
                    f'MONTO TOTAL: ${monto}' )
            break

        if tour_op == 4:
            print('La visita a lugares históricos tiene un costo de $40/persona y comienza las 10am con un cupo total de 15 personas')

            try:
                cant_ticket = int(input('Ingrese la cantidad de tickets por comprar: '))
                print()
            except ValueError as identifier:
                print('El dato ingresado es invalido')
            #Llevar cantidad de tickets contados
            tour_4.append(cant_ticket)
            while sum(tour_4) <= 15:
                #monto de ticket por persona
                monto = cant_ticket*40
                if  cant_ticket > 1 and cant_ticket <= 2:
                    print(  f'FECHA DE COMPRA: {date}\n' 
                            f'VISITA LUGARES HISTORICOS 10A.M\n'\
                            f'CANTIDAD DE BOLETOS: {cant_ticket}\n'\
                            f'MONTO TOTAL: ${monto}' )
                    break
            
                elif cant_ticket == 3:
                    descuento = 40*0.10
                    monto_total = monto - descuento
                    print(  f'FECHA DE COMPRA: {date}\n' 
                            f'TOUR EN EL PUERTO 7 A.M\n'\
                            f'CANTIDAD DE BOLETOS: {cant_ticket}\n'\
                            f'MONTO TOTAL: ${monto_total}' )
                    break

                elif cant_ticket == 4:
                    descuento = 80*0.10
                    monto_total = monto - descuento
                    print(  f'FECHA DE COMPRA: {date}\n' 
                            f'TOUR EN EL PUERTO 7 A.M\n'\
                            f'CANTIDAD DE BOLETOS: {cant_ticket}\n'\
                            f'MONTO TOTAL: ${monto_total}' )
                    break

                else: 
                    print('Lo siento solo se pueden vender hasta 4 entradas por familia')
            
            if sum(tour_4) > 15:
                print('Lo siento, el tour llego a su capacidad maxima')
                tour_4.pop(-1)

        else:
            break
        
    return tour_1,tour_2,tour_3,tour_4
    
        

def main():
    
    response = requests.get('https://saman-caribbean.vercel.app/api/cruise-ships')
    saman_caribbean = response.json()
    cruceros = []
    tour_1 = tour_2 = tour_3 = tour_4 = []
    menu = {}
    menu_combos = {}
    date = datetime.now()
    comida = []
    combos = []
    simple_r = []
    premium_r = []
    vip_r = []
    room_list = []
    cedula = []
    cruceros_info(cruceros,saman_caribbean)
    rooms_info(simple_r,premium_r, vip_r,saman_caribbean)
    while True:
        try:
            option = int(input(''''
            BIENVENIDO A SAMAN CARIBBEAN\n
            Escoga la operación que desea realizar:
            1 - Información general sobre los cruceros
            2 - Gestión de habitaciones
            3 - Venta de Tours
            4 - Gestión del restaurante
            >>> ''' ))
        except ValueError as identifier:
            print('El dato ingresado es invalido')

        if option == 1:
            cruceros = cruceros_info(cruceros, saman_caribbean)
            print(cruceros[0])
            print(cruceros[1])
            print(cruceros[2])
            print(cruceros[3])
        
        
        elif option == 2:
            try:
                option_hab = int(input('''
                1) Informacion de habitachiones 
                2) Vender habitación 
                >>> '''))
            except ValueError as identifier:
                print('El dato ingresado es invalido')
     
            #Buscar disponibilidad de habitacion en crucero escogido y realizar compra de boletos
            if option_hab == 1:
                cruceros_info(cruceros, saman_caribbean)
                rooms_info(simple_r, premium_r, vip_r, saman_caribbean)
                try:
                    option = int(input(f'''Escoja el crucero que le interesa: 
                    1) {cruceros[0].get_name()}
                    2) {cruceros[1].get_name()}
                    3) {cruceros[2].get_name()}
                    4) {cruceros[3].get_name()}
                    > '''))
                except ValueError as identifier:
                    print('El dato ingresado es invalido')
                if option == 1:
                    print(f'{simple_r[0]}')
                    print(premium_r[0])
                    print(f"{vip_r[0]}\n")
                elif option == 2:
                    print()
                    print(simple_r[1])
                    print(premium_r[1])
                    print(f'{vip_r[1]}\n')

                elif option == 3:
                    print()
                    print(simple_r[2])
                    print(premium_r[2])
                    print(f"{vip_r[2]}\n")

                elif option == 4:
                    print()
                    print(simple_r[3])
                    print(premium_r[3])
                    print(f"{vip_r[3]}\n")
                else:
                    print('Dato ingresado incorrecto')

            elif option_hab == 2:
                sell_hab(cedula, room_list, cruceros, simple_r, premium_r, vip_r, saman_caribbean) 

        elif option == 3:
            tours(cedula,tour_1, tour_2, tour_3, tour_4, date)

        elif option == 4:
            menu_restautante = restaurante(comida,menu, menu_combos)

        else:
            print('Error, intente de nuevo')

        
            

             

main()