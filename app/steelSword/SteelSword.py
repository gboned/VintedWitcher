from app.sword.Sword import Sword


class SteelSword(Sword):

    def __init__(self, name, description, breakage, price, sharpering):
        Sword.__init__(self, name, description, breakage, price, sharpering)

    def sharp(self):
        servicePrice = 0
        if self.sharpering < 40:
            servicePrice = (100 - self.sharpering) * 1.5
        self.sharpering = 100
        print(f'Sharpered {self.name}')
        return int(round(servicePrice))