class budgetItem:
    def __init__(self, price, food):
        self.price = price
        self.food = food
    
    def setPrice(self, price):
        self.price = price

    def getPrice(self):
        return self.price

    def setFood(self, food):
        self.food = food

    def getFood(self):
        return self.food
