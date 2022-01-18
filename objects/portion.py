class portion:
    # amountSize: int. The amount contained in a package. (e.g. 6 for a 6 pack of beer. 400 for 400 grams of rice)
    # portionSize: int. The amount of unit quantified per portion. (e.g. 1 for 1 beer. 100 for 100 grams of rice)
    # unit: string. Type of unit. (e.g. 'can' for beer, 'gr' for grams of rice)
    def __init__(self, amountSize, portionSize, unit):
        self.amountSize = amountSize
        self.portionSize = portionSize
        self.unit = unit

    def setAmountSize(self, amountSize):
        self.amountSize = amountSize

    def setPortionSize(self, portionSize):
        self.portionSize = portionSize

    def changeUnit(self, unit):
        self.unit = unit 