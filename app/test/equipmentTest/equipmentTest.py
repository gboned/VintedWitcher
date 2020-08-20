from app.equipment.Equipment import Equipment


def equipmentTest():
    crossbow = Equipment(
        'Crossbow',     # name
        '''A mechanically assisted bow which is used when more power is 
        required, either to launch heavier projectiles or to launch a more 
        conventional one a longer distance.''',    # description
        56,     # breakage (in %)
        123     # price (in crowns)
    )

    assert crossbow.getName() == 'Crossbow'
    assert crossbow.getBreakage() == 56
    assert crossbow.getPrice() == 123

    crossbow.repair()
    assert crossbow.getBreakage() == 0