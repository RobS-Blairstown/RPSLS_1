

class Player:
    def __init__(self, gesture):
        self.gesture = ['Rock', 'Paper', 'Scissors', 'Lizard', 'Spock']


# class Rock(Player):
#     def __init__(self):
#         self.rock_beats = ['Scissors', 'Lizard']
#         super().__init__()
#
#
# class Paper(Player):
#     def __init__(self):
#         self.paper_beats = ['Rock', 'Spock']
#         super().__init__()
#
#
# class Scissors(Player):
#     def __init__(self):
#         self.scissor_beats = ['Paper', 'Lizard']
#         super().__init__()
#
#
# class Lizard(Player):
#     def __init__(self):
#         self.lizard_beats = ['Spock', 'Paper']
#         super().__init__()
#
#
# class Spock(Player):
#     def __init__(self):
#         self.spock_beats = ['Scissors', 'Rock']
#         super().__init__()
#

# display gesture options class
class DisplayGesture(Player):
    def __init__(self):
        self.display_gesture = input(f'{Player.gesture}')
        return self.display_gesture


# assign a gesture to a player class
class AssignGesture(DisplayGesture):
    def __init__(self, assign_gesture):
        self.display_gesture = assign_gesture



