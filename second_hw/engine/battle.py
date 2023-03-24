from engine.state_machine import *

class Battle(State):
    trainer = None

    def run(self, *args):
        pass


    def update(self):
        pass

    def __str__(self):
        return '[State: ' + self.name + ']'

    def __repr__(self):
        return str(self)


## methods
battle = Battle('Battle')