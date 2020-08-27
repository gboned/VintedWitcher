from app.specialEquipment.SpecialEquipment import SpecialEquipment


class VintedWitcher:

    def __init__(self, location, stock):

        self.location = location
        self.stock = stock
        self.servicePrice = 0

    def addToStock(self, component):
        self.stock.append(component)

    def sell(self, component):
        self.stock.remove(component)
        print(f'{component.getName()} has been sold for ' + \
             str(component.getPrice()) + ' crowns.')

    def makeRepair(self, component):
        if isinstance(component, SpecialEquipment):
            self.servicePrice = component.specialRepair()
        else:
            self.servicePrice = component.repair() # Repara el componente y devuelve el precio del servicio
        print(f'Price: {self.servicePrice} crowns.')

    def makeSharpering(self, component):
        if isinstance(component, SpecialEquipment):
            self.servicePrice = component.specialSharp()
        else:
            self.servicePrice = component.sharp() # Afila el componente y devuelve el precio del servicio
        print(f'Price: {self.servicePrice} crowns.')

    def findSpecialSet(self, school):
        specialComponents = []
        for component in self.stock:
           if isinstance(component, SpecialEquipment):
               if component.getSchool() == school:
                   specialComponents.append(component)
        return specialComponents

    def getLocation(self):
        return self.location

    def setLocation(self, newLocation):
        self.location = newLocation

    def getStock(self):
        return self.stock

    def setStock(self, newStock):
        self.stock = newStock

    def getServicePrice(self):
        return self.servicePrice

    def setServicePrice(self, newServicePrice):
        self.servicePrice = newServicePrice

    def __str__(self):
        return self.location
    