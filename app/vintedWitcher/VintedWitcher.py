class VintedWitcher:

    def __init__(self, location, stock):

        self.location = location
        self.stock = stock

    def addToStock(self, component):
        self.stock.append(component)

    def getLocation(self):
        return self.location

    def setLocation(self, newLocation):
        self.location = newLocation

    def getStock(self):
        return self.stock

    def setStock(self, newStock):
        self.stock = newStock

    def __str__(self):
        return self.location
    