# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define m = Character ("Mugger", color = "#f90808", image = "mugger")
define a = Character ("Airplane Announcer", color = "#ffffff" , image = "airplane announcer")
define p = Character ("Phone", color = "#5e0101" , image = "phone")
define k = Character("Konrad", color = "#08f1f9" , image = "konrad")
define t = Character("Taizhou", color = "#93E9BE" , image = "taizhou")
define j = Character("Johnny", color = "#8303fb", image = "johnny")



init:
    $ Physical = 0;
    $ Intellectual = 0;
    $ Emotional = 0;

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
