from app.equipment.Equipment import Equipment
from app.sword.Sword import Sword
# from app.silverSword.SilverSword import SilverSword
# from app.steelSword.SteelSword import SteelSword
# from app.specialEquipment.SpecialEquipment import SpecialEquipment
# from app.specialSteelSword.SpecialSteelSword import SpecialSteelSword
from app.vintedWitcher.VintedWitcher import VintedWitcher



def main():


    # 1. AÑADIR EQUIPO AL INVENTARIO DE LA TIENDA

    print('-----------------------------------------------------------------------------------------------------------')
    print('ADDING EQUIPMENT TO BE SOLD...')
    print('-----------------------------------------------------------------------------------------------------------')

    # La tienda
    vintedWitcherInstance = VintedWitcher(
        'Novigrad',     # location
        []    # stock
    )

    # Los componentes

    crossbow = Equipment(
        'Crossbow',     # name
        '''A mechanically assisted bow which is used when more power is 
        required, either to launch heavier projectiles or to launch a more 
        conventional one a longer distance.''',    # description
        56,     # breakage (in %)
        123     # price (in crowns)
    )
    assaultGauntlets = Equipment(
        'Assaunt Gauntlets',# name
        'These are heavy armor gauntlets.',    # description
        60,     # breakage (in %)
        80,     # price (in crowns)
    )

    # Añadimos los componentes al inventario de la tienda

    vintedWitcherInstance.addToStock(crossbow)
    vintedWitcherInstance.addToStock(assaultGauntlets)

    # Y listamos el inventario por pantalla

    print('Displaying available equipment in Vinted Witcher...')

    for component in vintedWitcherInstance.getStock():
        print(component)



    # 2. VENDER COMPONENTES

    print('-----------------------------------------------------------------------------------------------------------')
    print('SELLING COMPONENTS...')
    print('-----------------------------------------------------------------------------------------------------------')

    vintedWitcherInstance.sell(crossbow)
    
    # Listamos los componentes que quedan entonces en la tienda
    
    print('Displaying available equipment in Vinted Witcher...')

    for component in vintedWitcherInstance.getStock():
        print(component)
    


    # 3. REPARAR UN COMPONENTE

    print('-----------------------------------------------------------------------------------------------------------')
    print('REAPAIRING CROSSBOW...')
    print('-----------------------------------------------------------------------------------------------------------')

    # Usamos directamente el método repair() de la clase Equipment

    crossbow.repair()

    print('Crossbow breakage has been reduced to ' + \
        str(crossbow.getBreakage()) + '%.')



    # 4. REPARAR UN COMPONENTE CON UN DESGASTE SUPERIOR AL 40%

    print('-----------------------------------------------------------------------------------------------------------')
    print('REAPAIRING ASSAULT GAUNTLETS...')
    print('-----------------------------------------------------------------------------------------------------------')

    # Abstraemos creando el método makeRepair() en la clase VintedWitcher

    vintedWitcherInstance.makeRepair(assaultGauntlets)
    print('Assaunt gauntlets breakage has been reduced to ' + \
        str(assaultGauntlets.getBreakage()) + '%.')



    # 5. TRATO ESPECIAL DE ESPADAS: filo, afilar

    print('-----------------------------------------------------------------------------------------------------------')
    print('CREATING A SWORD...')
    print('-----------------------------------------------------------------------------------------------------------')

    # Creamos una espada...

    rustySword = Sword(
        'Rusty Sword',    # name
        '''Is a steel sword in The Witcher and is the first weapon Geralt 
        receives in the Prologue.''', # description
        80,     # breakage (in %)
        50,     # price (in crowns)
        10,     # shapering (in %)      
    )

    print(rustySword)

    # la reparamos...

    print('Repairing Rusty Sword...')

    vintedWitcherInstance.makeRepair(rustySword)

    print('Rusty Sword breakage has been reduced to ' + \
        str(rustySword.getBreakage()) + '%.')

    # y la afilamos

    print('Sharpering the Rusty Sword...')

    vintedWitcherInstance.makeSharpering(rustySword)

    print('Rusty Sword sharpering has been restored to ' + \
        str(rustySword.getSharpering()) + '%.')



    # 6. TRATO ESPECIAL PARA ESPADAS DE ACERO: PRECIO DE AFILADO

    """
    Para esta historia de usuario tendremos que modificar algo del código 
    escrito para la anterior esperando que el coste del servicio resulte 
    de 135 coronas. 
    
    Aquí nos puede ser útil hacer de Sword una clase abstracta con el 
    @abstractmethod sharp() -necesitarás importar ABC y abstractmethod de la 
    librería abc de python- y definir el comportamiento en una clase SteelSword.

    Otra pista: las clases abstractas no se pueden instanciar, por lo que habrá
    que hacer alguna modificación en la definición de rustySword. 

    (* Revisar los casos test *)
    """
    


    # 7. TRATO ESPECIAL PARA ESPADAS DE PLATA: PRECIO DE AFILADO

    print('-----------------------------------------------------------------------------------------------------------')
    print('CREATING A SILVER SWORD...')
    print('-----------------------------------------------------------------------------------------------------------')

    # Creamos una espada de plata...

    eirlithrad = SilverSword(
        'Eirlithrad',   # name
        'It is a silver sword for killing monsters.',   # description
        20,     # breakage (in %)
        300,    # price (in crowns)
        40,     # sharpering
    )

    print(eirlithrad)

    # y la afilamos

    print('Sharpering Eirlithrad...')

    vintedWitcherInstance.makeSharpering(eirlithrad)

    print('Eirlithrad sharpering has been restored to ' + \
        str(eirlithrad.getSharpering()) + '%.')



    # 8. EQUIPO ESPECIAL: COMPONENTES DE SETS DE ESCUELAS DE BRUJOS

    print('-----------------------------------------------------------------------------------------------------------')
    print('CREATING SPECIAL EQUIPMENT...')
    print('-----------------------------------------------------------------------------------------------------------')

    # Creamos un componente de la Escuela de los Lobos

    wolvenTrousers = SpecialEquipment(
        'Wolven Trousers',  #name
        'Craftable medium armor trousers.',     # description
        60,     # breakage (in %)
        400,    # price (in crowns)
        'Wolf School',      # witcher school
    )

    print(wolvenTrousers)



    # 9. VENDER COMPONENTES DE UNA ESCUELA DE BRUJO CONCRETA

    print('-----------------------------------------------------------------------------------------------------------')
    print('CREATING AND SELLING SPECIAL EQUIPMENT...')
    print('-----------------------------------------------------------------------------------------------------------')

    # Creamos otro componente -una espada de acero- de la Escuela de los Lobos

    print('Creating Wolven Trousers...')

    wolvenSteelSword = SpecialSteelSword(
        'Wolven Steel Sword',  #name
        'A craftable steel sword.',  # description
        70,     # breakage (in %)
        800,    # price (in crowns)
        30,     # shapering (in %)
        'Wolf School',      # witcher school
    )

    print(wolvenSteelSword)

    # Añadimos los componentes de la Escuela de los Lobos al inventario

    print('\n')
    print('Adding Wolven components to Vinted Witcher stock...')

    vintedWitcherInstance.addToStock(wolvenTrousers) 
    vintedWitcherInstance.addToStock(wolvenSteelSword)

    print('\n')
    print('Displaying available equipment in Vinted Witcher...')

    for component in vintedWitcherInstance.getStock():
        print(component)

    # Buscamos los componentes de la Escuela de los Lobos...

    print('\n')
    print('Searching wolven components for selling...')

    wolvenSet = vintedWitcherInstance.findSpecialSet('Wolf School')

    # y los vendemos

    for component in wolvenSet:
        vintedWitcherInstance.sell(component)

    print('\n')
    print('Displaying available equipment in Vinted Witcher...')

    for component in vintedWitcherInstance.getStock():
        print(component)



    # 10. REPARAR Y AFILAR COMPONENTES DEL SET DE LA ESCUELA DE LOS LOBOS

    print('-----------------------------------------------------------------------------------------------------------')
    print('REPAIR AND SHARP OF SPECIAL EQUIPMENT...')
    print('-----------------------------------------------------------------------------------------------------------')
    
    # Reparamos los Wolven Trousers

    print('Repairing Wolven Trousers...')
    vintedWitcherInstance.makeRepair(wolvenTrousers)

    print('Wolven Trousers breakage has been reduced to ' + \
        str(wolvenTrousers.getBreakage()) + '%.')
    
    print('\n')

    # Afilamos la Wolven Steel Sword
    
    print('Sharpering Wolven Steel Sword...')
    vintedWitcherInstance.makeSharpering(wolvenSteelSword)

    print('Wolven Steel Sword sharpering has been restored to ' + \
        str(wolvenSteelSword.getSharpering()) + '%.')



if __name__ == '__main__':
    main()