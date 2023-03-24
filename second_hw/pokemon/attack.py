class Attack:
    def __init__(self, name, type, category, power, accuracy, pp, current_pp):
        self.name = name
        self.type = type
        self.category = category
        self.power = power
        self.accuracy = accuracy
        self.pp = pp
        self.current_pp = current_pp

class Tackle(Attack):
    def __init__(self):
        super().__init__('tackle', 'normal', 'physical', 35, 0.95, 35, 35)

class RazorLeaf(Attack):
    def __init__(self):
        super().__init__('razor leaf', 'grass', 'physical', 55, 0.95, 25, 25)

class Ember(Attack):
    def __init__(self):
        super().__init__('ember', 'fire', 'special', 40, 1.0, 25, 25)

class WaterGun(Attack):
    def __init__(self):
        super().__init__('water gun', 'water', 'special', 40, 1.0, 25, 25)