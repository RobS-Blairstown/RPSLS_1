

class Player:
    def __init__(self):
        self.gesture = [Rock(), Paper(), Scissors(), Lizard(), Spock()]


class Rock:
    def __init__(self):
        self.name = 'Rock'
        self.loses_to = ['Paper', 'Spock']


class Paper:
    def __init__(self):
        self.name = 'Paper'
        self.loses_to = ['Scissors', 'Lizard']


class Scissors:
    def __init__(self):
        self.name = 'Scissors'
        self.loses_to = ['Rock', 'Spock']


class Lizard:
    def __init__(self):
        self.name = 'Lizard'
        self.loses_to = ['Rock', 'Scissors']


class Spock:
    def __init__(self):
        self.name = 'Spock'
        self.loses_to = ['Lizard', 'Paper']
#

# display gesture options class
class Human(Player):
    def __init__(self, chosen_gesture):
        self.chosen_gesture = ''

#create AI class

class AI(Player):
    def __init__(self, chosen_gesture):
        self.chosen_gesture = ''

