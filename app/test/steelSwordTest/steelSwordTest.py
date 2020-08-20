from app.steelSword.SteelSword import SteelSword


def steelSwordTest():
    rustySword = SteelSword(
        'Rusty Sword',    # name
        '''Is a steel sword in The Witcher and is the first weapon Geralt 
        receives in the Prologue.''', # description
        80,     # breakage (in %)
        50,     # price (in crowns)
        10,     # shapering (in %)      
    )
    
    assert rustySword.getSharpering() == 10

if __name__ == '__main__':
    steelSwordTest()