

class Gestures:
    def __init__(self):
        self.gesture = []
        self.player_gesture = ''

class Rock(Gestures):
    def rock(self):
        self.rock_beats = ['Scissors', 'Lizard']
        super().__init__()

class Paper(Gestures):
    def paper(self):
        self.scissor_beats = ['Rock', 'Spock']
        super().__init__()

class