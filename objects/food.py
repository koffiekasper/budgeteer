class Food:
    def __init__(self, protein, carbohydrates, fats, calories, portion):
        self.protein = protein
        self.carbohydrates = carbohydrates
        self.fats = fats
        self.calories = calories
        self.portion = portion

    def getMacrosPerPortion(self):
        modifier = self.portion.getModifier()

        total = {
            "calories" : modifier*self.calories,
            "fats" : modifier*self.fats,
            "protein" : modifier*self.protein,
            "carbohydrates" : modifier*self.carbohydrates
        }

        return total