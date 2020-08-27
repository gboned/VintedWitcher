from app.specialEquipment.SpecialEquipment import SpecialEquipment
from app.steelSword.SteelSword import SteelSword
from app.specialSteelSword.SpecialSteelSword import SpecialSteelSword


def specialSteelSwordTest():

    wolvenSteelSword = SpecialSteelSword(
    'Wolven Steel Sword',  #name
    'A craftable steel sword.',  # description
    70,     # breakage (in %)
    800,    # price (in crowns)
    30,     # shapering (in %)
    'Wolf School',      # witcher school
)

    assert wolvenSteelSword.getSharpering() == 30
    wolvenSteelSword.sharp()
    assert wolvenSteelSword.getSharpering() == 100

    assert wolvenSteelSword.getSchool() == 'Wolf School'


if __name__ == '__main__':
    specialSteelSwordTest()