class Pizza:
    __HAWAIIAN_INGREDIENTS = ["ham", "pineapple"]
    __PEPPERONI_INGREDIENTS = ["bacon", "mozzarella", "oregano"]
    __MARGHERITA_INGREDIENTS = ["mozzarella", "olives", "tomatoes"]

    __order_counter = 0

    def __init__(self, ingredients: list):
        Pizza.__order_counter += 1

        self.__ingredients = ingredients
        self.__order_number = Pizza.__order_counter

    @classmethod
    def hawaiian(cls):
        return cls(cls.__HAWAIIAN_INGREDIENTS)

    @classmethod
    def pepperoni(cls):
        return cls(cls.__PEPPERONI_INGREDIENTS)

    @classmethod
    def margherita(cls):
        return cls(cls.__MARGHERITA_INGREDIENTS)

    @property
    def order_number(self):
        return self.__order_number

    @property
    def ingredients(self):
        return self.__ingredients

    @ingredients.setter
    def ingredients(self, ingredients: list):
        self.__ingredients = ingredients


p1 = Pizza(['bacon', 'parmesan', 'ham'])  # order 1
p2 = Pizza.pepperoni()  # order 2
print(p1.ingredients)  # ➞ ['bacon', 'parmesan', 'ham']
print(p2.ingredients)  # ➞ ['bacon', 'mozzarella', 'oregano']
print(p1.order_number)  # ➞ 1
print(p2.order_number)  # ➞ 2
