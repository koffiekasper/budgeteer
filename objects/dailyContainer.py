from datetime import date

class dailyContainer:
    # personalMacros = User's PersonalMacros Object. Used to check total macros of container against personal macros
    # margin = float between 0 and 1. Represents percentage that container's item's macros are allowed to go over personal macros. e.g. with 2000 calories a value of 0.1 would mean that all combined items in the container can total up to and not over 2100 calories
    def __init__(self, personalMacros, margin):
        self.date = date.today()
        self.itemList = []
        self.personalMacros = personalMacros
        self.margin = margin
    
    def addItem(self, item, amount):
        if self.testItem(item, amount):
            self.itemList.append(item)

    def getTotalMacros(self):
        total = {
            "calories" : 0,
            "fats" : 0,
            "protein" : 0,
            "carbohydrates" : 0
        }

        for budgetItem in self.itemList:
            foodItem = budgetItem.getFood()
            unitMacros = foodItem.getMacrosPerPortion()
            total["calories"] += unitMacros["calories"]
            total["fats"] += unitMacros["fats"]
            total["protein"] += unitMacros["protein"]
            total["carbohydrates"] += unitMacros["carbohydrates"]
        
        return total 

    def getTotalCalories(self):
        return self.getTotalMacros()["calories"]

    def getTotalFats(self):
        return self.getTotalMacros()["fats"]

    def getTotalCarbohydrates(self):
        return self.getTotalMacros()["carbohydrates"]

    def getTotalProtein(self):
        return self.getTotalMacros()["protein"]

    def testItem(self, item, amount):
        foodItem = item.getFood()
        unitMacros = foodItem.getMacrosPerPortion()
        total = self.getTotalMacros()

        for i in range(amount):
            total["calories"] += unitMacros["calories"]
            total["fats"] += unitMacros["fats"]
            total["protein"] += unitMacros["protein"]
            total["carbohydrates"] += unitMacros["carbohydrates"]

        if self.personalMacros.calories * (1 + self.margin) < total["calories"]:
            return False

        if self.personalMacros.protein * (1 + self.margin) < total["protein"]:
            return False

        if self.personalMacros.fats * (1 + self.margin) < total["fats"]:
            return False

        if self.personalMacros.carbohydrates * (1 + self.margin) < total["carbohydrates"]:
            return False
        
        return True