class Attack:
    def __init__(self, name, type, category, power, accuracy, pp):
        self.name = name
        self.type = type
        self.category = category
        self.power = power
        self.accuracy = accuracy
        self.pp = pp

class Tackle(Attack):
    def __init__(self):
        super().__init__('tackle', 'normal', 'physical', 35, 0.95, 35)