# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define m = Character ("Mugger", color = "#303030", image = "mug")
define a = Character ("Airplane Announcer", color = "#ffffff" , image = "airplane announcer")
define p = Character ("Johnny", color = "#330808" , image = "pho")
define k = Character("Konrad", color = "#067d26" , image = "kon")
define t = Character("Tai zhou", color = "#14234d" , image = "tai")

define final = "audio/vn_Orchestral_final_-_Combo_version_of_the_songs.ogg"
define bells = "audio/vn_Bells_final.ogg"
define brass = "audio/vn_Brass_final.ogg"
define stringflute = "audio/vn_String_and_Flute_final.ogg"

init python:
    physical = 0
    intellectual = 0
    emotional = 0

    prev_trait = None

    # These 4 values can be tweaked to balance the endings
    max_physical = 10
    max_intellectual = 10
    max_emotional = 10
    combo_bonus = 2

    def show_combo():
        renpy.notify('Combo!')

    def add_physical_score(score=1):
        global physical, prev_trait

        if prev_trait == 'physical':
            physical += score + combo_bonus
            show_combo()
        else:
            prev_trait = 'physical'
            physical += score
            
    def add_emotional_score(score=1):
        global emotional, prev_trait

        if prev_trait == 'emotional':
            emotional += score + combo_bonus
            show_combo()
        else:
            prev_trait = 'emotional'
            emotional += score

    def add_intellectual_score(score=1):
        global intellectual, prev_trait

        if prev_trait == 'intellectual':
            intellectual += score + combo_bonus
            show_combo()
        else:
            prev_trait = 'intellectual'
            intellectual += score


screen physical_screen():
    frame:
        xoffset -1720
        align(1.0, 0.0)
        text "Physical: [physical] "

screen intellectual_screen():
    frame:
        xoffset -860
        align(1.0, 0.0)
        text "Intellectual: [intellectual] "

screen emotional_screen():
    frame:
        align(1.0, 0.0)
        text "Emotional: [emotional] "


# The game starts here.

label start:
    stop music
    show screen physical_screen()
    show screen intellectual_screen()
    show screen emotional_screen()
    jump touchdown
    return
