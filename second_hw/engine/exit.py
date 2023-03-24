from engine.state_machine import *


class Exit(State):

    def run(self, *args):
        exit()

    def update(self):
        pass

    def __str__(self):
        return '[State: ' + self.name + ']'

    def __repr__(self):
        return str(self)


## methods
close = Exit('Exit')
