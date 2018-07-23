# imports random madule form library
from random import randint
import time
# the base class for the scenes. 
# Each scene has one variable name, and three functions: enter(), action(), and exit_scene(). 
# Read through the ones given, feel free to add more using the same template I've given you.
# Change, edit, or completely remove the scenes I gave you. Up to you.
class Scene(object):

    def enter(self):
        print ("This is the base scene class that's inherited by the other scenes, so it is not configured yet.")
        print ("Subclass it and implement enter(), action(), and exit_scene() for each scene.")
        exit(1)

class OWeek(Scene):

    name = 'O-Week'

    @property
    def enter(self):
        print("You are a college student-- a person whose future is on route but whose failure is just as easily available.\n")

        print("It is a time for change; a time to move away from the vices that weighed you down but also a moment from which\n"
        "the virtues of familiarity have too left./n You are scared, and, as stupid as that might sound, you know that "
        "statement resonates deeply, for it's truth can only be as hidden as your shaking hands and wavering eyes can "
        "deny.\n")
        print()
        print(
        "It's O-Week-- orientation-- an although high school has bludgeoned you wit this so pettily before, you can't "
        "help but feel as though all eyes are on you.\nThere is no reason for this; you aren't abnormally tall nor "
        "short, you aren't ugly nor stupid, you're not wearing a MAGA hat nor exuberating conspicuity, and yet all you "
        "can feel are glances piercing through your skin with every step you take on the QUAD.")
        print()
        print(
        "It is now you realize you must take action and gets past your nervous tremors. You have to take control. THIS "
        "IS THE LIFE OF THE MIND, and you are the player. It is now your job to overcome your phobias before classes "
        "start.")
        print()
        print(
        "A girl walks up to you, and you're heart rate begins to raise. She's beautiful-- a Chicana with curly hair."
        "She asks you, if you're willing to go to a party with her and her friends around the block. At that same moment,?"
        "you get a text from an old friend who lives in Chicago, asking you to come over and play on his PS4.\nQUICK!")
        print("What do you do")

        return self.action

    @property
    def action(self):
        print("What do you do?")
        print("Type 1 for: Reject her and go to your old friend's house.")
        print("Type 2 for: Reject him and go to the party.")
        print("Type 3 for Reject both and begin studying for your class next week-- math.")
        print("Type 4 to go to both functions.")
        choice = input("> ")
        if choice == ':q':
            return self.exit_scene(choice)
        # this is some exception handling, you don't need to worry about it,
        # just accept that it works and keeps the program from falling apart.
        try:
           choice = int(choice)
        except ValueError:
           print("That's not an int!")
           return self.exit_scene(self.name)

        if choice == 1:
            print(
            "In your mind, you merely let her down and move on with your life, but your nervous stupor"
            "won't allow you to leave this interaction with impunity. Tripping over your words you say,'No, I don't"
            "want to go to your dumb party-- dumb girl. Hmmm, how'd that happen; everything was going so well. She'd even"
            "begun to show interest with her gleaming eyes and beautiful smile.\n BUT NO... You're phobia and social anxiety has gotten to you."
            "She looks at you in disbelief for a couple seconds, before finally throwing her drink (one that seemingly came out of nowhere)"
            "onto your nervous face; she walks away to her friends and talks about you and your rude antics. Looks like you will not have"
            "a nice O-Week nor good reputation in the near future. How sad :(")
        return self.exit_scene('death')




        elif int(choice) == 1:
        print(
            "Okay, so you decide to go to her party. Everything is cool, and everyone is having fun. Not you, though. It seems like you don't"
            "know anybody here, and again, you seem like the lonely kid in the corner.\n You're not about to give up however, and something in you"
            "changes, and you walk up to the beautiful girl who invited you there. Somehow you gather the courage to ask her out... AND\n "
            ".... she says No. Maybe it's because you confused here name with Marla (you're ex) or maybe it's Maybelline. Well, at least you tried.  "
            )
        return self.exit_scene('death')


        elif int(choice) == 2:
        print (
               "You reject both of them at the same time, but for whatever reason your mouth doesn't want to speak nicely."
               "You make it clear you don't want to see her again despite her beauty, but your thumbs have to erred. Your friend Mario"
               "is ignored and waits for you patientily, as if you were to ever respond.\n It's 12 am, and you're studying for your math class"
               "Mario calls and  you reject his call. He calls again-- reject. Calls-- you hangs up.\n Call after call, DM after DM, you go back to "
               "your math. Finally, annoyed, you tell Mario he doesn't deserve your friendship.\n Seems like you won't be getting many more calls from him.")
        return self.exit_scene('Relationship')

        elif int(choice) == 3:
        print(
              "So is this path you really want to take-- the one where you sexually harass and innocent girl, and kiss here against her will. Need I"
              "say more.\n NEED I SAY MORE!")
        elif int(choice) == 4:

        print(
            "You decide to go to both functions, attending the latter (the party) after going to your friends house. It is there that you play a couple video games."
            "You hang out with him and understand why he was such a good friend-- and maybe a bit more. He's a good guy and you've grown attached to him. It's and odd thing, really."
            "So, you, decide to stay a bit longer... and longer... and longer\n The hours go by, and suddenly you realize that "
    )

        else:
        print ("DOES NOT COMPUTE! Choose an option or type :q to end game") # raise ValueError ('todo')
        return self.exit_scene(self.name)

    def exit_scene(self, outcome):
        return outcome

