class FoodInfo:
'''
Класс для удобного хранения калорийности продуктов.
'''
    def __init__(self, proteins, fats, carbohydrates):
        self.proteins = proteins
        self.fats = fats
        self.carbohydrates = carbohydrates
        self.kcalories = (4*self.proteins) + (9*self.fats) + (4*self.carbohydrates)

    def get_proteins(self):
        return self.proteins

    def get_fats(self):
        return self.fats

    def get_carbohydrates(self):
        return self.carbohydrates

    def get_kcalories(self):
        kcalories = (4*self.proteins) + (9*self.fats) + (4*self.carbohydrates)
        return kcalories

    def __eq__(self, other):
        return (self.kcalories) == (other.kcalories)

    def __ne__(self, other):
        return (self.kcalories) != (other.kcalories)

    def __lt__(self, other):
        return (self.kcalories) < (other.kcalories)

    def __gt__(self, other):
        return (self.kcalories) > (other.kcalories)

    def __le__(self, other):
        return (self.kcalories) <= (other.kcalories)

    def __ge__(self, other):
        return (self.kcalories) >= (other.kcalories)

    def __add__(self, other):
        aa = self.fats + other.fats
        bb = self.proteins + other.proteins
        cc = self.carbohydrates + other.carbohydrates
        return FoodInfo(aa, bb, cc)