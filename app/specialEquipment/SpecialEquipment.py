from app.equipment.Equipment import Equipment


class SpecialEquipment(Equipment):

    def __init__(self, name, description, breakage, price, school):
        super().__init__(name, description, breakage, price)
        self.school = school

    def getSchool(self):
        return self.school

    def setSchool(self, newSchool):
        self.school = newSchool