class Relationship(Scene):

    name = 'Relationship'

    def enter(self):
        print ("It's been a couple months, and suddenly it seems you're happy. You have a loving girlfriend and satisfactory confidence"
               "There is still something, however, that is holding you back, and you need to get rid of it. It's almost as if you're happiness"
               "is a mere facade.\n There lie a couple options to change the stagnancy your life has fallen into, but will you take them.\n")
        time.sleep(3)
        print ("Will you take your life into your own hands and take this unknown risks.")
        return self.action()

    def action(self):
        print("Select 1 to do IT and 2 to live in monotony forever.")
        choose = input("> ")
        if int(choose) == 1:
            time.sleep(4)
            print("Let's do this")
            return self.exit_scene('Breakup')
        elif int(choose) == 2:
            time.sleep(3)
            print("Too sad, so bad...")
            return self.exit_scene('death')


class Breakup(Scene):
    name = "Breakup"
    def enter(self):
        print("Oh, it's the time to do it. YOU FOUND YOUR PROBLEM. ")

    def action(self):
        print ("There's a keypad lock on the box")
        print()
        code = [randint(0,9), randint(0,9), randint(0,9)]
        guesses = 0
        # loop to check three random integers, one at a time
        for i in range(3):
            print ("Enter digit %d." % (i+1))
            guess = input("[keypad]> ")
            if guess == ':q':
                return self.exit_scene(guess)
            try:
               guess = int(guess)
            except ValueError:
               print("That's not an int!")
               return self.exit_scene(self.name)
            while int(guess) != code[i] and guesses <10:
                print ("BZZZZEDDD!")
                guesses += 1
                guess =input("[keypad]> ")
                if guess == ':q':
                    return self.exit_scene(guess)
                try:
                   guess = int(guess)
                except ValueError:
                   print("That's not an int!")
                   guess = -1

        if guesses < 10:
            print ("The container clicks open and the seal breaks, letting gas out.")
            print()
            return self.exit_scene('public_scorn')
        else:
            print ("The lock buzzes one last time and then you hear a sickening")
            print()
            return self.exit_scene('death') # raise ValueError ('todo')

    def exit_scene(self, outcome):
        return outcome
class PublicScorn(Scene):
    name ='public_scorn'

    def enter(self):
        print("I am really really sad because certain parts of this won't work.")
        return self.action

    @property
    def action(self):
        print("What will you do? How will you regain the commendation of you and your peers. Will you 1) try to gain a new girlfriend or 2)")
        print()
        time.sleep (4)
        print("The fate of your college career-- your future and your relationships rests on it.")
        print()
        choice = input("> ")

        if int(choice) == 1:
            print("Okay, so you are searching for friends, but of course, you're interpersonal skills really suck and you are prone to errors.")
            print()
            print("As a result, you can only speak and socialize with a limited number of people and you mess up beyond repair")
            print("")
            time.sleep(5)

            codes = [randint(0, 9), randint(0, 9), randint(0, 9)]
            guesses = 0
            # loop to check three random integers, one at a time
            for i in range(3):
                print("Enter digit %d." % (i + 1))
                guess = input("[keypad]> ")
                if guess == ':q':
                    return self.exit_scene(guess)
                try:
                    guess = int(guess)
                except ValueError:
                    print("That's not an int!")
                    return self.exit_scene(self.name)
                while int(guess) != codes[i] and guesses < 10:
                    print("BZZZZEDDD!")
                    guesses += 1
                    guess = input("[keypad]> ")
                    if guess == ':q':
                        return self.exit_scene(guess)
                    try:
                        guess = int(guess)
                    except ValueError:
                        print("That's not an int!")
                        guess = -1

            if guesses < 10:
                print("The container clicks open and the seal breaks, letting gas out.")
                print()
                return self.exit_scene('Finish')
            else:
                print("The lock buzzes one last time and then you hear a sickening")
                print()
                return self.exit_scene('death')

        return self.action

    def exit_scene(self, outcome):
        return self.action


class Finish(Scene):

    name = 'Finish'

    def enter(self):
        return self.action()


    def action(self):
        print ("There's 5 pods, which one do you take?")
        good_pod = randint(1,5)
        guess = input("[pod #]> ")

        if guess == ':q':
            return self.exit_scene(guess)
        try:
           guess = int(guess)
        except ValueError:
           print("That's not an int!")
           return self.exit_scene(self.name)

        if int(guess) != good_pod:
            print ("You jump into pod %s and hit the eject button."% guess)
            print()
            return self.exit_scene('death')
        else:
            print ("You jump into pod %s and hit the eject button."% guess)
            print()
            return self.exit_scene('finished')

    def exit_scene(self, outcome):
        return outcome