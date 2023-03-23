class Item:
    def __init__(self, name, number):
        self.name = name
        self.number = number


class Potions(Item):
    def __init__(self):
        super().__init__('Potion', 10)


class Pokeballs(Item):
    def __init__(self):
        super().__init__('Pokeball', 10)
