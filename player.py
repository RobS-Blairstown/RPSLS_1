from human import Human
from ai import AI
from spock import Spock
from scissors import Scissors
from lizard import Lizard
from paper import Paper
from rock import Rock


class Player:
    def __init__(self):
        self.gesture = [Rock(), Paper(), Scissors(), Lizard(), Spock()]


