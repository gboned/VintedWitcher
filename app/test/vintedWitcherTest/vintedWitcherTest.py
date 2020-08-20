from app.vintedWitcher.VintedWitcher import VintedWitcher
from app.equipment.Equipment import Equipment


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


if __name__ == '__main__':
    vintedWitcherTest()
