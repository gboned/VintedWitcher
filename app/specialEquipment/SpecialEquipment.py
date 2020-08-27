from app.equipment.Equipment import Equipment


class SpecialEquipment(Equipment):

    def __init__(self, name, description, breakage, price, school):
        Equipment.__init__(self, name, description, breakage, price)
        self.school = school

    def specialRepair(self):
        specialPrice = self.repair() * 2
        return specialPrice

    def getSchool(self):
        return self.school

    def setSchool(self, newSchool):
        self.school = newSchool