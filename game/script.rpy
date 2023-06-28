# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define m = Character ("Mugger", color = "#303030", image = "mug")
define a = Character ("Airplane Announcer", color = "#ffffff" , image = "airplane announcer")
define p = Character ("Phone", color = "#330808" , image = "phone")
define k = Character("Konrad", color = "#067d26" , image = "kon")
define t = Character("Taizhou", color = "#14234d" , image = "tai")
define j = Character("Johnny", color = "#330808", image = "joh")

default Physical = 0
default Intellectual = 0
default Emotional = 0

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
