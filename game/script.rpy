# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define m = Character ("Mugger", color = "#303030", image = "mug")
define a = Character ("Airplane Announcer", color = "#ffffff" , image = "airplane announcer")
define p = Character ("Johnny", color = "#330808" , image = "pho")
define k = Character("Konrad", color = "#067d26" , image = "kon")
define t = Character("Tai zhou", color = "#14234d" , image = "tai")

int python:
    $ Physical = min(max_physical,0)
    $ Intellectual = min(max_intellectual,0)
    $ Emotional = min(max_emotional,0)
    $ max_physical = 25
    $ max_emotional = 25
    $ max_intellectual = 25

    $ prev_trait = None
    $ combo_bonus = 2 # can be balanced

    $ add_physical_score(score=1):
        if prev_trait == 'Physical':
            Physical += score + combo_bonus
            # Todo: update trait bar and show combo sparkle
        else:
            prev_trait = 'Physical'
            Physical += score
            # Todo: update trait bar
            
    $ add_emotional_score(score=1):
        if prev_trait == 'Emotional':
            Emotional += score + combo_bonus
            # Todo: update trait bar and show combo sparkle
        else:
            prev_trait = 'Emotional'
            add_emotional += score
            # Todo: update trait bar

    $ add_intellectual_score(score=1):
        if prev_trait == 'Intellectual':
            Intellectual += score + combo_bonus
            # Todo: update trait bar and show combo sparkle
        else:
            prev_trait = 'Intellectual'
            Intellectual += score
            # Todo: update trait bar

screen physical_screen():
    frame:
        xoffset -1730
        align(1.0, 0.0)
        text "Physical: [Physical]"

screen intellectual_screen():
    frame:
        xoffset -860
        align(1.0, 0.0)
        text "Intellectual: [Intellectual]"

screen emotional_screen():
    frame:
        align(1.0, 0.0)
        text "Emotional: [Emotional]"


# The game starts here.

label start:
    show screen physical_screen()
    show screen intellectual_screen()
    show screen emotional_screen()
    jump touchdown
    return
