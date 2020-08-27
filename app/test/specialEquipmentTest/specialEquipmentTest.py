from app.specialEquipment.SpecialEquipment import SpecialEquipment


def specialEquipmentTest():

    wolvenTrousers = SpecialEquipment(
        'Wolven Trousers',  #name
        'Craftable medium armor trousers.',     # description
        60,     # breakage (in %)
        400,    # price (in crowns)
        'Wolf School',      # witcher school
    )

    assert wolvenTrousers.getSchool() == 'Wolf School'

    assert wolvenTrousers.getBreakage() == 60
    wolvenTrousers.repair()
    assert wolvenTrousers.getBreakage() == 0


if __name__ == '__main__':
    specialEquipmentTest()