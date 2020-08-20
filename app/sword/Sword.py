from app.equipment.Equipment import Equipment


class Sword(Equipment):

    def __init__(self, name, description, breakage, price, sharpering):
        super().__init__(name, description, breakage, price)
        self.sharpering = sharpering

    def sharp(self):
        self.sharpering = 100
        print(f'Sharpered {self.name}.')

    def getSharpering(self):
        return self.sharpering

    def setShapering(self, newSharpering):
        self.sharpering = newSharpering

    def __str__(self):
        return f'-{self.name}: {self.description} ' + str(self.breakage) + '% ' + 'of breakage. ' + str(self.sharpering) + '% ' + 'sharpered. ' + str(self.price) + ' crowns.'