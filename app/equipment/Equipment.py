class Equipment:

    def __init__(self, name, description, breakage, price):
        self.name = name
        self.description = description
        self.breakage = breakage
        self.price = price

    def getName(self):
        return self.name

    def setName(self, newName):
        self.name = newName

    def getDescription(self):
        return self.description

    def setDescription(self, newDescription):
        self.description = newDescription

    def getBreakage(self):
        return self.breakage

    def setBreakage(self, newBreakage):
        self.breakage = newBreakage

    def getPrice(self):
        return self.price

    def setPrice(self, newPrice):
        self.price = newPrice

    def __str__(self):
        return f'-{self.name}: {self.description} ' + str(self.breakage) + '% ' + 'of breakage. ' + str(self.price) + ' crowns.'