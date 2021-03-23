from player import Player
from spock import Spock
from scissors import Scissors
from lizard import Lizard
from paper import Paper
from rock import Rock

class Human(Player):
    def __init__(self, chosen_gesture):
        self.chosen_gesture = ''
