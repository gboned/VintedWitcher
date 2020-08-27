from app.sword.Sword import Sword


class SilverSword(Sword):

    def __init__(self, name, description, breakage, price, sharpering):
        super().__init__(name, description, breakage, price, sharpering)


    def sharp(self):
        servicePrice = 0
        if self.sharpering < 50:
            servicePrice = (100 - self.sharpering) * 3
        self.sharpering = 100
        print(f'Sharpered {self.name}')
        return int(round(servicePrice))