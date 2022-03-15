consumo_energia = {
    'Coca Codo Sinclair':{
        'Quito': {'consumos': (400, 432, 400, 420, 432, 460, 432, 400, 432, 300, 213), 'tarifa': 65},
        'Guayaquil': {'consumos': (120, 55, 32, 120, 75, 32, 150, 55, 32, 120, 97, 32),'tarifa': 84},
    },
    'Sopladora': {
        'Guayaquil':{ 'consumos': (310, 220, 321, 310, 220, 321, 310, 220, 321, 310, 220, 321),'tarifa':55},
        'Quito': { 'consumos': (400, 432, 587, 400, 432, 587, 400, 432, 587, 400, 432, 587),'tarifa': 79},
        'Loja': { 'consumos': (50, 32, 32, 50, 32, 32, 50, 32, 32, 50, 32, 32),'tarifa': 32},
 },
}
tot_coca_codo_g = (120 + 55 + 32 + 120 + 75 + 32 + 150 + 55 + 32 + 120 + 97 + 32)
tot_coca_codo_q = (400 + 432 + 400 + 420 + 432 + 460 + 432 + 400 + 432 + 300 + 213)
tot_sopladora_g = (310 + 220 + 321 + 310 + 220 + 321 + 310 + 220 + 321 + 310 + 220 + 321)
tot_sopladora_q = (400 + 432 + 587 + 400 + 432 + 587 + 400 + 432 + 587 + 400 + 432 + 587)
tot_sopladora_l = (50 + 32 + 32 + 50 + 32 + 32 + 50 + 32 + 32 + 50 + 32 + 32)

informacion = {
 'costa': ('Guayaquil', 'Manta'),
 'sierra': ('Quito', 'Ambato', 'Loja'),
 'oriente': ('Tena', 'Nueva Loja')
}

costa = tot_coca_codo_g + tot_sopladora_g
sierra = tot_sopladora_q + tot_coca_codo_q + tot_sopladora_l
oriente = ('No hay planta en oriente')

print('''
    *******************************
        MENU PRINCIPAL
    *******************************
    ''')

opcion=-1
def menu():
    print('<1>. Total de MWh en Planta y Ciudad ')
    print('<2>. Total de Energia por Ciudad ')
    print('<3>. Dinero Recaudado por Region ')
    print('<4>. Para abandonar el programa')
    
while opcion != 0:
        menu ()
        opcion = int(input("Elija una opcion: "))
    
    
        if opcion == 1:
            
            print('''
            *********************************
            TOTAL DE MWh EN PLANTA Y CIUDAD
            *********************************
            ''')

            n_planta = input('Ingrese la planta: ')

            if n_planta == 'Coca Codo Sinclair':
                n_ciudad = input('Coloque el nombre de la ciudad: ')

                if n_ciudad == 'Quito':
                    print('Total de Mwh de consumo en Coca Codo Sinclair, Quito: ', tot_coca_codo_q)
                    print('Con tarifa de: ', consumo_energia['Coca Codo Sinclair']['Quito']['tarifa'])
                elif n_ciudad == 'Guayaquil':
                    print('Total de MWh de consumo en Coca Codo Sinclair, Guayaquil: ', tot_coca_codo_g, 'Megavatios')
                    print('Con tarifa de: ', consumo_energia['Coca Codo Sinclair']['Guayaquil']['tarifa'])
                elif n_ciudad =='Loja':
                    print("No existe planta de Coca Codo Sinclair en Loja")
            print()

            if n_planta == 'Sopladora':
                n_ciudad = input('Coloque el nombre de la ciudad: ')

                if n_ciudad == 'Quito':
                    print('Total de MWh de consumo en Sopladora, Quito: ', tot_sopladora_q)
                    print('Con tarifa de: ', consumo_energia['Sopladora']['Quito']['tarifa'])
                elif n_ciudad == 'Guayaquil':
                    print('Total de MWh de consumo en Sopladora, Guayaquil: ', tot_sopladora_g)
                    print('Con tarifa de: ', consumo_energia['Sopladora']['Guayaquil']['tarifa'])
                elif n_ciudad == 'Loja':
                    print('Total de MWh de consumo en Sopladora, Loja: ', tot_sopladora_l)
                    print('Con tarifa de: ', consumo_energia['Sopladora']['Loja']['tarifa'])
                else:
                    print("Escriba correctamente")


        elif opcion == 2:
            print('''
            **************************************
                TOTAL DE ENERGIA POR CIUDAD
            **************************************
            '''),
            

            n_ciudad2 = input('Ingrese la ciudad: ')

            if n_ciudad2 == 'Guayaquil':
                print('Total de MWh, Coca Codo Sinclair: ', tot_coca_codo_g)
                print('Total de MWh, Sopladora:', tot_sopladora_g)
            elif n_ciudad2 == 'Quito':
                print('Total de MWh, Coca Codo Sinclair: ', tot_coca_codo_q)
                print('Total de MWh, Sopladora:', tot_sopladora_q)
            elif n_ciudad2 == 'Loja':
                print('Total de MWh, Sopladora:', tot_sopladora_l)
            else:
                print('Ninguna planta otorga energía en esa ciudad ')
            print()

        elif opcion == 3:
            print('''
            ********************************
                    DINERO RECAUDADO
            ********************************        
            '''),

            n_region = input('Ingrese nombre de Región: ')

            if n_region == 'Costa':
                print('Total Recaudado en Costa: ', costa, 'dolares')
            elif n_region == 'Sierra':
                print('Total Recaudado en Sierra: ', sierra, 'dolares')
            elif n_region == 'Oriente':
                print(oriente)
            else:
                print('Escriba correctamente')
        elif opcion==4:
            print ('Gracias')
            quit()