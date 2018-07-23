# importing random int maker module
from random import randint


# class defines what happens when a player dies.
# in this case, it has a list of phrases to be displayed
# randomly, and returns the string 'died' to let the engine know.
class Death(object):
    quips = ["Wow, you messed up... as usual",
             "Unlucky again... or is it perhaps a lack of skill",
             "Of course this was another forgettable error.",
             "I'm sorry you feel that way about yourself, and if you didn't, you should.",
             "Better luck in another life.",
             "Ouch, that would've hurt more, if you understood the depth of your incompetence."
             ]

    def enter(self):
        print(Death.quips[randint(0, len(self.quips) - 1)])
        return 'died'
