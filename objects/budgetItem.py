class budgetItem:
    def __init__(self, price, food, portion):
        self.price = price
        self.food = food
        self.portion = portion
    
    def setPrice(self, price):
        self.price = price

    def getPrice(self):
        return self.price

    def setFood(self, food):
        self.food = food

    def getFood(self):
        return self.food

    def setPortion(self, portion):
        self.portion = portion

    def getPortion(self):
        return self.portion