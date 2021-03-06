"""Utility classes and methods for turtles
to keep turtles.py clean
clean turtles
"""


class Turtle:
    """base class for bots to be run using the 'deap' genetic algorithm library
    """
    def __init__(self, env, reward, file_handler):
        """
        Arguments:
          - env (<retro.retro_env.RetroEnv obj>): Open AI Retro Game Environment
          - reward (int): current reward value
          - file_handler (<FileHandler obj>): for creating game replays
        """
        self.env = env
        self.reward = reward
        self.file_handler = file_handler


class Direction:
    """For states and state transitioning
    """
    def __init__(self, name, key, transitions={}):
        """Initially a direction only has a name

        Arguments:
          - name (str): name of the direction
          - key (int or None): int associated with the gamepad key of this direction
          - transitions (dict): <Direction objects> with associated probabilities as values
        """
        self.name = name
        self.key = key
        self.transitions = transitions

    def __repr__(self):
        return 'Directions: ' + str(self.transitions)

    def update_transitions(self, name, probability):
        """Since not all connected states might be defined at initialization
        this method sets the connected states after initialization

        this method updates the transitions dict

        Arguments:
          - name (str): name of <Direction obj>
          - probability (dict): has `start` and `end` keys, creating a numeric range
                                which represent a probability
                                so {'start': 13, 'end': 23} would be a 10 percent chance
        """
        self.transitions[name] = probability
