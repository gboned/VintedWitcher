from app.vintedWitcher.VintedWitcher import VintedWitcher
from app.equipment.Equipment import Equipment
from app.sword.Sword import Sword
from app.steelSword.SteelSword import SteelSword
from app.silverSword.SilverSword import SilverSword


def vintedWitcherTest():

    vintedWitcherInstance = VintedWitcher(
        'Novigrad',     # location
        []    # stock
    )

    assert vintedWitcherInstance.getLocation() == 'Novigrad'

    crossbow = Equipment(
        'Crossbow',     # name
        '''A mechanically assisted bow which is used when more power is 
        required, either to launch heavier projectiles or to launch a more 
        conventional one a longer distance.''',    # description
        56,     # breakage (in %)
        123     # price (in crowns)
    )

    assert vintedWitcherInstance.getStock() == []
    vintedWitcherInstance.addToStock(crossbow)
    assert len(vintedWitcherInstance.getStock()) == 1
    assert vintedWitcherInstance.getStock()[0].getName() == crossbow.getName()

    vintedWitcherInstance.sell(crossbow)
    assert vintedWitcherInstance.getStock() == []


    assaultGauntlets = Equipment(
        'Assaunt Gauntlets',# name
        'These are heavy armor gauntlets.',    # description
        60,     # breakage (in %)
        80,     # price (in crowns)
    )

    vintedWitcherInstance.makeRepair(assaultGauntlets)
    assert assaultGauntlets.getBreakage() == 0
    assert vintedWitcherInstance.getServicePrice() == 120


    rustySword = SteelSword(
        'Rusty Sword',    # name
        '''Is a steel sword in The Witcher and is the first weapon Geralt 
        receives in the Prologue.''', # description
        80,     # breakage (in %)
        50,     # price (in crowns)
        10,     # shapering (in %)      
    )

    vintedWitcherInstance.makeRepair(rustySword)
    assert rustySword.getBreakage() == 0
    assert vintedWitcherInstance.getServicePrice() == 160

    vintedWitcherInstance.makeSharpering(rustySword)
    assert rustySword.getSharpering() == 100
    vintedWitcherInstance.getServicePrice() == 135

    eirlithrad = SilverSword(
        'Eirlithrad',   # name
        'It is a silver sword for killing monsters.',   # description
        20,     # breakage (in %)
        300,    # price (in crowns)
        40,     # sharpering     
    )

    vintedWitcherInstance.makeRepair(eirlithrad)
    assert eirlithrad.getBreakage() == 0
    assert vintedWitcherInstance.getServicePrice() == 0

    vintedWitcherInstance.makeSharpering(eirlithrad)
    assert eirlithrad.getSharpering() == 100
    vintedWitcherInstance.getServicePrice() == 180


if __name__ == '__main__':
    vintedWitcherTest()
