class Item:
    def __init__(self, name, number, max):
        self.name = name
        self.number = number
        self.max = max


class Potions(Item):
    def __init__(self):
        super().__init__('Potion', 10, 10)


class Pokeballs(Item):
    def __init__(self):
        super().__init__('Pokeball', 10, 10)
