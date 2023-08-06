from engine.state_machine import *


class Story(State):
    trainer = None

    def run(self, *args):
        print('We are in the main story!')

    def update(self, choices):
        print(self.choices)

    def __str__(self):
        return '[State: ' + self.name + ']'

    def __repr__(self):
        return str(self)

# methods
story = Story('Story')
