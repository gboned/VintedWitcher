from app.specialEquipment.SpecialEquipment import SpecialEquipment
from app.steelSword.SteelSword import SteelSword


class SpecialSteelSword(SpecialEquipment, SteelSword):

    def __init__(self, name, description, breakage, price, sharpering, school):
        SpecialEquipment.__init__(self, name, description, breakage, price, school)
        SteelSword.__init__(self, name, description, breakage, price, sharpering)

    def specialSharp(self):
        return self.sharp() * 2